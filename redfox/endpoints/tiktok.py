"""TikTok 平台 API 端点"""

from typing import Optional, Dict, Any


class TikTokAPI:
    """
    TikTok 平台 API 集合

    包含 TikTok 账号搜索、视频搜索、作品详情、话题搜索、评论等接口。
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

    def search_topics(
        self, keyword: str, offset: int = 0, source: str = "TikTok 话题搜索-SDK"
    ) -> dict:
        """
        TikTok 指定关键词话题搜索

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量，首次传 0，后续传响应中的 nextCursor
        :return: 话题列表字典，包含 topicList/nextCursor/hasMore
        """
        return self._client.post(
            "/story/api/tiktok/ability/searchTopic",
            data={"keyword": keyword, "offset": offset},
            source=source,
        )

    def get_topic_works(
        self,
        ch_id: int,
        cursor: int = 0,
        region: str = None,
        source: str = "获取 TikTok 话题作品数据-SDK",
    ) -> dict:
        """
        获取 TikTok 指定话题作品数据

        :param ch_id: 话题 ID（必填）
        :param cursor: 翻页游标，第一页传 0
        :param region: 地区，支持 US、GB、FR、JP、VN、SG，默认 US
        :return: 话题作品字典，包含 workList/nextCursor/hasMore
        """
        data: Dict[str, Any] = {"ch_id": ch_id, "cursor": cursor}
        if region is not None:
            data["region"] = region
        return self._client.post(
            "/story/api/tiktok/ability/topicAwemeList", data=data, source=source
        )

    def get_user_liked_works(
        self, sec_user_id: str, max_cursor: int = 0, source: str = "获取 TikTok 用户喜欢作品数据-SDK"
    ) -> dict:
        """
        获取 TikTok 用户喜欢作品数据

        :param sec_user_id: 用户加密 ID（sec_user_id，必填）
        :param max_cursor: 翻页游标，第一页传 0
        :return: 喜欢的作品字典，包含 workList/nextCursor/hasMore
        """
        return self._client.post(
            "/story/api/tiktok/ability/userFavoriteAwemeList",
            data={"sec_user_id": sec_user_id, "max_cursor": max_cursor},
            source=source,
        )

    def get_user_following(
        self,
        user_id: str = None,
        sec_user_id: str = None,
        min_time: str = "0",
        page_token: str = "",
        source: str = "获取 TikTok 用户关注列表-SDK",
    ) -> dict:
        """
        获取 TikTok 指定用户的关注列表数据

        user_id 和 sec_user_id 二选一。

        :param user_id: 纯数字用户 ID
        :param sec_user_id: 字母数字混合 ID
        :param min_time: 翻页参数，首次传 "0"，后续传上次返回的 minTime
        :param page_token: 翻页 token，首次传空字符串，后续传上次返回的 pageToken
        :return: 关注列表字典，包含 followingList/minTime/pageToken
        """
        data: Dict[str, Any] = {"minTime": str(min_time), "pageToken": str(page_token)}
        if user_id:
            data["userId"] = user_id
        if sec_user_id:
            data["secUserId"] = sec_user_id
        return self._client.post(
            "/story/api/tiktok/ability/userFollowing", data=data, source=source
        )

    def get_video_comments(
        self, aweme_id: str, cursor: int = 0, source: str = "获取 TikTok 视频评论数据-SDK"
    ) -> dict:
        """
        获取 TikTok 单个视频评论数据

        :param aweme_id: 作品 ID（必填）
        :param cursor: 翻页游标，第一页传 0
        :return: 评论列表字典，包含 commentList/nextCursor/hasMore
        """
        return self._client.post(
            "/story/api/tiktok/ability/commentList",
            data={"aweme_id": aweme_id, "cursor": cursor},
            source=source,
        )

    def get_comment_replies(
        self,
        item_id: str,
        comment_id: str,
        cursor: int = 0,
        count: int = 10,
        source: str = "获取 TikTok 评论回复数据-SDK",
    ) -> dict:
        """
        获取 TikTok 指定视频的评论回复数据

        :param item_id: 作品 ID（必填）
        :param comment_id: 评论 ID（必填）
        :param cursor: 翻页游标，第一页传 0
        :param count: 每页数量，默认 10
        :return: 评论回复字典，包含 commentList/nextCursor/hasMore
        """
        return self._client.post(
            "/story/api/tiktok/ability/commentReply",
            data={
                "itemId": item_id,
                "commentId": comment_id,
                "cursor": cursor,
                "count": count,
            },
            source=source,
        )
