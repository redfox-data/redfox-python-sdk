"""易车平台 API 端点"""

from typing import Optional, Dict, Any


class YicheAPI:
    """
    易车平台 API 集合

    包含易车作品搜索、文章/视频详情、账号搜索、账号作品列表等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        page: int = 1,
        source_type: str = "xinwen",
        source: str = "易车关键词搜索作品-SDK",
    ) -> dict:
        """
        易车关键词搜索作品

        :param keyword: 搜索关键词（必填）
        :param page: 页码，从 1 开始，翻页 +1
        :param source_type: 内容类型：club=社区，shipin=视频，xinwen=文章
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "page": page,
            "sourceType": source_type,
        }
        return self._client.post("/story/api/yiche/searchWork", data=data, source=source)

    def get_article(self, url: str, source: str = "获取易车文章详情-SDK") -> dict:
        """
        易车文章详情

        :param url: 文章 URL（必填）
        :return: 文章详情字典
        """
        return self._client.post(
            "/story/api/yiche/articleDetail", data={"url": url}, source=source
        )

    def get_article_v2(self, url: str, source: str = "获取易车文章详情V2-SDK") -> dict:
        """
        易车文章详情 V2

        :param url: 文章 URL（必填）
        :return: 文章详情字典
        """
        return self._client.post(
            "/story/api/yiche/articleDetailV2", data={"url": url}, source=source
        )

    def get_video(self, work_id: str, source: str = "获取易车视频详情-SDK") -> dict:
        """
        易车视频详情

        :param work_id: 易车视频作品 ID（必填）
        :return: 视频详情字典
        """
        return self._client.post(
            "/story/api/yiche/videoDetail", data={"workId": work_id}, source=source
        )

    def get_user_works(self, user_id: str, timestamp: str = None, source: str = "获取易车用户作品列表-SDK") -> dict:
        """
        易车全部作品列表

        :param user_id: 用户 ID（必填）
        :param timestamp: 时间戳，第一页不传，翻页传前一页返回的最后一条的 publishTime
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"userId": user_id}
        if timestamp is not None:
            data["timestamp"] = timestamp
        return self._client.post("/story/api/yiche/workList", data=data, source=source)

    def search_users(self, keyword: str, page: int = 1, source: str = "易车关键词搜索账号-SDK") -> dict:
        """
        易车账号搜索

        :param keyword: 搜索关键词（必填）
        :param page: 页码，从 1 开始
        :return: 搜索结果字典
        """
        return self._client.post(
            "/story/api/yiche/searchAccount",
            data={"keyword": keyword, "page": page},
            source=source,
        )
