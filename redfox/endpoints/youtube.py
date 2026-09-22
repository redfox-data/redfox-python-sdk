"""YouTube 平台 API 端点"""

from typing import Optional, Dict, Any


class YouTubeAPI:
    """
    YouTube 平台 API 集合

    包含视频搜索、视频详情、视频评论、视频提文案等接口。
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
        format: str = None,
        include_timestamp: bool = None,
        send_metadata: bool = None,
        language: str = None,
        source: str = "提取 YouTube 视频字幕/文案-SDK",
    ) -> dict:
        """
        YouTube 视频提文案（提取字幕/口播文案）

        :param video_url: YouTube 视频 URL 或视频 ID（必填），
            支持完整 URL、短 URL（youtu.be）或仅视频 ID
        :param format: 输出格式：json 或 text，默认 json
        :param include_timestamp: 是否包含时间戳，默认 True
        :param send_metadata: 是否包含视频元数据，默认 False
        :param language: 语言优先级列表，逗号分隔的语言代码，如 "zh,en,asr"
        :return: 文案提取结果字典
        """
        data: Dict[str, Any] = {"videoUrl": video_url}
        if format is not None:
            data["format"] = format
        if include_timestamp is not None:
            data["includeTimestamp"] = include_timestamp
        if send_metadata is not None:
            data["sendMetadata"] = send_metadata
        if language is not None:
            data["language"] = language
        return self._client.post("/story/api/youtube/transcript", data=data, source=source)
