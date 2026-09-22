"""Instagram 平台 API 端点"""

from typing import Optional, Dict, Any


class InstagramAPI:
    """
    Instagram 平台 API 集合

    包含综合搜索、帖子详情、帖子评论、用户信息等接口。
    """

    def __init__(self, client):
        self._client = client

    def search(
        self,
        keyword: str,
        pagination_token: str = None,
        source: str = "Instagram 关键词搜索-SDK",
    ) -> dict:
        """
        Instagram 综合搜索

        :param keyword: 搜索关键词（必填）
        :param pagination_token: 分页 token，从上一次响应获取，用于翻页
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if pagination_token is not None:
            data["paginationToken"] = pagination_token
        return self._client.post("/story/api/ins/search", data=data, source=source)

    def get_post(self, code_or_url: str, source: str = "获取 Instagram 单个帖子详情-SDK") -> dict:
        """
        获取 Instagram 帖子详情

        :param code_or_url: 帖子 Shortcode 或完整 URL（必填），
            如 "DRhvwVLAHAG" 或 "https://www.instagram.com/reel/DPi5REKCali/"
        :return: 帖子详情字典
        """
        return self._client.post(
            "/story/api/ins/postDetail", data={"codeOrUrl": code_or_url}, source=source
        )

    def get_comments(
        self,
        code_or_url: str,
        sort_by: str = "recent",
        pagination_token: str = None,
        source: str = "获取 Instagram 帖子评论-SDK",
    ) -> dict:
        """
        获取 Instagram 帖子评论

        :param code_or_url: 帖子 Shortcode 或完整 URL（必填）
        :param sort_by: 排序方式："recent" 最新（默认）/ "popular" 热门
        :param pagination_token: 分页 token，从上一次响应获取，用于翻页
        :return: 评论列表字典
        """
        data: Dict[str, Any] = {"codeOrUrl": code_or_url, "sortBy": sort_by}
        if pagination_token is not None:
            data["paginationToken"] = pagination_token
        return self._client.post("/story/api/ins/postComment", data=data, source=source)

    def get_user(
        self,
        username: str = None,
        user_id: str = None,
        source: str = "获取 Instagram 用户信息-SDK",
    ) -> dict:
        """
        获取 Instagram 用户信息

        username 和 user_id 至少传一个，同时传入时优先使用 user_id。

        :param username: 用户名
        :param user_id: 用户 ID，如 "18527"
        :return: 用户信息字典
        """
        data: Dict[str, Any] = {}
        if username is not None:
            data["username"] = username
        if user_id is not None:
            data["userId"] = user_id
        return self._client.post("/story/api/ins/userInfo", data=data, source=source)
