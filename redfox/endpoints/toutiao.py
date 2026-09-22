"""今日头条平台 API 端点"""

from typing import Optional, Dict, Any


class ToutiaoAPI:
    """
    今日头条平台 API 集合

    包含今日头条作品搜索、作品详情等接口（实时）。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        offset: int = 0,
        source: str = "搜索今日头条内容-SDK",
    ) -> dict:
        """
        获取今日头条账号作品列表（实时）

        :param keyword: 搜索关键词（必填）
        :param offset: 翻页偏移量，从 0 开始，每页 +1
        :return: 作品列表
        """
        data: Dict[str, Any] = {"keyword": keyword, "offset": str(offset)}
        return self._client.post("/story/api/toutiao/searchWork", data=data, source=source)

    def get_work(self, opus_id: str, source: str = "获取今日头条作品详情-SDK") -> dict:
        """
        获取今日头条作品内容详情（实时）

        :param opus_id: 作品 ID（必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/toutiao/workDetail", data={"opusId": opus_id}, source=source
        )

    def get_comments(self, opus_id: str, offset: str = None, source: str = "获取今日头条作品评论-SDK") -> dict:
        """
        获取今日头条作品评论（实时）

        :param opus_id: 作品 ID（必填）
        :param offset: 翻页偏移量
        :return: 评论列表字典
        """
        data: Dict[str, Any] = {"opusId": opus_id}
        if offset is not None:
            data["offset"] = offset
        return self._client.post("/story/api/toutiao/workComment", data=data, source=source)

    def search_users(
        self,
        name: str,
        offset: str = None,
        search_id: str = None,
        source: str = "今日头条关键词搜索账号-SDK",
    ) -> dict:
        """
        获取今日头条关键词搜索账号（实时）

        :param name: 搜索关键词（必填）
        :param offset: 翻页偏移量，hasMore 为 1 时使用返回的 offset
        :param search_id: 搜索 ID，hasMore 为 1 时使用返回的 searchId
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"name": name}
        if offset is not None:
            data["offset"] = offset
        if search_id is not None:
            data["searchId"] = search_id
        return self._client.post("/story/api/toutiao/searchAccount", data=data, source=source)

    def get_user_works(self, category: str, token: str, source: str = "获取今日头条账号作品列表-SDK") -> dict:
        """
        获取今日头条账号作品列表（实时）

        :param category: 内容分类（必填）：profile_all 全部；pc_profile_article 文章；
            pc_profile_video 视频；pc_profile_ugc 微头条；profile_wenda 问答；pc_profile_short_video 小视频
        :param token: web 端 uid（必填）
        :return: 作品列表字典
        """
        return self._client.post(
            "/story/api/toutiao/userWorkList",
            data={"category": category, "token": token},
            source=source,
        )
