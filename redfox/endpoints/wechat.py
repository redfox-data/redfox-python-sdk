"""微信公众号平台 API 端点"""

from typing import Optional, Dict, Any


class WechatAPI:
    """
    微信公众号平台 API 集合

    包含公众号账号查询、作品搜索、文章详情等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 账号相关 ───────────────────────────────────────────

    def get_account(self, account: str, account_name: str = None) -> dict:
        """
        获取公众号账号信息（优质库）

        :param account: 公众号微信号（必填）
        :param account_name: 公众号名称（可选）
        :return: 账号信息字典
        """
        data: Dict[str, Any] = {"account": account}
        if account_name is not None:
            data["accountName"] = account_name
        return self._client.post("/story/api/gzhData/queryUser", data=data)

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取公众号账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式：_0=默认，_2=最新，_4=最热
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post("/story/api/gzhData/searchUser", data=data)

    # ─── 作品相关 ───────────────────────────────────────────

    def get_work(self, work_uuid: str) -> dict:
        """
        根据作品 UUID 获取公众号作品（优质库）

        :param work_uuid: 作品 UUID（必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/gzhData/queryWork", data={"workUuid": work_uuid}
        )

    def get_article_detail(self, url: str) -> dict:
        """
        根据作品地址获取公众号文章（优质库）

        :param url: 文章链接（必填）
        :return: 文章详情字典
        """
        return self._client.post(
            "/story/api/gzhData/queryArticleDetail", data={"url": url}
        )

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
    ) -> dict:
        """
        搜索关键词获取公众号作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post("/story/api/gzhData/searchArticle", data=data)

    def get_user_works(
        self,
        account: str,
        account_name: str = None,
        offset: int = 0,
        sort_type: str = None,
        publish_time_start: str = None,
        publish_time_end: str = None,
    ) -> dict:
        """
        获取公众号账号作品列表（优质库）

        :param account: 公众号微信号（必填）
        :param account_name: 公众号名称（可选）
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式：_0=默认，_2=最新，_4=最热
        :param publish_time_start: 发布时间起始，最早 2026-04-01，不传默认 2026-04-01
        :param publish_time_end: 发布时间结束，不传默认当前时间
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"account": account}
        if account_name:
            data["accountName"] = account_name
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        if publish_time_start is not None:
            data["publishTimeStart"] = publish_time_start
        if publish_time_end is not None:
            data["publishTimeEnd"] = publish_time_end
        return self._client.post("/story/api/gzhData/queryWorkList", data=data)

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
        搜索关键词获取公众号 AI 创作作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1（必填）
        :param page_size: 每页条数，默认 20（必填）
        :param start_time: 开始时间，格式 "2026-06-01 00:00:00"
        :param end_time: 结束时间，格式 "2026-06-01 23:59:59"
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
        return self._client.post("/story/api/parseWork/queryAiMsgs", data=data)
