"""微博平台 API 端点"""

from typing import Optional, Dict, Any


class WeiboAPI:
    """
    微博平台 API 集合

    包含微博账号搜索、微博内容详情、用户详情等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_users(self, keyword: str, page: int = 1, source: str = "微博账号搜索-SDK") -> dict:
        """
        微博账号搜索

        :param keyword: 搜索关键词（必填）
        :param page: 分页，第一页传 1
        :return: 账号列表
        """
        return self._client.post(
            "/story/api/weibo/ability/accountSearch",
            data={"keyword": keyword, "page": page},
            source=source,
        )

    def get_work(self, opus_id: str, source: str = "获取微博内容详情-SDK") -> dict:
        """
        微博内容详情

        :param opus_id: 作品 ID（必填）
        :return: 微博详情字典
        """
        return self._client.post(
            "/story/api/weibo/ability/opusDetail",
            data={"opusId": opus_id},
            source=source,
        )

    def get_user(self, user_id: str, source: str = "获取微博用户详情-SDK") -> dict:
        """
        微博用户详情

        :param user_id: 用户 userId（必填）
        :return: 用户详情字典
        """
        return self._client.post(
            "/story/api/weibo/ability/userDetail",
            data={"userId": user_id},
            source=source,
        )
