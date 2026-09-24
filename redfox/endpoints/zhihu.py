"""知乎平台 API 端点"""

from typing import Optional, Dict, Any


class ZhihuAPI:
    """
    知乎平台 API 集合

    包含知乎关键词搜索作品接口。
    """

    def __init__(self, client):
        self._client = client

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
        data: Dict[str, Any] = {"keword": keyword, "offset": str(offset)}
        if sort is not None:
            data["sort"] = sort
        if time_interval is not None:
            data["timeInterval"] = time_interval
        if vertical is not None:
            data["vertical"] = vertical
        return self._client.post(
            "/story/api/zhihu/ability/searchWork", data=data, source=source
        )
