"""Facebook 平台 API 端点"""

from typing import Optional, Dict, Any


class FacebookAPI:
    """
    Facebook 平台 API 集合

    包含 Facebook 主页信息、主页帖子列表、帖子详情、帖子评论等接口。
    """

    def __init__(self, client):
        self._client = client

    def get_user(self, url: str, source: str = "Facebook获取主页信息-SDK") -> dict:
        """
        Facebook获取主页信息

        :param url: Facebook 主页 URL（必填），如 https://www.facebook.com/Meta
        :return: 主页详细信息字典，包含分类、粉丝数、简介等
        """
        return self._client.post("/story/api/fb/userInfo", data={"url": url}, source=source)

    def get_user_posts(
        self,
        url: str = None,
        page_id: str = None,
        cursor: str = None,
        source: str = "Facebook获取主页帖子列表-SDK",
    ) -> dict:
        """
        Facebook获取主页帖子列表

        url 和 page_id 至少传一个，传 page_id 查询更快。

        :param url: Facebook 主页 URL
        :param page_id: Facebook 主页 ID（由 get_user 接口返回）
        :param cursor: 分页 cursor，传上一页响应中的 paginationToken 翻页
        :return: 帖子列表字典，包含 items/paginationToken
        """
        data: Dict[str, Any] = {}
        if url:
            data["url"] = url
        if page_id:
            data["pageId"] = page_id
        if cursor:
            data["cursor"] = cursor
        return self._client.post("/story/api/fb/userPosts", data=data, source=source)

    def get_post(self, url: str, source: str = "Facebook获取帖子详情-SDK") -> dict:
        """
        Facebook获取帖子详情

        :param url: Facebook 帖子 URL（必填），如 https://www.facebook.com/reel/1746412686633900
        :return: 帖子详情字典，包含 reactions 细分、预估触达、互动率等
        """
        return self._client.post("/story/api/fb/postDetail", data={"url": url}, source=source)

    def get_post_comments(
        self,
        url: str = None,
        feedback_id: str = None,
        cursor: str = None,
        source: str = "Facebook获取帖子评论-SDK",
    ) -> dict:
        """
        Facebook获取帖子评论

        url 和 feedback_id 至少传一个，传 feedback_id 查询更快。

        :param url: Facebook 帖子 URL
        :param feedback_id: 评论线程 feedback_id（由 get_post 接口返回）
        :param cursor: 分页 cursor，传上一页响应中的 paginationToken 翻页
        :return: 评论列表字典，包含 comments/paginationToken
        """
        data: Dict[str, Any] = {}
        if url:
            data["url"] = url
        if feedback_id:
            data["feedbackId"] = feedback_id
        if cursor:
            data["cursor"] = cursor
        return self._client.post("/story/api/fb/postComment", data=data, source=source)
