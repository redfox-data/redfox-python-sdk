"""快手平台 API 端点"""

from typing import Optional, Dict, Any


class KuaishouAPI:
    """
    快手平台 API 集合（广域库）

    包含快手作品搜索、账号搜索、作品详情、视频提文案等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 作品相关 ───────────────────────────────────────────

    def search_works(
        self,
        keyword: str,
        page: int = 1,
        size: int = 20,
        sort: str = "综合",
    ) -> dict:
        """
        快手按关键词搜索作品（广域库）

        :param keyword: 搜索关键词（必填）
        :param page: 页码，从 1 开始，默认 1
        :param size: 每页条数，默认 20，最大 50
        :param sort: 排序方式：综合 / 最新 / 最多点赞 / 最多收藏，默认综合
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "page": page,
            "size": size,
            "sort": sort,
        }
        return self._client.post("/story/api/ksAllData/searchWork", data=data)

    def get_work(self, photo_id: str) -> dict:
        """
        快手按作品获取正文详情（广域库）

        :param photo_id: 作品 ID（列表接口返回的 photoId）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/ksAllData/queryWorkDetail", data={"photoId": photo_id}
        )

    def get_user_works(
        self,
        kwai_id: str = None,
        three_x_id: str = None,
        page: int = 1,
        size: int = 20,
    ) -> dict:
        """
        快手按账号获取作品列表（广域库）

        kwai_id 和 three_x_id 二选一必填。

        :param kwai_id: 快手账号平台展示 ID（search_users 接口返回的 kwaiId）
        :param three_x_id: 快手账号主页链接中的 ID，
            如 https://www.kuaishou.com/profile/3x4wxhrrzefrq4y 中的 3x4wxhrrzefrq4y
        :param page: 页码，从 1 开始，默认 1
        :param size: 每页条数，默认 20，最大 50
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"page": page, "size": size}
        if kwai_id:
            data["kwaiId"] = kwai_id
        if three_x_id:
            data["threeXId"] = three_x_id
        return self._client.post("/story/api/ksAllData/queryWorkList", data=data)

    # ─── 账号相关 ───────────────────────────────────────────

    def search_users(
        self,
        account_name: str,
        page: int = 1,
        page_size: int = 20,
    ) -> dict:
        """
        快手账号搜索（广域库）

        :param account_name: 快手账号名称（模糊搜索关键词，必填）
        :param page: 页码，从 1 开始，默认 1
        :param page_size: 每页条数，默认 20，最大 50
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {
            "accountName": account_name,
            "page": page,
            "pageSize": page_size,
        }
        return self._client.post("/story/api/ksAllData/searchUser", data=data)

    # ─── 视频提文案 ─────────────────────────────────────────

    def transcript_submit(self, url: str) -> dict:
        """
        快手视频提文案 - 提交任务

        :param url: 视频链接（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/submit/kuaishou",
            data={"url": url},
        )

    def transcript_result(self, task_id: str) -> dict:
        """
        快手视频提文案 - 查询结果

        :param task_id: 任务 ID（由 transcript_submit 返回）
        :return: 文案提取结果字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/result/kuaishou",
            data={"taskId": task_id},
        )
