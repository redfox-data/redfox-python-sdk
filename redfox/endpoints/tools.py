"""通用工具 API 端点（短视频下载 / 文件上传）"""

from typing import Optional, Dict, Any


class ToolsAPI:
    """
    通用工具 API 集合

    包含多平台短视频下载（去水印）和素材文件上传接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 短视频下载（去水印） ─────────────────────────────────

    def download(self, url: str) -> dict:
        """
        短视频下载器（通用）

        :param url: 视频链接地址（必填）
        :return: 解析结果字典，包含下载链接等信息
        """
        return self._client.post("/story/api/parseWork/parse", data={"url": url})

    def download_douyin(self, url: str) -> dict:
        """
        抖音视频下载（去水印）

        :param url: 视频链接（必填），支持口令分享文本
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/douyin", data={"url": url}
        )

    def download_kuaishou(self, url: str) -> dict:
        """
        快手视频下载（去水印）

        :param url: 视频链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/kuaishou", data={"url": url}
        )

    def download_xiaohongshu(self, url: str) -> dict:
        """
        小红书视频下载（去水印）

        :param url: 笔记链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/xhs", data={"url": url}
        )

    def download_bilibili(self, url: str) -> dict:
        """
        哔哩哔哩视频下载（去水印）

        :param url: 视频链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/bilibili", data={"url": url}
        )

    def download_wechat_channels(self, url: str) -> dict:
        """
        视频号视频下载（去水印）

        :param url: 视频号链接，如 https://weixin.qq.com/sph/xxx（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/sph", data={"url": url}
        )

    def download_tiktok(self, url: str) -> dict:
        """
        TikTok 视频下载（去水印）

        :param url: 视频链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/tiktok", data={"url": url}
        )

    def download_youtube(self, url: str) -> dict:
        """
        YouTube 视频下载

        :param url: 视频链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/youtube", data={"url": url}
        )

    def download_instagram(self, url: str) -> dict:
        """
        Instagram 视频下载（去水印）

        :param url: 帖子/Reel 链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/instagram", data={"url": url}
        )

    def download_twitter(self, url: str) -> dict:
        """
        X (Twitter) 视频下载（去水印）

        :param url: 推文链接（必填）
        :return: 解析结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoDownload/x", data={"url": url}
        )

    # ─── 素材上传 ───────────────────────────────────────────

    def upload_image(self, file, format: str) -> dict:
        """
        上传图片

        :param file: 图片文件（必填），支持文件路径 / (filename, bytes) 元组 / 文件对象 / bytes
        :param format: 上传图片格式（必填），支持 png、jpeg、webp
        :return: 上传结果字典，包含可访问的图片 URL
        """
        return self._client.upload(
            "/story/api/parseWork/imageGen/uploadImage",
            file=file,
            data={"format": format},
        )

    def upload_file(self, file, format: str) -> dict:
        """
        上传视频/图片/音频素材

        文件大小限制：视频（mp4/avi/mov/mkv/webm）50MB；
        音频（mp3/wav/aac/ogg/flac）20MB；图片（png/jpg/jpeg/webp/gif/bmp）10MB。

        :param file: 素材文件（必填），支持文件路径 / (filename, bytes) 元组 / 文件对象 / bytes
        :param format: 素材格式（必填），用于判断文件大小限制和存储路径，如 "mp4"
        :return: 上传结果字典，包含可访问的文件 URL
        """
        return self._client.upload(
            "/story/api/parseWork/videoGen/uploadFile",
            file=file,
            data={"format": format},
        )
