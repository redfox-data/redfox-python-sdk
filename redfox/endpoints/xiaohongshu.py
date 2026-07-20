"""小红书平台 API 端点"""

from typing import Optional, Dict, Any


class XiaohongshuAPI:
    """
    小红书平台 API 集合

    包含小红书账号查询、作品详情、关键词搜索等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 账号相关 ───────────────────────────────────────────

    def get_account(
        self,
        account_id: str,
        user_id: str = None,
    ) -> dict:
        """
        获取小红书账号信息（优质库）

        :param account_id: 小红书号（必填）
        :param user_id: 用户 ID，可从主页链接提取
        :return: 账号信息字典
        """
        data: Dict[str, Any] = {"accountId": account_id}
        if user_id is not None:
            data["userId"] = user_id
        return self._client.post("/story/api/xhsUser/queryAccountDetail", data=data)

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post("/story/api/xhsUser/searchUser", data=data)

    # ─── 作品相关 ───────────────────────────────────────────

    def get_work(self, note_id: str) -> dict:
        """
        获取小红书作品内容详情（优质库）

        :param note_id: 笔记 ID
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/xhsUser/queryWorkDetail",
            data={"noteId": note_id},
        )

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post("/story/api/xhsUser/searchArticle", data=data)

    # ─── AI 作品 ────────────────────────────────────────────

    def search_ai_articles(
        self,
        keyword: str,
        page_num: int = 1,
        page_size: int = 20,
        start_time: str = None,
        end_time: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书 AI 作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :param start_time: 开始时间
        :param end_time: 结束时间
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "pageNum": page_num,
            "pageSize": page_size,
        }
        if start_time is not None:
            data["startTime"] = start_time
        if end_time is not None:
            data["endTime"] = end_time
        return self._client.post("/story/api/parseWork/queryXhsAiMsgs", data=data)
