"""微信视频号平台 API 端点"""

from typing import Optional, Dict, Any


class WechatChannelsAPI:
    """
    微信视频号平台 API 集合

    包含视频号作品搜索、账号搜索、作品详情、链接提文案等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 作品相关（广域库） ──────────────────────────────────

    def search_works(
        self,
        keyword: str,
        sort: str = None,
        page: int = 1,
        size: int = 20,
        source: str = "微信视频号关键词搜索作品-SDK",
    ) -> dict:
        """
        搜索关键词获取视频号作品（广域库）

        :param keyword: 搜索关键词（模糊匹配内容描述，必填）
        :param sort: 排序方式：综合 / 最新 / 最多点赞 / 最多收藏，默认综合
        :param page: 页码，从 1 开始，默认 1
        :param size: 每页条数，默认 20，最大 50
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword, "page": page, "size": size}
        if sort is not None:
            data["sort"] = sort
        return self._client.post("/story/api/sphAllData/searchWork", data=data, source=source)

    def get_work(self, video_id: str, source: str = "获取微信视频号单个作品详情-SDK") -> dict:
        """
        获取视频号作品内容详情（广域库）

        :param video_id: 视频 ID（video_id，必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/sphAllData/queryWorkDetail", data={"videoId": video_id}, source=source
        )

    def get_user_works(
        self,
        nickname: str,
        page: int = 1,
        size: int = 20,
        source: str = "获取微信视频号用户作品列表-SDK",
    ) -> dict:
        """
        获取视频号账号作品列表（广域库）

        :param nickname: 视频号账号昵称（精准匹配，必填）
        :param page: 页码，从 1 开始，默认 1
        :param size: 每页条数，默认 20，最大 50
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"nickname": nickname, "page": page, "size": size}
        return self._client.post("/story/api/sphAllData/queryWorkList", data=data, source=source)

    def get_work_by_link(self, url: str, source: str = "通过链接获取微信视频号作品详情-SDK") -> dict:
        """
        视频号作品链接更新详情（实时）

        :param url: 视频号短链，如 https://weixin.qq.com/sph/xxx（必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/sph/ability/workLinkDetail", data={"url": url}, source=source
        )

    # ─── 账号相关 ───────────────────────────────────────────

    def search_users(
        self,
        account_name: str,
        page: int = 1,
        page_size: int = 20,
        source: str = "微信视频号关键词搜索账号-SDK",
    ) -> dict:
        """
        搜索关键词获取视频号账号（广域库）

        :param account_name: 视频号账号名称（模糊搜索关键词，必填）
        :param page: 页码，从 1 开始，默认 1
        :param page_size: 每页条数，默认 20，最大 50
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "accountName": account_name,
            "page": page,
            "pageSize": page_size,
        }
        return self._client.post("/story/api/sphAllData/searchUser", data=data, source=source)

    # ─── 链接提文案 ─────────────────────────────────────────

    def transcript_submit(self, url: str, source: str = "微信视频号视频字幕/文案提取-SDK") -> dict:
        """
        视频号链接提文案 - 提交任务

        :param url: 视频链接（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/parseWork/sphSubtitle/submit", data={"url": url}, source=source
        )

    def transcript_result(self, task_id: str, source: str = "查询微信视频号字幕提取任务结果-SDK") -> dict:
        """
        视频号链接提文案 - 查询结果

        :param task_id: 任务 ID（由 transcript_submit 返回）
        :return: 文案提取结果字典
        """
        return self._client.post(
            "/story/api/parseWork/sphSubtitle/result", data={"taskId": task_id}, source=source
        )
