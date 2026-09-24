"""百家号平台 API 端点"""

from typing import Optional, Dict, Any


class BaijiahaoAPI:
    """
    百家号平台 API 集合

    包含百家号账号关键词搜索、关键词搜索作品、视频详情、作品内容 html、账号信息等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_users(self, keyword: str, page: str = "0", source: str = "百家号账号关键词搜索-SDK") -> dict:
        """
        百家号账号关键词搜索

        :param keyword: 搜索关键词（必填）
        :param page: 页码，第一页传 "0"，下一页传返回数据中的 page 值
        :return: 账号列表字典
        """
        return self._client.post(
            "/story/api/bjh/ability/accountSearch",
            data={"keyword": keyword, "page": str(page)},
            source=source,
        )

    def search_works(
        self,
        keyword: str,
        pn: str = "0",
        sort: str = None,
        source: str = "百家号关键词搜索作品-SDK",
    ) -> dict:
        """
        百家号关键词搜索作品

        :param keyword: 关键词（必填）
        :param pn: 翻页，第一页传 "0"，翻页 +10
        :param sort: 排序："1"=焦点排序（默认），"2"=时间排序
        :return: 作品列表
        """
        data: Dict[str, Any] = {"keyWord": keyword, "pn": str(pn)}
        if sort is not None:
            data["sort"] = sort
        return self._client.post(
            "/story/api/bjh/ability/searchWork", data=data, source=source
        )

    def get_video(self, sv_id: str, source: str = "获取百家号视频详情-SDK") -> dict:
        """
        百家号视频详情

        :param sv_id: 视频 ID（必填）
        :return: 视频详情字典
        """
        return self._client.post(
            "/story/api/bjh/ability/videoDetail",
            data={"svId": sv_id},
            source=source,
        )

    def get_article_html(self, article_id: str, source: str = "获取百家号作品内容 html-SDK") -> dict:
        """
        百家号作品内容 html

        :param article_id: 文章 ID（必填）
        :return: 文章 HTML 内容字典（含 content / clearContent / imageList 等）
        """
        return self._client.post(
            "/story/api/bjh/ability/opusHtml",
            data={"articleId": article_id},
            source=source,
        )

    def get_user(self, uk: str, source: str = "获取百家号账号信息-SDK") -> dict:
        """
        百家号账号信息

        :param uk: 账号 uk（必填）
        :return: 账号信息字典
        """
        return self._client.post(
            "/story/api/bjh/ability/accountDetail",
            data={"uk": uk},
            source=source,
        )
