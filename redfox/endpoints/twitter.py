"""X (Twitter) 平台 API 端点"""

from typing import Optional, Dict, Any


class TwitterAPI:
    """
    X (Twitter) 平台 API 集合

    包含推文搜索、推文详情、用户信息、评论、关注列表、用户发帖、热门账号榜等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_tweets(
        self,
        keyword: str,
        search_type: str = None,
        cursor: str = None,
        source: str = "X(Twitter) 关键词搜索推文-SDK",
    ) -> dict:
        """
        搜索推文

        :param keyword: 搜索关键字（必填）
        :param search_type: 搜索类型，默认 Top，可选：Top / Latest / Media / People / Lists
        :param cursor: 分页游标，首次不传，后续从上一次返回结果中获取
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if search_type is not None:
            data["searchType"] = search_type
        if cursor is not None:
            data["cursor"] = cursor
        return self._client.post("/story/api/x/search", data=data, source=source)

    def get_tweet(self, tweet_id: str, source: str = "获取 X(Twitter) 单条推文详情-SDK") -> dict:
        """
        获取单个推文详情

        :param tweet_id: 推文 ID（必填）
        :return: 推文详情字典
        """
        return self._client.post(
            "/story/api/x/tweetDetail", data={"tweetId": tweet_id}, source=source
        )

    def get_user(
        self,
        screen_name: str = None,
        rest_id: str = None,
        source: str = "获取 X(Twitter) 用户信息-SDK",
    ) -> dict:
        """
        获取 X 用户信息

        screen_name 和 rest_id 至少传一个，同时传入时优先使用 rest_id。

        :param screen_name: 用户名，如 "maurodm600"
        :param rest_id: 用户 ID，如 "110766540"
        :return: 用户信息字典
        """
        data: Dict[str, Any] = {}
        if screen_name is not None:
            data["screenName"] = screen_name
        if rest_id is not None:
            data["restId"] = rest_id
        return self._client.post("/story/api/x/userInfo", data=data, source=source)

    def get_comments(
        self,
        tweet_id: str,
        cursor: str = None,
        source: str = "获取 X(Twitter) 推文评论/回复-SDK",
    ) -> dict:
        """
        获取推文评论

        :param tweet_id: 推文 ID（必填）
        :param cursor: 翻页游标，首次不传，后续从上一次请求的返回结果中获取
        :return: 评论列表字典
        """
        data: Dict[str, Any] = {"tweetId": tweet_id}
        if cursor is not None:
            data["cursor"] = cursor
        return self._client.post("/story/api/x/tweetComments", data=data, source=source)

    def get_following(
        self,
        screen_name: str,
        cursor: str = None,
        source: str = "获取 X(Twitter) 用户关注列表-SDK",
    ) -> dict:
        """
        获取用户关注列表

        :param screen_name: 用户名，如 "elonmusk"（必填）
        :param cursor: 翻页游标，首次不传，后续从上一次返回结果中获取
        :return: 关注列表字典
        """
        data: Dict[str, Any] = {"screenName": screen_name}
        if cursor is not None:
            data["cursor"] = cursor
        return self._client.post("/story/api/x/userFollowing", data=data, source=source)

    def get_user_works(
        self,
        screen_name: str = None,
        rest_id: str = None,
        cursor: str = None,
        source: str = "获取 X(Twitter) 用户发帖-SDK",
    ) -> dict:
        """
        获取用户发帖（时间线）

        screen_name 和 rest_id 至少传一个，同时传入时优先使用 rest_id。

        :param screen_name: 用户名，如 "elonmusk"
        :param rest_id: 用户 ID
        :param cursor: 翻页游标，首次不传，后续从上一次返回结果中获取
        :return: 用户发帖列表字典
        """
        data: Dict[str, Any] = {}
        if screen_name is not None:
            data["screenName"] = screen_name
        if rest_id is not None:
            data["restId"] = rest_id
        if cursor is not None:
            data["cursor"] = cursor
        return self._client.post("/story/api/x/userTimeline", data=data, source=source)

    def get_hot_account_rank(
        self,
        rank_date: str,
        page_num: int = 1,
        gender: str = "all",
        category: str = None,
        source: str = "X 热门账号榜-SDK",
    ) -> dict:
        """
        X 热门账号榜

        每页固定 20 条，最多 200 条。

        :param rank_date: 榜单日期，格式 "YYYY-MM-DD"（必填）
        :param page_num: 页码，从 1 开始
        :param gender: 性别筛选：all 全部（默认）/ male 男 / female 女，也支持中文 全部/男/女
        :param category: 行业分类，如 "科技软件"、"市场营销"、"政治新闻" 等
        :return: 榜单字典
        """
        data: Dict[str, Any] = {"rankDate": rank_date, "pageNum": page_num, "gender": gender}
        if category is not None:
            data["category"] = category
        return self._client.post("/story/api/x/hotAccount/rankList", data=data, source=source)
