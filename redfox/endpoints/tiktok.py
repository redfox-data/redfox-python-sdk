"""TikTok 平台 API 端点"""

from typing import Optional, Dict, Any


class TikTokAPI:
    """
    TikTok 平台 API 集合

    包含 TikTok 账号搜索等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_users(
        self,
        keyword: str,
        cursor: int = 0,
        rid: str = None,
    ) -> dict:
        """
        TikTok 关键词搜索账号

        :param keyword: 搜索关键词（必填）
        :param cursor: 翻页游标，第一页为 0，每页 +10
        :param rid: 数据返回的 rid，翻页时传入，第一页传空
        :return: 搜索结果字典，包含 cursor/hasMore/userList
        """
        data: Dict[str, Any] = {"keyword": keyword, "cursor": cursor}
        if rid is not None:
            data["rid"] = rid
        return self._client.post("/story/api/deepSearch/tk/searchUser", data=data)

    def search_videos(
        self,
        keyword: str,
        offset: str = "0",
        count: str = "20",
        sort_type: str = "0",
        publish_time: str = "0",
        region: str = "US",
    ) -> dict:
        """
        TikTok 关键词视频搜索

        :param keyword: 搜索关键词
        :param offset: 偏移量，示例 "0"
        :param count: 数量，示例 "20"
        :param sort_type: 排序方式：0=相关度，1=最多点赞
        :param publish_time: 发布时间：0=不限制，1=最近一天，7=最近一周，30=最近一个月，90=最近三个月，180=最近半年
        :param region: 地区，默认 US（美国），可选值参考 ISO 3166-1 alpha-2 国家代码
        :return: 搜索结果字典
        """
        return self._client.post(
            "/story/api/tiktok/ability/searchVideo",
            data={
                "keyword": keyword,
                "offset": offset,
                "count": count,
                "sortType": sort_type,
                "publishTime": publish_time,
                "region": region,
            },
        )

    def get_work(self, aweme_id: str) -> dict:
        """
        获取 TikTok 单个作品数据

        :param aweme_id: 作品 ID（aweme_id，必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/tiktok/ability/awemeDetail", data={"awemeId": aweme_id}
        )

    def get_user_works(self, sec_user_id: str) -> dict:
        """
        获取 TikTok 用户主页作品数据

        :param sec_user_id: 用户 ID（sec_user_id，必填）
        :return: 用户主页作品字典
        """
        return self._client.post(
            "/story/api/tiktok/ability/userAwemeList",
            data={"secUserId": sec_user_id},
        )
