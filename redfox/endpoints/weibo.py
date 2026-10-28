"""微博平台 API 端点"""

from typing import Optional, Dict, Any


class WeiboAPI:
    """
    微博平台 API 集合

    包含微博账号搜索、微博内容详情、用户详情、关键词搜索作品、热搜等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        search_type: str = "61",
        page: str = "1",
        ext_param: str = None,
        source: str = "微博关键词搜索作品-SDK",
    ) -> dict:
        """
        微博关键词搜索作品

        :param keyword: 搜索关键词（必填）
        :param search_type: 搜索类别：1=综合，3=搜索账号，60=热门，61=实时博文
        :param page: 页码（必填）
        :param ext_param: 认证类别："3"=机构认证，"2"=个人认证，"0"=普通用户；
                          不传则为搜索博文
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "searchType": str(search_type),
            "page": str(page),
            "keyword": keyword,
        }
        if ext_param is not None:
            data["extParam"] = ext_param
        return self._client.post(
            "/story/api/weibo/ability/searchWork", data=data, source=source
        )

    def get_hot_search(self, source: str = "微博热搜-SDK") -> dict:
        """
        微博热搜

        :return: 热搜列表字典，包含 list/cursor/hasMore/updateTime
        """
        return self._client.post(
            "/story/api/weibo/ability/hotSearch", data={}, source=source
        )

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
