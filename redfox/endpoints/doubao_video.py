"""豆包视频生成 API 端点（Seedance 2.0）"""

from typing import Optional, Dict, Any, List


class DoubaoVideoAPI:
    """
    豆包视频生成 API 集合（Seedance 2.0）

    包含视频生成任务提交与结果查询接口。
    """

    def __init__(self, client):
        self._client = client

    def submit(
        self,
        content: List[Dict[str, Any]],
        model: str = None,
        resolution: str = "720p",
        ratio: str = "adaptive",
        duration: int = 5,
        seed: int = -1,
        watermark: bool = False,
        generate_audio: bool = True,
        return_last_frame: bool = False,
        source: str = "豆包 Seedance 2.0 视频生成-SDK",
    ) -> dict:
        """
        提交视频生成任务（Seedance 2.0）

        content 是一个列表，每个元素是一个字典，支持以下 type：
        - text: {"type": "text", "text": "描述文字"}
        - image_url: {"type": "image_url", "imageUrl": "图片URL", "imageRole": "first_frame/reference_image"}
        - video_url: {"type": "video_url", "videoUrl": "视频URL", "videoRole": "reference_video"}
        - audio_url: {"type": "audio_url", "audioUrl": "音频URL", "audioRole": "reference_audio"}

        :param content: 输入内容列表（必填），每项包含 type 及对应字段
        :param model: 模型名称，如 "doubao-seedance-2-0-260128"
        :param resolution: 视频分辨率：480p/720p/1080p（Seedance 2.0 fast 不支持 1080p）
        :param ratio: 宽高比：adaptive/16:9/4:3/1:1/3:4/9:16/21:9
        :param duration: 视频时长（秒），[4,15] 或 -1（智能）
        :param seed: 随机种子，-1 为随机，范围 [-1, 2^32-1]
        :param watermark: 是否添加水印
        :param generate_audio: 是否生成同步音频（仅 Seedance 2.0 系列）
        :param return_last_frame: 是否返回尾帧图像（用于连续视频生成）
        :return: 含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "content": content,
            "resolution": resolution,
            "ratio": ratio,
            "duration": duration,
            "seed": seed,
            "watermark": watermark,
            "generateAudio": generate_audio,
            "returnLastFrame": return_last_frame,
        }
        if model is not None:
            data["model"] = model
        return self._client.post(
            "/story/api/parseWork/videoGen/submit", data=data, source=source
        )

    def result(self, task_id: str, source: str = "查询豆包视频生成任务结果-SDK") -> dict:
        """
        查询视频生成任务结果

        :param task_id: 任务 ID（submit 接口返回）
        :return: 视频生成结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoGen/result",
            data={"taskId": task_id},
            source=source,
        )

    # ─── Seedance 2.0（新端点） ──────────────────────────────

    def seedance_submit(
        self,
        prompt: str,
        aspect_ratio: str = "adaptive",
        duration: int = 5,
        resolution: str = "720p",
        generate_audio: bool = True,
        return_last_frame: bool = False,
        image_with_roles: Optional[List[Dict[str, Any]]] = None,
        source: str = "豆包 Seedance 2.0 视频生成（新端点）-SDK",
    ) -> dict:
        """
        提交 Seedance 2.0 视频生成任务（新端点）

        支持文生视频、首帧/首尾帧图生视频、多模态参考生视频。

        :param prompt: 生成提示词（必填）
        :param aspect_ratio: 视频宽高比：21:9、16:9、4:3、1:1、3:4、9:16、
                             adaptive（由上游根据输入素材自动选择）
        :param duration: 视频时长（秒），取值范围 4-15
        :param resolution: 视频分辨率：480p、720p，默认 720p
        :param generate_audio: 是否自动生成配音/背景音乐
        :param return_last_frame: 是否返回视频最后一帧图片
        :param image_with_roles: 参考图片列表，每项如
            {"url": "图片URL", "role": "first_frame/last_frame/reference_image"}，
            first_frame/last_frame 最多 1 张，reference_image 最多 9 张
        :return: 含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "aspectRatio": aspect_ratio,
            "duration": duration,
            "resolution": resolution,
            "generateAudio": generate_audio,
            "returnLastFrame": return_last_frame,
        }
        if image_with_roles:
            data["imageWithRoles"] = image_with_roles
        return self._client.post(
            "/story/api/parseWork/videoGen/seedanceSubmit", data=data, source=source
        )

    def seedance_result(
        self, task_id: str, source: str = "查询 Seedance 2.0 视频生成结果（新端点）-SDK"
    ) -> dict:
        """
        查询 Seedance 2.0 视频生成结果（新端点）

        :param task_id: 任务 ID（由 seedance_submit 返回）
        :return: 视频生成结果字典，包含 status/progress/videoUrl/failReason 等。
                 status 取值 completed/processing/failed
        """
        return self._client.post(
            "/story/api/parseWork/videoGen/seedanceResult",
            data={"taskId": task_id},
            source=source,
        )
