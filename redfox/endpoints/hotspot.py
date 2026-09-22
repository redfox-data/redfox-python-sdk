"""多平台热点榜单 API 端点"""

from typing import Optional, Dict, Any, List


class HotspotAPI:
    """
    多平台热点榜单 API 集合

    聚合抖音、快手、微博、B站、知乎、今日头条、百度、小红书等平台的热点数据。

    平台编码：1=快手，2=抖音，5=微博，6=小红书，7=百度，8=B站，9=知乎，10=今日头条
    """

    def __init__(self, client):
        self._client = client

    def get_platform_rank(
        self,
        platform: int,
        start_date: str,
        end_date: str,
        source: str = "各平台热点榜-SDK",
    ) -> dict:
        """
        各平台热点榜

        :param platform: 平台编码（必填）：1=快手 2=抖音 6=小红书 5=微博 7=百度 8=B站 9=知乎 10=今日头条
        :param start_date: 起始日期，格式 yyyy-MM-dd（必填）
        :param end_date: 截止日期，格式 yyyy-MM-dd（必填）
        :return: 热点榜单字典
        """
        return self._client.get(
            "/story/api/hotSpot/getListByPlatform",
            params={
                "platform": platform,
                "startDate": start_date,
                "endDate": end_date,
            },
            source=source,
        )

    def search_by_keywords(
        self,
        keywords: List[str],
        start_date: str,
        end_date: str,
        platforms: List[int] = None,
        source: str = "全网热搜查询-SDK",
    ) -> dict:
        """
        全网热搜查询（关键词）

        :param keywords: 关键词列表（必填），如 ["三星"]
        :param start_date: 开始时间（必填），查询时间范围不能超过 30 天；
            查询当日数据时开始时间传今日、结束时间传明日
        :param end_date: 结束时间（必填）
        :param platforms: 平台编码列表：1=快手 2=抖音 5=微博 7=百度 8=B站 9=知乎 10=今日头条；
            不指定则查询所有平台
        :return: 热搜查询结果字典
        """
        data: Dict[str, Any] = {
            "keywords": keywords,
            "startDate": start_date,
            "endDate": end_date,
        }
        if platforms is not None:
            data["platforms"] = platforms
        return self._client.post(
            "/story/api/hotSpot/getListByPlatformWithKeyword", data=data, source=source
        )

    def get_top10(self, start_date: str, end_date: str, source: str = "全网聚合热点 TOP10 列表-SDK") -> dict:
        """
        全网聚合热点 TOP10 列表

        :param start_date: 开始时间，格式 yyyy-MM-dd HH:mm:ss（必填）
        :param end_date: 结束时间，格式 yyyy-MM-dd HH:mm:ss（必填）
        :return: 聚合热点 TOP10 字典
        """
        return self._client.post(
            "/story/api/hotKeyword/list",
            data={"startDate": start_date, "endDate": end_date},
            source=source,
        )
