"""汽车之家平台 API 端点"""

from typing import Optional, Dict, Any


class AutohomeAPI:
    """
    汽车之家平台 API 集合

    包含汽车之家作品搜索、文章/视频详情、账号作品列表等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        offset: str = "0",
        page: str = "1",
        source_type: str = "video",
        source: str = "汽车之家关键词搜索作品-SDK",
    ) -> dict:
        """
        汽车之家关键词搜索作品

        :param keyword: 搜索关键词（必填）
        :param offset: 翻页偏移量，从 0 开始，翻页 +10
        :param page: 页码，从 1 开始，翻页 +1
        :param source_type: 内容类型：club / article / video
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "offset": str(offset),
            "page": str(page),
            "sourceType": source_type,
        }
        return self._client.post("/story/api/autohome/searchWork", data=data, source=source)

    def get_article(self, work_id: str, page: int = 0, source: str = "获取汽车之家文章详情-SDK") -> dict:
        """
        汽车之家文章详情（车家号）

        :param work_id: 作品 ID（必填）
        :param page: 页码，默认 0
        :return: 文章详情字典
        """
        return self._client.post(
            "/story/api/autohome/articleDetail",
            data={"workId": work_id, "page": page},
            source=source,
        )

    def get_video(self, video_id: str, video_type: int, source: str = "获取汽车之家视频详情-SDK") -> dict:
        """
        汽车之家视频详情（原创账号+车家号）

        :param video_id: 视频 ID（必填）
        :param video_type: 视频类型：0=原创账号，4=车家号（必填）
        :return: 视频详情字典
        """
        return self._client.post(
            "/story/api/autohome/videoDetail",
            data={"videoId": video_id, "videoType": video_type},
            source=source,
        )

    def get_user_works(self, author_id: str, page: int = 0, source: str = "获取汽车之家作者作品列表-SDK") -> dict:
        """
        汽车之家作品列表（原创账号）

        :param author_id: 作者 ID（必填）
        :param page: 页码，默认 0
        :return: 作品列表字典
        """
        return self._client.post(
            "/story/api/autohome/workList",
            data={"authorId": author_id, "page": page},
            source=source,
        )
