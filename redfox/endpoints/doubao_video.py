"""豆包视频生成工具 API 端点"""

from typing import Optional, Dict, Any


class DoubaoVideoAPI:
    """
    豆包视频生成工具 API 集合

    基于 Seedance 2.0 模型，支持文生视频。
    """

    def __init__(self, client):
        self._client = client

    def submit(
        self,
        prompt: str,
        model: str = "doubao-seedance-2-0-250528",
        resolution: str = "720p",
        ratio: str = "16:9",
        duration: int = 5,
        seed: int = None,
        generate_audio: bool = True,
    ) -> dict:
        """
        提交 Seedance 2.0 视频生成任务

        :param prompt: 视频生成提示词（必填）
        :param model: 模型名称
        :param resolution: 分辨率，如 720p
        :param ratio: 宽高比，如 16:9
        :param duration: 时长（秒），如 5
        :param seed: 随机种子
        :param generate_audio: 是否生成音频
        :return: 包含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "model": model,
            "resolution": resolution,
            "ratio": ratio,
            "duration": duration,
            "generateAudio": generate_audio,
        }
        if seed is not None:
            data["seed"] = seed
        return self._client.post("/story/api/parseWork/videoGen/submit", data=data)

    def result(self, task_id: str) -> dict:
        """
        查询 Seedance 2.0 视频生成任务结果

        :param task_id: 任务 ID（由 submit 接口返回）
        :return: 任务结果字典，包含 status/videoUrl/failReason 等
        """
        return self._client.post(
            "/story/api/parseWork/videoGen/result", data={"taskId": task_id}
        )
