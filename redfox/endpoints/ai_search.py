"""AI 搜索工具 API 端点"""

from typing import Optional, Dict, Any


class AISearchAPI:
    """
    AI 搜索工具 API 集合

    支持 Kimi、豆包、Deepseek 三种 AI 搜索引擎。
    每种引擎均为异步模式：先 submit 提交任务，再 result 查询结果。
    """

    def __init__(self, client):
        self._client = client

    # ─── Kimi ───────────────────────────────────────────────

    def kimi_submit(self, inquiry_text: str) -> dict:
        """
        Kimi 纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/kimi/submit", data={"inquiryText": inquiry_text}
        )

    def kimi_result(self, task_id: str) -> dict:
        """
        Kimi 纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典，包含 completed/content/webPages
        """
        return self._client.post(
            "/story/api/kimi/result", data={"taskId": task_id}
        )

    # ─── 豆包 ───────────────────────────────────────────────

    def doubao_submit(self, inquiry_text: str) -> dict:
        """
        豆包纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/dbSubmit", data={"inquiryText": inquiry_text}
        )

    def doubao_result(self, task_id: str) -> dict:
        """
        豆包纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/dbResult", data={"taskId": task_id}
        )

    # ─── Deepseek ───────────────────────────────────────────

    def deepseek_submit(self, inquiry_text: str) -> dict:
        """
        Deepseek 纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/dsSubmit", data={"inquiryText": inquiry_text}
        )

    def deepseek_result(self, task_id: str) -> dict:
        """
        Deepseek 纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/dsResult", data={"taskId": task_id}
        )
