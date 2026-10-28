"""红狐平台账户 API 端点（余额 / 调用记录）"""

from typing import Optional, Dict, Any


class RedFoxAccountAPI:
    """
    红狐平台账户 API 集合

    包含账户余额查询、接口调用记录查询等接口。
    """

    def __init__(self, client):
        self._client = client

    def balance(self, source: str = "用户余额查询-SDK") -> dict:
        """
        查询账户余额

        :return: 余额字典，包含 totalAvailablePoints（剩余积分）、
                 freeAvailablePoints（剩余免费积分）、paidAvailablePoints（剩余付费积分）
        """
        return self._client.get(
            "/story/web/points/api-key/balance",
            params={"apiKey": self._client.api_key},
            source=source,
        )

    def consume_flows(
        self,
        page_num: int = 1,
        page_size: int = 20,
        source: str = "接口调用记录查询-SDK",
    ) -> dict:
        """
        查询接口调用记录

        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :return: 调用记录字典，包含 total/pages/records（含消耗积分、原因、调用时间）
        """
        return self._client.get(
            "/story/web/points/api-key/consume-flows",
            params={
                "apiKey": self._client.api_key,
                "pageNum": str(page_num),
                "pageSize": str(page_size),
            },
            source=source,
        )
