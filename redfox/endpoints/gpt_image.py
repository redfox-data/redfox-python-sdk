"""GPT 图片生成工具 API 端点"""

from typing import Optional, Dict, Any, List


class GPTImageAPI:
    """
    GPT 图片生成工具 API 集合

    支持文生图和图生图，基于 image2-GPT 模型。
    """

    def __init__(self, client):
        self._client = client

    def submit(
        self,
        prompt: str,
        n: int = 1,
        size: str = "1024x1024",
        quality: str = "medium",
        background: str = "auto",
        output_format: str = "png",
        output_compression: int = None,
        model_name: str = "gpt-image-2",
        operation: str = "generate",
        input_fidelity: str = None,
        images: List[Dict[str, str]] = None,
    ) -> dict:
        """
        提交 GPT 图片生成任务

        :param prompt: 图片生成提示词（必填）
        :param n: 生成数量，1~10
        :param size: 图片尺寸，如 "1024x1024"
        :param quality: 质量，支持 low/medium/high/auto
        :param background: 背景类型，支持 transparent/opaque/auto
        :param output_format: 输出格式，支持 png/jpeg/webp
        :param output_compression: 输出压缩比，0~100
        :param model_name: 模型名称，默认 gpt-image-2
        :param operation: 操作类型，generate（文生图）/ edit（图生图）
        :param input_fidelity: 输入图保真度，编辑模式（operation=edit）支持 high/low
        :param images: 图片编辑输入图列表，operation=edit 时必填
        :return: 包含 taskId 的字典
        """
        parameters: Dict[str, Any] = {
            "modelName": model_name,
            "n": n,
            "size": size,
            "quality": quality,
            "background": background,
            "outputFormat": output_format,
        }
        if output_compression is not None:
            parameters["outputCompression"] = output_compression
        if input_fidelity is not None:
            parameters["inputFidelity"] = input_fidelity

        data: Dict[str, Any] = {
            "prompt": prompt,
            "operation": operation,
            "parameters": parameters,
        }
        if images is not None:
            data["images"] = images
        return self._client.post("/story/api/parseWork/imageGen/submitSkill", data=data)

    def result(self, task_id: str) -> dict:
        """
        查询 GPT 图片生成任务结果

        :param task_id: 任务 ID（由 submit 接口返回）
        :return: 任务结果字典，包含 status/imagePaths/failReason
        """
        return self._client.post(
            "/story/api/parseWork/imageGen/result", data={"taskId": task_id}
        )
