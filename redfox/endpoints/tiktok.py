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
        offset: str = "0",
        count: str = "20",
        follower_count_filter: int = None,
        profile_type_filter: int = None,
        other_pref_filter: int = None,
        source: str = "搜索 TikTok 账号-SDK",
    ) -> dict:
        """
        TikTok 关键词搜索账号

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量，从 0 开始，翻页 +count
        :param count: 每页数量，默认 20
        :param follower_count_filter: 粉丝数筛选：1=0~1K，2=1K~10K，3=10K~100K，4=100K 以上，不传不限制
        :param profile_type_filter: 账号类型筛选：1=认证用户，不传不限制
        :param other_pref_filter: 其他偏好：1=按用户名相关性，不传不限制
        :return: 搜索结果字典，包含 cursor/hasMore/userList
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "offset": offset,
            "count": count,
        }
        if follower_count_filter is not None:
            data["followerCountFilter"] = follower_count_filter
        if profile_type_filter is not None:
            data["profileTypeFilter"] = profile_type_filter
        if other_pref_filter is not None:
            data["otherPrefFilter"] = other_pref_filter
        return self._client.post(
            "/story/api/tiktok/ability/searchUser", data=data, source=source
        )

    def search_videos(
        self,
        keyword: str,
        offset: str = "0",
        count: str = "20",
        sort_type: str = "0",
        publish_time: str = "0",
        region: str = "US",
        source: str = "TikTok 关键词视频搜索-SDK",
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
            source=source,
        )

    def get_work(self, aweme_id: str, source: str = "获取 TikTok 单个作品数据-SDK") -> dict:
        """
        获取 TikTok 单个作品数据

        :param aweme_id: 作品 ID（aweme_id，必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/tiktok/ability/awemeDetail", data={"awemeId": aweme_id}, source=source
        )

    def get_user_works(self, sec_user_id: str, source: str = "获取 TikTok 用户主页作品数据-SDK") -> dict:
        """
        获取 TikTok 用户主页作品数据

        :param sec_user_id: 用户 ID（sec_user_id，必填）
        :return: 用户主页作品字典
        """
        return self._client.post(
            "/story/api/tiktok/ability/userAwemeList",
            data={"secUserId": sec_user_id},
            source=source,
        )
