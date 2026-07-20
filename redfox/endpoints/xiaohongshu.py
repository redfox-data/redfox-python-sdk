"""小红书平台 API 端点"""

from typing import Optional, Dict, Any


class XiaohongshuAPI:
    """
    小红书平台 API 集合

    包含小红书账号查询、作品搜索、笔记详情等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 账号相关 ───────────────────────────────────────────

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post(
            "/story/api/redBookData/searchUser", data=data
        )

    def get_account(
        self,
        account_id: str,
        user_id: str = None,
    ) -> dict:
        """
        获取小红书账号信息（优质库）

        :param account_id: 小红书号（必填）
        :param user_id: 用户 ID（可选）
        :return: 账号信息字典
        """
        data: Dict[str, Any] = {"accountId": account_id}
        if user_id is not None:
            data["userId"] = user_id
        return self._client.post(
            "/story/api/redBookData/queryUser", data=data
        )

    # ─── 作品相关 ───────────────────────────────────────────

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post(
            "/story/api/redBookData/searchArticle", data=data
        )

    def get_work(
        self,
        work_id: str = None,
        work_link: str = None,
    ) -> dict:
        """
        获取小红书作品内容详情（优质库）

        work_id 和 work_link 至少传一个。

        :param work_id: 作品 ID
        :param work_link: 作品链接，如 https://www.xiaohongshu.com/explore/xxx
        :return: 作品详情字典
        """
        data: Dict[str, Any] = {}
        if work_id:
            data["workId"] = work_id
        if work_link:
            data["workLink"] = work_link
        return self._client.post(
            "/story/api/redBookData/queryWork", data=data
        )

    # ─── AI 作品 ────────────────────────────────────────────

    def search_ai_articles(
        self,
        keyword: str,
        page_num: int = 1,
        page_size: int = 20,
        start_time: str = None,
        end_time: str = None,
        source: str = None,
    ) -> dict:
        """
        搜索关键词获取小红书 AI 创作作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :param start_time: 起始时间，格式 "2026-06-01 00:00:00"
        :param end_time: 结束时间，格式 "2026-06-02 00:00:00"
        :param source: 来源平台（可选）
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
        if source is not None:
            data["source"] = source
        return self._client.post(
            "/story/api/parseWork/queryAiMsgs", data=data
        )
