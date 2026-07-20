"""哔哩哔哩平台 API 端点"""

from typing import Optional, Dict, Any


class BilibiliAPI:
    """
    哔哩哔哩平台 API 集合

    包含 B 站账号查询、作品搜索、作品详情等接口。
    """

    def __init__(self, client):
        self._client = client

    def get_account(self, mid: str) -> dict:
        """
        获取哔哩哔哩账号信息（优质库）

        :param mid: 账号 MID（B 站用户唯一 ID，必填）
        :return: 账号信息字典
        """
        return self._client.post(
            "/story/api/bili/data/accountDetail", data={"mid": mid}
        )

    def get_work(self, bvid: str) -> dict:
        """
        获取哔哩哔哩作品内容详情（优质库）

        :param bvid: 作品 BV ID
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/bili/data/workDetail", data={"bvid": bvid}
        )

    def search_users(
        self,
        keyword: str,
        page_num: int = 1,
        order: str = None,
    ) -> dict:
        """
        搜索关键词获取哔哩哔哩账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param order: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword, "page": str(page_num)}
        if order is not None:
            data["order"] = order
        return self._client.post("/story/api/bili/data/accountSearch", data=data)

    def search_articles(
        self,
        keyword: str,
        page_num: int = 1,
        order: str = None,
    ) -> dict:
        """
        搜索关键词获取哔哩哔哩作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param order: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword, "page": str(page_num)}
        if order is not None:
            data["order"] = order
        return self._client.post("/story/api/bili/data/workSearch", data=data)

    def get_user_works(
        self,
        mid: str,
        page_num: int = 1,
        page_size: int = 30,
    ) -> dict:
        """
        获取哔哩哔哩账号作品列表（优质库）

        :param mid: 账号 MID（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 30
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {
            "mid": mid,
            "page": str(page_num),
            "pageSize": str(page_size),
        }
        return self._client.post("/story/api/bili/data/accountWorkList", data=data)
