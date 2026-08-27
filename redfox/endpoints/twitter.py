"""X (Twitter) 平台 API 端点"""

from typing import Optional, Dict, Any


class TwitterAPI:
    """
    X (Twitter) 平台 API 集合

    包含推文搜索、推文详情、用户信息、评论等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_tweets(
        self,
        keyword: str,
        search_type: str = None,
        cursor: str = None,
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
        return self._client.post("/story/api/x/search", data=data)

    def get_tweet(self, tweet_id: str) -> dict:
        """
        获取单个推文详情

        :param tweet_id: 推文 ID（必填）
        :return: 推文详情字典
        """
        return self._client.post(
            "/story/api/x/tweetDetail", data={"tweetId": tweet_id}
        )

    def get_user(
        self,
        screen_name: str = None,
        rest_id: str = None,
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
        return self._client.post("/story/api/x/userInfo", data=data)

    def get_comments(
        self,
        tweet_id: str,
        cursor: str = None,
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
        return self._client.post("/story/api/x/tweetComments", data=data)
