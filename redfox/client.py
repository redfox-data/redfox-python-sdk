"""RedFox SDK 核心客户端 — 同步 + 异步双客户端，自动重试，零配置"""

import os
import time
import random
import logging
from typing import Optional, Dict, Any

import httpx

from .exceptions import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

# 导入端点（同步和异步共享同一套端点类）
from .endpoints.douyin import DouyinAPI
from .endpoints.xiaohongshu import XiaohongshuAPI
from .endpoints.wechat import WechatAPI
from .endpoints.bilibili import BilibiliAPI
from .endpoints.toutiao import ToutiaoAPI
from .endpoints.tiktok import TikTokAPI
from .endpoints.gpt_image import GPTImageAPI
from .endpoints.doubao_image import DoubaoImageAPI
from .endpoints.doubao_video import DoubaoVideoAPI
from .endpoints.ai_search import AISearchAPI

logger = logging.getLogger("redfox")

# 可重试的 HTTP 状态码
RETRYABLE_STATUSES = {429, 500, 502, 503, 504}

# 可重试的网络异常
RETRYABLE_EXCEPTIONS = (
    httpx.TimeoutException,
    httpx.ConnectError,
    httpx.RemoteProtocolError,
    httpx.NetworkError,
)


def _compute_delay(attempt: int, backoff_factor: float = 0.5) -> float:
    """计算指数退避延迟（含随机抖动）"""
    base = backoff_factor * (2 ** attempt)
    jitter = base * random.uniform(0.5, 1.5)
    return min(jitter, 30.0)  # 上限 30 秒


def _should_retry(status_code: int, exception: Optional[Exception] = None) -> bool:
    """判断是否应该重试"""
    if exception is not None:
        return isinstance(exception, RETRYABLE_EXCEPTIONS)
    return status_code in RETRYABLE_STATUSES


class _RequestMixin:
    """HTTP 请求 + 重试 + 响应处理的共享逻辑"""

    def _prepare_request(
        self, method: str, path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> tuple:
        """准备请求 URL 和清洗后的参数"""
        url = f"{self.base_url}{path}"
        if data:
            data = {k: v for k, v in data.items() if v is not None}
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        return url, params, data

    def _handle_response(self, response) -> dict:
        """处理 API 响应，提取 data 或抛出结构化异常"""
        if response.status_code == 401:
            raise RedFoxAuthError(
                "API Key 无效或缺失，请在 https://redfox.hk/settings/api-keys?source=github 获取",
                code=401,
            )
        if response.status_code == 429:
            raise RedFoxRateLimitError("请求频率超限，请稍后重试", code=429)
        if response.status_code >= 500:
            raise RedFoxAPIError("服务端错误", code=response.status_code)

        try:
            result = response.json()
        except ValueError:
            raise RedFoxAPIError(f"响应解析失败: {response.text[:200]}")

        code = result.get("code")
        if code and code != 2000:
            msg = result.get("msg", "未知错误")
            if code == 401 or code == 4001:
                raise RedFoxAuthError(
                    f"{msg}，请在 https://redfox.hk/settings/api-keys?source=github 获取有效的 API Key",
                    code=code,
                    response=result,
                )
            raise RedFoxAPIError(msg, code=code, response=result)

        return result.get("data", result)

    def _map_exception(self, exc: Exception) -> RedFoxAPIError:
        """将网络异常映射为 RedFoxAPIError"""
        if isinstance(exc, httpx.TimeoutException):
            return RedFoxAPIError("请求超时，请稍后重试")
        if isinstance(exc, (httpx.ConnectError, httpx.NetworkError)):
            return RedFoxAPIError("网络连接失败，请检查网络")
        return RedFoxAPIError(f"请求异常: {str(exc)}")


class RedFoxClient(_RequestMixin):
    """
    RedFox 红狐数据平台客户端（同步）

    使用示例::

        from redfox import RedFoxClient

        # 零配置：自动从环境变量 REDFOX_API_KEY 读取
        client = RedFoxClient()

        # 或显式传入
        client = RedFoxClient(api_key="ak_xxx")

        # 搜索抖音作品
        result = client.douyin.search_articles(keyword="AI")

        # 搜索小红书作品
        result = client.xiaohongshu.search_articles(keyword="AI")

        # AI 搜索
        task = client.ai_search.kimi_submit(inquiry_text="夏日茶饮推荐")

    :param api_key: RedFox API Key。不传则从环境变量 ``REDFOX_API_KEY`` 读取
    :param base_url: API 基础地址，默认 https://redfox.hk
    :param timeout: 请求超时（秒），默认 30
    :param max_retries: 最大重试次数（指数退避），默认 3
    :param backoff_factor: 退避基础因子，默认 0.5
    """

    DEFAULT_BASE_URL = "https://redfox.hk"
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_BACKOFF_FACTOR = 0.5

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    ):
        # 零配置：未传 api_key 时从环境变量读取
        if api_key is None:
            api_key = os.getenv("REDFOX_API_KEY", "")

        if not api_key:
            raise ValueError(
                "api_key 不能为空。请设置环境变量 REDFOX_API_KEY，"
                "或传入 api_key 参数。"
                "获取地址: https://redfox.hk/settings/api-keys?source=github"
            )

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        self._client = httpx.Client(
            timeout=httpx.Timeout(timeout),
            headers={
                "Content-Type": "application/json",
                "REDFOX_API_KEY": self.api_key,
            },
        )

        # 初始化各平台 API 模块（端点类与异步客户端共享）
        self.douyin = DouyinAPI(self)
        self.xiaohongshu = XiaohongshuAPI(self)
        self.wechat = WechatAPI(self)
        self.bilibili = BilibiliAPI(self)
        self.toutiao = ToutiaoAPI(self)
        self.tiktok = TikTokAPI(self)
        self.gpt_image = GPTImageAPI(self)
        self.doubao_image = DoubaoImageAPI(self)
        self.doubao_video = DoubaoVideoAPI(self)
        self.ai_search = AISearchAPI(self)

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> dict:
        """
        发送 API 请求（含自动重试 + 指数退避）

        :param method: HTTP 方法（GET/POST）
        :param path: API 路径
        :param params: URL 查询参数
        :param data: 请求体 JSON 数据
        :return: API 响应 data 字段内容
        :raises RedFoxAPIError: 重试耗尽后仍失败时抛出
        """
        url, params, data = self._prepare_request(method, path, params, data)
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,
                )

                # 需要重试的 HTTP 状态码
                if response.status_code in RETRYABLE_STATUSES and attempt < self.max_retries:
                    delay = _compute_delay(attempt, self.backoff_factor)
                    logger.debug(
                        "收到 %d，第 %d/%d 次重试，等待 %.1fs",
                        response.status_code, attempt + 1, self.max_retries, delay,
                    )
                    time.sleep(delay)
                    continue

                return self._handle_response(response)

            except RETRYABLE_EXCEPTIONS as exc:
                last_exception = exc
                if attempt < self.max_retries:
                    delay = _compute_delay(attempt, self.backoff_factor)
                    logger.debug(
                        "网络异常 %s，第 %d/%d 次重试，等待 %.1fs",
                        type(exc).__name__, attempt + 1, self.max_retries, delay,
                    )
                    time.sleep(delay)
                else:
                    raise self._map_exception(exc)

            except (RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError):
                # 业务异常不重试，直接抛出
                raise

        # 重试耗尽
        raise self._map_exception(last_exception) if last_exception else RedFoxAPIError("请求失败")

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> dict:
        """发送 POST 请求"""
        return self.request("POST", path, data=data)

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> dict:
        """发送 GET 请求"""
        return self.request("GET", path, params=params)

    def close(self):
        """关闭 HTTP 连接"""
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncRedFoxClient(_RequestMixin):
    """
    RedFox 红狐数据平台客户端（异步）

    使用示例::

        import asyncio
        from redfox import AsyncRedFoxClient

        async def main():
            async with AsyncRedFoxClient() as client:
                # 所有 API 调用与同步客户端完全一致，只需 await
                result = await client.douyin.search_articles(keyword="AI")
                print(result)

        asyncio.run(main())

    :param api_key: RedFox API Key。不传则从环境变量 ``REDFOX_API_KEY`` 读取
    :param base_url: API 基础地址，默认 https://redfox.hk
    :param timeout: 请求超时（秒），默认 30
    :param max_retries: 最大重试次数（指数退避），默认 3
    :param backoff_factor: 退避基础因子，默认 0.5
    """

    DEFAULT_BASE_URL = "https://redfox.hk"
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_BACKOFF_FACTOR = 0.5

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    ):
        if api_key is None:
            api_key = os.getenv("REDFOX_API_KEY", "")

        if not api_key:
            raise ValueError(
                "api_key 不能为空。请设置环境变量 REDFOX_API_KEY，"
                "或传入 api_key 参数。"
                "获取地址: https://redfox.hk/settings/api-keys?source=github"
            )

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        self._client = httpx.AsyncClient(
            timeout=httpx.Timeout(timeout),
            headers={
                "Content-Type": "application/json",
                "REDFOX_API_KEY": self.api_key,
            },
        )

        # 初始化各平台 API 模块（与同步客户端共享同一套端点类）
        self.douyin = DouyinAPI(self)
        self.xiaohongshu = XiaohongshuAPI(self)
        self.wechat = WechatAPI(self)
        self.bilibili = BilibiliAPI(self)
        self.toutiao = ToutiaoAPI(self)
        self.tiktok = TikTokAPI(self)
        self.gpt_image = GPTImageAPI(self)
        self.doubao_image = DoubaoImageAPI(self)
        self.doubao_video = DoubaoVideoAPI(self)
        self.ai_search = AISearchAPI(self)

    async def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> dict:
        """
        异步发送 API 请求（含自动重试 + 指数退避）

        :param method: HTTP 方法（GET/POST）
        :param path: API 路径
        :param params: URL 查询参数
        :param data: 请求体 JSON 数据
        :return: API 响应 data 字段内容
        """
        url, params, data = self._prepare_request(method, path, params, data)
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,
                )

                if response.status_code in RETRYABLE_STATUSES and attempt < self.max_retries:
                    delay = _compute_delay(attempt, self.backoff_factor)
                    logger.debug(
                        "收到 %d，第 %d/%d 次重试，等待 %.1fs",
                        response.status_code, attempt + 1, self.max_retries, delay,
                    )
                    await self._async_sleep(delay)
                    continue

                return self._handle_response(response)

            except RETRYABLE_EXCEPTIONS as exc:
                last_exception = exc
                if attempt < self.max_retries:
                    delay = _compute_delay(attempt, self.backoff_factor)
                    logger.debug(
                        "网络异常 %s，第 %d/%d 次重试，等待 %.1fs",
                        type(exc).__name__, attempt + 1, self.max_retries, delay,
                    )
                    await self._async_sleep(delay)
                else:
                    raise self._map_exception(exc)

            except (RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError):
                raise

        raise self._map_exception(last_exception) if last_exception else RedFoxAPIError("请求失败")

    async def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> dict:
        """异步发送 POST 请求"""
        return await self.request("POST", path, data=data)

    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> dict:
        """异步发送 GET 请求"""
        return await self.request("GET", path, params=params)

    async def _async_sleep(self, seconds: float):
        """异步延时"""
        import asyncio
        await asyncio.sleep(seconds)

    async def close(self):
        """关闭 HTTP 连接"""
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
