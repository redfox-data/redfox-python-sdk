"""知乎平台 API 端点"""

from typing import Optional, Dict, Any


class ZhihuAPI:
    """
    知乎平台 API 集合

    包含知乎关键词搜索作品、文章详情、评论详情、账号详情、搜索热点等接口。
    """

    def __init__(self, client):
        self._client = client

    def get_account(self, user_id: str, source: str = "知乎账号详情-SDK") -> dict:
        """
        知乎账号详情

        :param user_id: 用户 ID，从知乎主页链接中获取，如 he-jia-lei-80（必填）
        :return: 账号详情字典，包含 nickname/fansNum/headline/ipLocation 等
        """
        return self._client.post(
            "/story/api/zhihu/ability/accountDetail",
            data={"userId": user_id},
            source=source,
        )

    def get_article(self, article_id: str, source: str = "知乎文章详情-SDK") -> dict:
        """
        知乎文章详情

        :param article_id: 文章 ID（必填），如 2074146944805500249
        :return: 文章详情字典，包含 content/likedNum/commentNum/opusUrl 等
        """
        return self._client.post(
            "/story/api/zhihu/ability/articleDetail",
            data={"articleId": article_id},
            source=source,
        )

    def get_article_comments(
        self,
        article_id: str,
        next_url: str = None,
        source: str = "知乎评论详情-SDK",
    ) -> dict:
        """
        知乎评论详情

        :param article_id: 文章 ID（必填）
        :param next_url: 翻页地址，传上一页响应中的 nextUrl；为空表示第一页
        :return: 评论列表字典，包含 items/nextUrl
        """
        data: Dict[str, Any] = {"articleId": article_id}
        if next_url is not None:
            data["nextUrl"] = next_url
        return self._client.post(
            "/story/api/zhihu/ability/articleComment", data=data, source=source
        )

    def get_hot_search(self, source: str = "知乎搜索热点-SDK") -> dict:
        """
        获取知乎搜索热点

        :return: 热点列表字典，包含 title/hotValue/label/rank
        """
        return self._client.post(
            "/story/api/zhihu/ability/hotSearch", data={}, source=source
        )

    def search_works(
        self,
        keyword: str,
        offset: str = "0",
        sort: str = None,
        time_interval: str = None,
        vertical: str = None,
        source: str = "知乎关键词搜索作品-SDK",
    ) -> dict:
        """
        知乎关键词搜索作品

        :param keyword: 关键词（必填）
        :param offset: 翻页偏移量，+20 递增，第一页为 "0"
        :param sort: 排序：upvoted_count 最多点赞；created_time 最新发布
        :param time_interval: 时间范围：a_day 一天内；a_week 一周内；a_month 一个月内；
            three_months 3 个月内；half_a_year 半年内；a_year 一年内
        :param vertical: 类型：answer 回答；article 文章；zvide 视频
        :return: 作品列表
        """
        data: Dict[str, Any] = {"keyword": keyword, "offset": str(offset)}
        if sort is not None:
            data["sort"] = sort
        if time_interval is not None:
            data["timeInterval"] = time_interval
        if vertical is not None:
            data["vertical"] = vertical
        return self._client.post(
            "/story/api/zhihu/ability/searchWork", data=data, source=source
        )
