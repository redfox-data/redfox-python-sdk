"""Gemini 图片生成工具 API 端点（Nano Banana 2.1）"""

from typing import Optional, Dict, Any, List


class GeminiImageAPI:
    """
    Gemini 图片生成工具 API 集合（Nano Banana 2.1）

    支持 1K/2K/4K 分辨率输出。异步执行：submit() 返回 taskId，
    再轮询 result() 取 imageUrls。
    """

    # 服务端支持的输出分辨率档位
    RESOLUTIONS = ("1K", "2K", "4K")

    # 服务端支持的输出宽高比
    SIZES = (
        "1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16",
        "5:4", "4:5", "21:9", "1:4", "4:1", "1:8", "8:1",
    )

    # result() 的 status 取值，仅后两者为终态
    TERMINAL_STATUSES = ("completed", "failed")

    def __init__(self, client):
        self._client = client

    def submit(
        self,
        prompt: str,
        size: str = "16:9",
        resolution: str = "2K",
        image_urls: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source: str = "Gemini Nano Banana 2.1 图片生成-SDK",
    ) -> dict:
        """
        提交 Gemini Nano Banana 2.1 图片生成任务

        :param prompt: 图片生成提示词（必填）
        :param size: 输出图像宽高比，支持 1:1、3:2、2:3、4:3、3:4、16:9、9:16、
                     5:4、4:5、21:9、1:4、4:1、1:8、8:1
        :param resolution: 输出图像分辨率，支持 1K/2K/4K（大写 K）
        :param image_urls: 参考图片 URL 列表，用于图生图场景，不传则为纯文生图
        :param metadata: 附加元数据，如 {"retouchTool": "crop"}（可选）
        :return: 包含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "size": size,
            "resolution": resolution,
        }
        if image_urls:
            data["imageUrls"] = image_urls
        if metadata is not None:
            data["metadata"] = metadata
        return self._client.post(
            "/story/api/parseWork/imageGen/geminiBanana21Submit", data=data, source=source
        )

    def result(self, task_id: str, source: str = "查询 Gemini 图片生成任务结果-SDK") -> dict:
        """
        查询 Gemini Nano Banana 2.1 图片生成结果

        :param task_id: 任务 ID（由 submit 接口返回）
        :return: 任务结果字典，包含 status/progress/imageUrls/failReason 等。
                 status 取值 queued/in_progress/completed/failed，仅后两者为终态
        """
        return self._client.post(
            "/story/api/parseWork/imageGen/geminiBanana21Result",
            data={"taskId": task_id},
            source=source,
        )
