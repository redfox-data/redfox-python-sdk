"""AI 搜索工具 API 端点"""

from typing import Optional, Dict, Any


class AISearchAPI:
    """
    AI 搜索工具 API 集合

    支持 Kimi、豆包、Deepseek、元宝、千问、百度六种 AI 搜索引擎。
    每种引擎均为异步模式：先 submit 提交任务，再 result 查询结果。

    另含 Kimi K3 纯文字搜索，以及豆包/千问含商品卡信息的纯文本搜索。
    """

    def __init__(self, client):
        self._client = client

    # ─── Kimi ───────────────────────────────────────────────

    def kimi_submit(self, inquiry_text: str, source: str = "Kimi 联网 AI 搜索-SDK") -> dict:
        """
        Kimi 纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/kimi/submit", data={"inquiryText": inquiry_text}, source=source
        )

    def kimi_result(self, task_id: str, source: str = "查询 Kimi 搜索任务结果-SDK") -> dict:
        """
        Kimi 纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典，包含 completed/content/webPages
        """
        return self._client.post(
            "/story/api/kimi/result", data={"taskId": task_id}, source=source
        )

    # ─── 豆包 ───────────────────────────────────────────────

    def doubao_submit(self, inquiry_text: str, source: str = "豆包联网 AI 搜索-SDK") -> dict:
        """
        豆包纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/dbSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def doubao_result(self, task_id: str, source: str = "查询豆包搜索任务结果-SDK") -> dict:
        """
        豆包纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/dbResult", data={"taskId": task_id}, source=source
        )

    # ─── Deepseek ───────────────────────────────────────────

    def deepseek_submit(self, inquiry_text: str, source: str = "Deepseek 联网 AI 搜索-SDK") -> dict:
        """
        Deepseek 纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/dsSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def deepseek_result(self, task_id: str, source: str = "查询 Deepseek 搜索任务结果-SDK") -> dict:
        """
        Deepseek 纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/dsResult", data={"taskId": task_id}, source=source
        )

    # ─── 元宝 ───────────────────────────────────────────────

    def yuanbao_submit(self, inquiry_text: str, source: str = "元宝联网 AI 搜索-SDK") -> dict:
        """
        元宝纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/ybSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def yuanbao_result(self, task_id: str, source: str = "查询元宝搜索任务结果-SDK") -> dict:
        """
        元宝纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID（由 yuanbao_submit 返回）
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/ybResult", data={"taskId": task_id}, source=source
        )

    # ─── 千问 ───────────────────────────────────────────────

    def qianwen_submit(self, inquiry_text: str, source: str = "千问联网 AI 搜索-SDK") -> dict:
        """
        千问纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/qwSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def qianwen_result(self, task_id: str, source: str = "查询千问搜索任务结果-SDK") -> dict:
        """
        千问纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID（由 qianwen_submit 返回）
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/qwResult", data={"taskId": task_id}, source=source
        )

    # ─── 百度 ───────────────────────────────────────────────

    def baidu_submit(self, inquiry_text: str, source: str = "百度联网 AI 搜索-SDK") -> dict:
        """
        百度纯文字搜索 - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/bdSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def baidu_result(self, task_id: str, source: str = "查询百度搜索任务结果-SDK") -> dict:
        """
        百度纯文字搜索 - 查询任务结果

        :param task_id: 任务 ID（由 baidu_submit 返回）
        :return: 任务结果字典
        """
        return self._client.post(
            "/story/api/deepSearch/bdResult", data={"taskId": task_id}, source=source
        )

    # ─── Kimi K3 ────────────────────────────────────────────

    def kimi_k3_submit(self, inquiry_text: str, source: str = "Kimi K3 纯文字搜索-提交任务-SDK") -> dict:
        """
        kimi-K3 纯文字搜索 - 提交任务

        :param inquiry_text: 输入文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/kimi/submitK3", data={"inquiryText": inquiry_text}, source=source
        )

    # ─── 豆包（含商品卡信息） ─────────────────────────────────

    def doubao_goods_submit(
        self, inquiry_text: str, source: str = "豆包纯文本搜索（含商品卡）-提交任务-SDK"
    ) -> dict:
        """
        豆包纯文本搜索（含商品卡信息） - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/dbaSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def doubao_goods_result(
        self, task_id: str, source: str = "豆包纯文本搜索（含商品卡）-查询结果-SDK"
    ) -> dict:
        """
        豆包纯文本搜索（含商品卡信息） - 查询任务结果

        :param task_id: 任务 ID（由 doubao_goods_submit 返回）
        :return: 任务结果字典，包含参考文档 searchGuid、主回答 content、商品卡 cardData
        """
        return self._client.post(
            "/story/api/deepSearch/dbaResult", data={"taskId": task_id}, source=source
        )

    # ─── 千问（含商品卡信息） ─────────────────────────────────

    def qianwen_goods_submit(
        self, inquiry_text: str, source: str = "千问纯文本搜索（含商品卡）-提交任务-SDK"
    ) -> dict:
        """
        千问纯文本搜索（含商品卡信息） - 提交任务

        :param inquiry_text: 搜索文本（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/deepSearch/qwaSubmit", data={"inquiryText": inquiry_text}, source=source
        )

    def qianwen_goods_result(
        self, task_id: str, source: str = "千问纯文本搜索（含商品卡）-查询结果-SDK"
    ) -> dict:
        """
        千问纯文本搜索（含商品卡信息） - 查询任务结果

        :param task_id: 任务 ID（由 qianwen_goods_submit 返回）
        :return: 任务结果字典，包含 AI 导购结果 result、商品卡片 cardData
        """
        return self._client.post(
            "/story/api/deepSearch/qwaResult", data={"taskId": task_id}, source=source
        )
