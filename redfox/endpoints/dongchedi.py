"""懂车帝平台 API 端点"""

from typing import Optional, Dict, Any


class DongchediAPI:
    """
    懂车帝平台 API 集合

    包含懂车帝作品搜索、作品详情、用户作品列表、用户搜索等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        offset: str = "0",
        source_type: str = "1",
        source: str = "懂车帝关键词搜索作品-SDK",
    ) -> dict:
        """
        懂车帝关键词搜索作品

        :param keyword: 搜索关键词（必填）
        :param offset: 翻页偏移量，从 0 开始，翻页 +20
        :param source_type: 内容类型：1=综合，2=视频
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "offset": str(offset),
            "sourceType": str(source_type),
        }
        return self._client.post("/story/api/dongchedi/searchWork", data=data, source=source)

    def get_work(self, work_id: str, work_type: str, source: str = "获取懂车帝作品详情-SDK") -> dict:
        """
        懂车帝作品详情

        :param work_id: 懂车帝作品 ID（必填）
        :param work_type: 作品类型：video=视频，article=图文（必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/dongchedi/workDetail",
            data={"workId": work_id, "workType": work_type},
            source=source,
        )

    def get_user_works(self, user_id: str, cursor: int = 0, source: str = "获取懂车帝用户作品列表-SDK") -> dict:
        """
        懂车帝用户作品列表

        :param user_id: 用户 ID（必填）
        :param cursor: 游标，首次传 0，翻页传上一页返回的 cursor 值
        :return: 作品列表字典
        """
        return self._client.post(
            "/story/api/dongchedi/workList",
            data={"userId": user_id, "cursor": cursor},
            source=source,
        )

    def search_users(self, keyword: str, offset: int = 0, source: str = "懂车帝关键词搜索账号-SDK") -> dict:
        """
        懂车帝用户搜索

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量，从 0 开始
        :return: 搜索结果字典
        """
        return self._client.post(
            "/story/api/dongchedi/searchUser",
            data={"keyword": keyword, "offset": offset},
            source=source,
        )
