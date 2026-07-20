"""抖音平台 API 端点"""

from typing import Optional, Dict, Any


class DouyinAPI:
    """
    抖音平台 API 集合

    包含抖音作品搜索、账号查询、作品详情等接口。
    所有接口均为 POST 请求，参数通过 JSON body 传递。
    """

    def __init__(self, client):
        self._client = client

    # ─── 作品相关 ───────────────────────────────────────────

    def get_work(
        self,
        work_id: str = None,
        work_url: str = None,
    ) -> dict:
        """
        获取抖音作品内容详情（优质库）

        通过作品 ID 或作品链接查询作品详细信息，包括互动数据、作者信息等。
        work_id 和 work_url 至少传一个。

        :param work_id: 作品 ID，如 "10000123456789"
        :param work_url: 作品链接，如 "https://www.douyin.com/video/xxx"
        :return: 作品详情字典
        """
        data = {}
        if work_id:
            data["workId"] = work_id
        if work_url:
            data["workUrl"] = work_url

        return self._client.post("/story/api/dyData/queryWork", data=data)

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取抖音作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始，每次 +20
        :param sort_type: 排序方式，如 "default"
        :return: 搜索结果字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/searchArticle", data=data)

    def get_user_works(
        self,
        account_id: str = None,
        author_url: str = None,
        sec_user_id: str = None,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        获取抖音账号作品列表（优质库）

        account_id / author_url / sec_user_id 至少传一个。

        :param account_id: 抖音号
        :param author_url: 作者主页链接
        :param sec_user_id: 作者 sec_user_id
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式：0=默认，2=最新，4=最热
        :return: 作品列表字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {}
        if account_id:
            data["accountId"] = account_id
        if author_url:
            data["authorUrl"] = author_url
        if sec_user_id:
            data["secUserId"] = sec_user_id
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/queryWorkList", data=data)

    # ─── 账号相关 ───────────────────────────────────────────

    def get_user(self, account_id: str) -> dict:
        """
        获取抖音账号信息（优质库）

        :param account_id: 抖音账号 ID（支持 unique_id、short_id、uid 任一匹配）
        :return: 账号信息字典
        """
        return self._client.post(
            "/story/api/dyData/queryUser",
            data={"accountId": account_id},
        )

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取抖音账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始
        :param sort_type: 排序方式
        :return: 搜索结果字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/searchUser", data=data)

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
        搜索关键词获取抖音 AI 作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :param start_time: 开始时间，格式 "2026-06-01 00:00:00"
        :param end_time: 结束时间，格式 "2026-06-02 00:00:00"
        :return: 搜索结果字典，包含 total/pageNum/pageSize/pages/list
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

        return self._client.post("/story/api/parseWork/queryDyAiMsgs", data=data)
