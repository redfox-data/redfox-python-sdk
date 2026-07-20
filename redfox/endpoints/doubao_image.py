"""豆包图片生成工具 API 端点"""

from typing import Optional, Dict, Any, Union, List


class DoubaoImageAPI:
    """
    豆包图片生成工具 API 集合

    支持 Seedream 5.0 Pro 和 Seedream 5.0 Lite 两个模型。
    """

    def __init__(self, client):
        self._client = client

    # ─── Seedream 5.0 Pro ───────────────────────────────────

    def pro_submit(
        self,
        prompt: str,
        size: str = "2048x2048",
        image: Union[str, List[str]] = None,
        output_format: str = "jpeg",
        response_format: str = "url",
        watermark: bool = True,
        optimize_prompt: bool = False,
        optimize_mode: str = "standard",
    ) -> dict:
        """
        提交 Seedream 5.0 Pro 图片生成任务

        :param prompt: 图片生成提示词（必填）
        :param size: 尺寸，支持 1K/2K 或像素值如 "2048x2048"
        :param image: 图生图输入图片，支持 URL 或 Base64
        :param output_format: 输出格式，png/jpeg
        :param response_format: 返回格式，url/b64_json
        :param watermark: 是否添加 AI 生成水印
        :param optimize_prompt: 是否开启提示词优化
        :param optimize_mode: 优化模式，standard/fast
        :return: 包含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "size": size,
            "outputFormat": output_format,
            "responseFormat": response_format,
            "watermark": watermark,
        }
        if image is not None:
            data["image"] = image
        if optimize_prompt:
            data["optimizePromptOptions"] = {"mode": optimize_mode}
        return self._client.post("/story/api/parseWork/imageGen/arkProSubmit", data=data)

    def pro_result(self, task_id: str) -> dict:
        """
        查询 Seedream 5.0 Pro 任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/parseWork/imageGen/arkProResult", data={"taskId": task_id}
        )

    # ─── Seedream 5.0 Lite ──────────────────────────────────

    def lite_submit(
        self,
        prompt: str,
        size: str = "2048x2048",
        image: Union[str, List[str]] = None,
        output_format: str = "jpeg",
        response_format: str = "url",
        watermark: bool = True,
        sequential: str = "disabled",
        max_images: int = 4,
        optimize_prompt: bool = False,
        optimize_mode: str = "standard",
    ) -> dict:
        """
        提交 Seedream 5.0 Lite 图片生成任务

        :param prompt: 图片生成提示词（必填）
        :param size: 尺寸，支持 2K/3K/4K 或像素值
        :param image: 图生图输入图片
        :param output_format: 输出格式，png/jpeg
        :param response_format: 返回格式，url/b64_json
        :param watermark: 是否添加 AI 生成水印
        :param sequential: 组图控制，auto/disabled
        :param max_images: 组图最大数量，1~10
        :param optimize_prompt: 是否开启提示词优化
        :param optimize_mode: 优化模式，standard/fast
        :return: 包含 taskId 的字典
        """
        data: Dict[str, Any] = {
            "prompt": prompt,
            "size": size,
            "outputFormat": output_format,
            "responseFormat": response_format,
            "watermark": watermark,
            "sequentialImageGeneration": sequential,
        }
        if image is not None:
            data["image"] = image
        if sequential == "auto":
            data["sequentialImageGenerationOptions"] = {"maxImages": max_images}
        if optimize_prompt:
            data["optimizePromptOptions"] = {"mode": optimize_mode}
        return self._client.post("/story/api/parseWork/imageGen/arkSubmit", data=data)

    def lite_result(self, task_id: str) -> dict:
        """
        查询 Seedream 5.0 Lite 任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/parseWork/imageGen/arkResult", data={"taskId": task_id}
        )
