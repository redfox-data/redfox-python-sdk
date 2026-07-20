"""RedFox SDK 核心客户端"""

import requests
from typing import Optional, Dict, Any

from .exceptions import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError
from .endpoints.douyin import DouyinAPI


class RedFoxClient:
    """
    RedFox 红狐数据平台客户端

    使用示例::

        from redfox import RedFoxClient

        client = RedFoxClient(api_key="your_api_key")

        # 搜索抖音作品
        result = client.douyin.search_articles(keyword="AI")

        # 获取账号信息
        user = client.douyin.get_user(account_id="dy_user123")

    :param api_key: RedFox API Key，在 https://redfox.hk/settings/api-keys?source=github 获取
    :param base_url: API 基础地址，默认 https://redfox.hk
    :param timeout: 请求超时时间（秒），默认 30
    """

    DEFAULT_BASE_URL = "https://redfox.hk"
    DEFAULT_TIMEOUT = 30

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        if not api_key:
            raise ValueError(
                "api_key 不能为空，请在 https://redfox.hk/settings/api-keys?source=github 获取"
            )

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json",
            "REDFOX_API_KEY": self.api_key,
        })

        # 初始化各平台 API 模块
        self.douyin = DouyinAPI(self)

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> dict:
        """
        发送 API 请求

        :param method: HTTP 方法（GET/POST）
        :param path: API 路径
        :param params: URL 查询参数
        :param data: 请求体 JSON 数据
        :return: API 响应 data 字段内容
        :raises RedFoxAPIError: API 返回错误时抛出
        """
        url = f"{self.base_url}{path}"

        # 过滤掉值为 None 的参数
        if data:
            data = {k: v for k, v in data.items() if v is not None}
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        try:
            response = self._session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=self.timeout,
            )
        except requests.exceptions.Timeout:
            raise RedFoxAPIError("请求超时，请稍后重试")
        except requests.exceptions.ConnectionError:
            raise RedFoxAPIError("网络连接失败，请检查网络")
        except requests.exceptions.RequestException as e:
            raise RedFoxAPIError(f"请求异常: {str(e)}")

        return self._handle_response(response)

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> dict:
        """发送 POST 请求"""
        return self.request("POST", path, data=data)

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> dict:
        """发送 GET 请求"""
        return self.request("GET", path, params=params)

    def _handle_response(self, response: requests.Response) -> dict:
        """处理 API 响应"""
        # HTTP 级别错误
        if response.status_code == 401:
            raise RedFoxAuthError(
                "API Key 无效或缺失，请在 https://redfox.hk/settings/api-keys?source=github 获取",
                code=401,
            )
        if response.status_code == 429:
            raise RedFoxRateLimitError("请求频率超限，请稍后重试", code=429)
        if response.status_code >= 500:
            raise RedFoxAPIError(f"服务端错误", code=response.status_code)

        try:
            result = response.json()
        except ValueError:
            raise RedFoxAPIError(f"响应解析失败: {response.text[:200]}")

        # 业务级别错误
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
