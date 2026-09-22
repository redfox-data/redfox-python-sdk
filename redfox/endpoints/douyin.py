"""抖音平台 API 端点"""

from typing import Optional, Dict, Any


class DouyinAPI:
    """
    抖音平台 API 集合

    包含抖音作品搜索、账号查询、作品详情等接口。
    所有接口均为 POST 请求，参数通过 JSON body 传递。
    """

    def __init__(self, client):
        self._client = client

    # ─── 作品相关 ───────────────────────────────────────────

    def get_work(
        self,
        work_id: str = None,
        work_url: str = None,
        source: str = "获取抖音作品详情（优质库）-SDK",
    ) -> dict:
        """
        获取抖音作品内容详情（优质库）

        通过作品 ID 或作品链接查询作品详细信息，包括互动数据、作者信息等。
        work_id 和 work_url 至少传一个。

        :param work_id: 作品 ID，如 "10000123456789"
        :param work_url: 作品链接，如 "https://www.douyin.com/video/xxx"
        :return: 作品详情字典
        """
        data = {}
        if work_id:
            data["workId"] = work_id
        if work_url:
            data["workUrl"] = work_url

        return self._client.post("/story/api/dyData/queryWork", data=data, source=source)

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
        source: str = "搜索抖音作品（优质库）-SDK",
    ) -> dict:
        """
        搜索关键词获取抖音作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始，每次 +20
        :param sort_type: 排序方式，如 "default"
        :return: 搜索结果字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/searchArticle", data=data, source=source)

    def get_user_works(
        self,
        account_id: str = None,
        author_url: str = None,
        sec_user_id: str = None,
        offset: int = 0,
        sort_type: str = None,
        source: str = "获取抖音账号作品列表（优质库）-SDK",
    ) -> dict:
        """
        获取抖音账号作品列表（优质库）

        account_id / author_url / sec_user_id 至少传一个。

        :param account_id: 抖音号
        :param author_url: 作者主页链接
        :param sec_user_id: 作者 sec_user_id
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式：0=默认，2=最新，4=最热
        :return: 作品列表字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {}
        if account_id:
            data["accountId"] = account_id
        if author_url:
            data["authorUrl"] = author_url
        if sec_user_id:
            data["secUserId"] = sec_user_id
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/queryWorkList", data=data, source=source)

    # ─── 账号相关 ───────────────────────────────────────────

    def get_user(self, account_id: str, source: str = "获取抖音账号信息-SDK") -> dict:
        """
        获取抖音账号信息（优质库）

        :param account_id: 抖音账号 ID（支持 unique_id、short_id、uid 任一匹配）
        :return: 账号信息字典
        """
        return self._client.post(
            "/story/api/dyData/queryUser",
            data={"accountId": account_id},
            source=source,
        )

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
        source: str = "搜索抖音账号（优质库）-SDK",
    ) -> dict:
        """
        搜索关键词获取抖音账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 分页偏移量，从 0 开始
        :param sort_type: 排序方式
        :return: 搜索结果字典，包含 total/hasMore/list
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type

        return self._client.post("/story/api/dyData/searchUser", data=data, source=source)

    # ─── AI 作品 ────────────────────────────────────────────

    def search_ai_articles(
        self,
        keyword: str,
        page_num: int = 1,
        page_size: int = 20,
        start_time: str = None,
        end_time: str = None,
        source: str = "搜索抖音 AI 相关作品-SDK",
    ) -> dict:
        """
        搜索关键词获取抖音 AI 作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :param start_time: 开始时间，格式 "2026-06-01 00:00:00"
        :param end_time: 结束时间，格式 "2026-06-02 00:00:00"
        :return: 搜索结果字典，包含 total/pageNum/pageSize/pages/list
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "pageNum": page_num,
            "pageSize": page_size,
        }
        if start_time is not None:
            data["startTime"] = start_time
        if end_time is not None:
            data["endTime"] = end_time

        return self._client.post("/story/api/parseWork/queryDyAiMsgs", data=data, source=source)

    # ─── 广域库（更大覆盖范围） ──────────────────────────────

    def search_works_wide(
        self,
        keyword: str,
        start_date: str = None,
        end_date: str = None,
        page_num: int = 1,
        page_size: int = 10,
        source: str = "搜索抖音作品（广域库）-SDK",
    ) -> dict:
        """
        搜索关键词获取抖音作品（广域库）

        :param keyword: 搜索关键词（必填，匹配作品正文）
        :param start_date: 开始日期，格式 yyyy-MM-dd
        :param end_date: 结束日期，格式 yyyy-MM-dd
        :param page_num: 页码，从 1 开始，默认 1
        :param page_size: 每页大小，默认 10，最大 50
        :return: 搜索结果字典，包含 total/pageNum/pageSize/list
        """
        data: Dict[str, Any] = {
            "keyword": keyword,
            "pageNum": page_num,
            "pageSize": page_size,
        }
        if start_date is not None:
            data["startDate"] = start_date
        if end_date is not None:
            data["endDate"] = end_date
        return self._client.post("/story/api/dy/data/searchWork", data=data, source=source)

    def search_accounts_wide(
        self,
        keyword: str,
        page_num: int = 1,
        page_size: int = 10,
        source: str = "搜索抖音账号（广域库）-SDK",
    ) -> dict:
        """
        搜索关键词获取抖音账号（广域库）

        :param keyword: 搜索关键词（必填，匹配账号名）
        :param page_num: 页码，从 1 开始，默认 1
        :param page_size: 每页大小，默认 10，最大 50
        :return: 搜索结果字典
        """
        return self._client.post(
            "/story/api/dy/data/searchAccount",
            data={"keyword": keyword, "pageNum": page_num, "pageSize": page_size},
            source=source,
        )

    def get_work_wide(self, video_id: str, source: str = "获取抖音作品详情（广域库）-SDK") -> dict:
        """
        获取抖音作品内容详情（广域库）

        :param video_id: 作品 ID（对应 aweme_id，必填）
        :return: 作品详情字典
        """
        return self._client.post(
            "/story/api/dy/data/workDetail", data={"videoId": video_id}, source=source
        )

    def get_user_works_wide(
        self,
        user_id: str = None,
        unique_name: str = None,
        short_id: str = None,
        page_num: int = 1,
        page_size: int = 10,
        start_date: str = None,
        end_date: str = None,
        source: str = "获取抖音账号作品列表（广域库）-SDK",
    ) -> dict:
        """
        获取抖音账号作品列表（广域库）

        user_id / unique_name / short_id 三选一必填。

        :param user_id: 账号主键 id / uid
        :param unique_name: 账号平台展示 id
        :param short_id: 账号平台展示 id-short
        :param page_num: 页码，从 1 开始，默认 1
        :param page_size: 每页大小，默认 10，最大 50
        :param start_date: 开始时间，格式 yyyy-MM-dd
        :param end_date: 结束时间，格式 yyyy-MM-dd
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"pageNum": page_num, "pageSize": page_size}
        if user_id:
            data["userId"] = user_id
        if unique_name:
            data["uniqueName"] = unique_name
        if short_id:
            data["shortId"] = short_id
        if start_date is not None:
            data["startDate"] = start_date
        if end_date is not None:
            data["endDate"] = end_date
        return self._client.post("/story/api/dy/data/listWorkByAccount", data=data, source=source)

    # ─── 榜单 ───────────────────────────────────────────

    def get_daily_hot_rank(
        self,
        type: str = None,
        start_time: str = None,
        end_time: str = None,
        source: str = "抖音每日热门作品榜-SDK",
    ) -> dict:
        """
        抖音每日热门作品榜

        :param type: 类别（不传则查询全部）：小剧场、财富理财、二次元、美食、旅行、汽车等
        :param start_time: 开始时间，格式 yyyy-MM-dd（不传则默认昨日，每日 10 点后更新昨日数据）
        :param end_time: 结束时间，格式 yyyy-MM-dd（不传则默认昨日）
        :return: 榜单字典
        """
        data: Dict[str, Any] = {}
        if type is not None:
            data["type"] = type
        if start_time is not None:
            data["startTime"] = start_time
        if end_time is not None:
            data["endTime"] = end_time
        return self._client.post("/story/api/dy/search/likesRank", data=data, source=source)

    def get_daily_surge_rank(
        self,
        type: str = None,
        start_time: str = None,
        source: str = "抖音每日点赞飙升榜-SDK",
    ) -> dict:
        """
        抖音每日点赞猟升榜

        :param type: 分类展示名称：小剧场 财富理财 二次元 美食 旅行 等；为空或"全部"时查询全部分类
        :param start_time: 榜单日期，格式 yyyy-MM-dd（不传则默认昨日，每日 16 点更新昨日数据）
        :return: 榜单字典
        """
        data: Dict[str, Any] = {}
        if type is not None:
            data["type"] = type
        if start_time is not None:
            data["startTime"] = start_time
        return self._client.post("/story/api/dy/search/getDailyRank", data=data, source=source)

    def get_weekly_surge_rank(
        self,
        type: str = None,
        start_time: str = None,
        source: str = "抖音七日点赞飙升榜-SDK",
    ) -> dict:
        """
        抖音七日点赞猟升榜

        :param type: 分类展示名称：小剧场 财富理财 二次元 美食 旅行 等；为空或"全部"时查询全部分类
        :param start_time: 榜单日期，格式 yyyy-MM-dd（不传则默认昨日，每日 16:30 更新昨日数据）
        :return: 榜单字典
        """
        data: Dict[str, Any] = {}
        if type is not None:
            data["type"] = type
        if start_time is not None:
            data["startTime"] = start_time
        return self._client.post("/story/api/dy/search/getWeeklyRank", data=data, source=source)

    def get_hot_accounts(
        self,
        date_type: str,
        rank_date: str,
        type: str,
        source: str = "抖音热门账号推荐-SDK",
    ) -> dict:
        """
        抖音热门账号推荐

        :param date_type: 日期类型：days=日，weeks=周，months=月（必填）
        :param rank_date: 日期格式 yyyy-MM-dd（必填）。days 传所需日的起始时间（每晚 8 点更新昨日数据）；
            weeks 传所需周的周一时间（每周一更新上周数据）；months 传所需月的一号时间（每月一号更新上月数据）
        :param type: 类别（必填）：全部、个人才艺、生活vlog、财富理财、二次元、美食、汽车等
        :return: 热门账号字典
        """
        return self._client.post(
            "/story/api/dyData/query",
            data={"dateType": date_type, "rankDate": rank_date, "type": type},
            source=source,
        )

    # ─── 视频提文案 ─────────────────────────────────────────

    def transcript_submit(self, url: str, source: str = "抖音视频提文案-SDK") -> dict:
        """
        抖音视频提文案 - 提交任务

        :param url: 视频链接（必填），支持口令分享文本
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/submit/douyin",
            data={"url": url},
            source=source,
        )

    def transcript_result(self, task_id: str, source: str = "查询抖音视频提文案任务结果-SDK") -> dict:
        """
        抖音视频提文案 - 查询结果

        :param task_id: 任务 ID（由 transcript_submit 返回）
        :return: 文案提取结果字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/result/douyin",
            data={"taskId": task_id},
            source=source,
        )
