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
            "/story/api/parseWork/videoGen/submit", data=data
        )

    def result(self, task_id: str) -> dict:
        """
        查询视频生成任务结果

        :param task_id: 任务 ID（submit 接口返回）
        :return: 视频生成结果字典
        """
        return self._client.post(
            "/story/api/parseWork/videoGen/result",
            data={"taskId": task_id},
        )
