"""YouTube 平台 API 端点"""

from typing import Optional, Dict, Any


class YouTubeAPI:
    """
    YouTube 平台 API 集合

    包含视频搜索、视频详情、视频评论、视频提文案、字幕详情等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_videos(
        self,
        search_query: str,
        continuation_token: str = None,
        source: str = "YouTube 关键词视频搜索-SDK",
    ) -> dict:
        """
        搜索 YouTube 视频

        :param search_query: 搜索关键词（必填）
        :param continuation_token: 翻页游标（传入上次响应的 continuationToken 获取下一页）
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"searchQuery": search_query}
        if continuation_token is not None:
            data["continuationToken"] = continuation_token
        return self._client.post("/story/api/youtube/searchVideo", data=data, source=source)

    def get_video(self, video_id: str, source: str = "获取 YouTube 单个视频详情-SDK") -> dict:
        """
        获取 YouTube 视频详情

        :param video_id: 视频 ID，如 "sa8AzBK4dao"（必填）
        :return: 视频详情字典
        """
        return self._client.post(
            "/story/api/youtube/videoDetail", data={"videoId": video_id}, source=source
        )

    def get_comments(
        self,
        video_id: str,
        language_code: str = None,
        country_code: str = None,
        sort_by: str = None,
        continuation_token: str = None,
        source: str = "获取 YouTube 视频评论-SDK",
    ) -> dict:
        """
        获取 YouTube 视频评论

        :param video_id: 视频 ID（必填）
        :param language_code: 评论显示语言偏好，默认 "zh-CN"，可选 "en-US"、"ja-JP"、"ko-KR" 等
        :param country_code: 地区代码，默认 "US"，可选 "JP"、"GB" 等
        :param sort_by: 排序方式："top" 热门评论（默认）/ "newest" 最新评论
        :param continuation_token: 翻页令牌，从上一次响应中获取，首次请求不传
        :return: 评论列表字典
        """
        data: Dict[str, Any] = {"videoId": video_id}
        if language_code is not None:
            data["languageCode"] = language_code
        if country_code is not None:
            data["countryCode"] = country_code
        if sort_by is not None:
            data["sortBy"] = sort_by
        if continuation_token is not None:
            data["continuationToken"] = continuation_token
        return self._client.post("/story/api/youtube/videoComments", data=data, source=source)

    def get_transcript(
        self,
        video_url: str,
        source: str = "提取 YouTube 视频字幕/文案-SDK",
    ) -> dict:
        """
        YouTube 视频字幕提取

        返回视频信息（标题、时长、发布时间、封面、描述）及各语言、
        各格式（srt/vtt/ttml/json3）的字幕下载地址，含人工字幕与自动生成字幕。

        :param video_url: YouTube 视频链接（必填），
            如 "https://www.youtube.com/watch?v=jNQXAC9IVRw"
        :return: 字幕提取结果字典，包含 subtitles 字幕轨道列表
        """
        return self._client.post(
            "/story/api/parseWork/videoSubtitle/youtube",
            data={"url": video_url},
            source=source,
        )

    def get_info(self, video_url: str, source: str = "获取 YouTube 视频字幕详情-SDK") -> dict:
        """
        获取 YouTube 视频字幕详情（视频信息 + 可用字幕语言列表）

        :param video_url: YouTube 视频 URL 或视频 ID（必填）
        :return: 视频字幕详情字典
        """
        return self._client.post(
            "/story/api/youtube/info", data={"videoUrl": video_url}, source=source
        )
