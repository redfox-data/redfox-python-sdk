"""TikTok 平台 API 端点"""

from typing import Optional, Dict, Any


class TikTokAPI:
    """
    TikTok 平台 API 集合

    包含 TikTok 账号搜索等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_users(
        self,
        keyword: str,
        cursor: int = 0,
        rid: str = None,
    ) -> dict:
        """
        TikTok 关键词搜索账号

        :param keyword: 搜索关键词（必填）
        :param cursor: 翻页游标，第一页为 0，每页 +10
        :param rid: 数据返回的 rid，翻页时传入，第一页传空
        :return: 搜索结果字典，包含 cursor/hasMore/userList
        """
        data: Dict[str, Any] = {"keyword": keyword, "cursor": cursor}
        if rid is not None:
            data["rid"] = rid
        return self._client.post("/story/api/deepSearch/tk/searchUser", data=data)
