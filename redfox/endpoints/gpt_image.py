"""GPT 图片生成工具 API 端点"""

from typing import Optional, Dict, Any, List


class GPTImageAPI:
    """
    GPT 图片生成工具 API 集合

    基于 gpt-image-2 模型，支持文生图和参考图生图（最多 2 张参考图）。
    异步执行：submit() 返回 taskId，再轮询 result() 取 imageUrls。

    注意：result() 返回的图片 URL 有效期仅数分钟，过期后访问返回 404，
    需立即下载保存；用平台生成图做参考图时也必须在其失效前提交。
    """

    # 服务端支持的输出分辨率档位
    RESOLUTIONS = ("1k", "2k", "4k")

    # 服务端支持的输出宽高比
    SIZES = (
        "1:1", "3:2", "2:3", "4:3", "3:4", "5:4", "4:5",
        "16:9", "9:16", "2:1", "1:2", "21:9", "9:21",
    )

    # result() 的 status 取值，仅后两者为终态
    TERMINAL_STATUSES = ("completed", "failed")

    def __init__(self, client):
        self._client = client

    def submit(
        self,
        prompt: str,
        resolution: str = "1k",
        size: str = "1:1",
        n: int = 1,
        reference_images: Optional[List[str]] = None,
    ) -> dict:
        """
        提交 GPT-Image-2 图片生成任务

        :param prompt: 图片生成提示词，描述期望的生成效果（必填）
        :param resolution: 输出分辨率档位，支持 1k/2k/4k
        :param size: 输出图片宽高比，支持 1:1、3:2、2:3、4:3、3:4、5:4、4:5、
                     16:9、9:16、2:1、1:2、21:9、9:21
        :param n: 生成图片数量，最大 4（超限服务端报 1002）
        :param reference_images: 参考图片 URL 列表，最多 2 张，用于图生图场景；
                                 不传则为纯文生图。URL 必须公网可访问且未过期，
                                 否则任务会以 failed 结束
        :return: 包含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "resolution": resolution,
            "size": size,
            "n": n,
        }
        if reference_images:
            data["referenceImages"] = reference_images
        return self._client.post(
            "/story/api/parseWork/imageGen/gptImage2Submit", data=data
        )

    def result(self, task_id: str) -> dict:
        """
        查询 GPT-Image-2 图片生成任务结果

        :param task_id: 任务 ID（由 submit 接口返回）
        :return: 任务结果字典，包含 status/progress/imageUrls/failReason/
                 model/resolution/size。status 取值 queued/in_progress/completed/
                 failed，仅 completed 与 failed 为终态；imageUrls 数量与 n 一致，
                 但有效期仅数分钟，需立即下载保存
        """
        return self._client.post(
            "/story/api/parseWork/imageGen/gptImage2Result", data={"taskId": task_id}
        )
