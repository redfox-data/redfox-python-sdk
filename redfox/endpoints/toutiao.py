"""今日头条平台 API 端点"""

from typing import Optional, Dict, Any


class ToutiaoAPI:
    """
    今日头条平台 API 集合

    包含今日头条作品搜索、作品详情等接口（实时）。
    """

    def __init__(self, client):
        self._client = client

    def search_works(
        self,
        keyword: str,
        offset: int = 0,
    ) -> dict:
        """
        获取今日头条账号作品列表（实时）

        :param keyword: 搜索关键词（必填）
        :param offset: 翻页偏移量，从 0 开始，每页 +1
        :return: 作品列表
        """
        data: Dict[str, Any] = {"keyword": keyword, "offset": str(offset)}
        return self._client.post("/story/api/toutiao/searchWork", data=data)

    def get_work(self, opus_id: str) -> dict:
        """
        获取今日头条作品内容详情（实时）

        :param opus_id: 作品 ID（必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/toutiao/workDetail", data={"opusId": opus_id}
        )
