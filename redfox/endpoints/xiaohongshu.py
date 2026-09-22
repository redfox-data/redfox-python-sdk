"""小红书平台 API 端点"""

from typing import Optional, Dict, Any


class XiaohongshuAPI:
    """
    小红书平台 API 集合

    包含小红书账号查询、作品搜索、笔记详情等接口。
    """

    def __init__(self, client):
        self._client = client

    # ─── 账号相关 ───────────────────────────────────────────

    def search_users(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
        source: str = "搜索小红书博主账号-SDK",
    ) -> dict:
        """
        搜索关键词获取小红书账号（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post(
            "/story/api/xhsUser/searchUser", data=data, source=source
        )

    def get_account(
        self,
        account_id: str,
        user_id: str = None,
        source: str = "获取小红书账号信息-SDK",
    ) -> dict:
        """
        获取小红书账号信息（优质库）

        :param account_id: 小红书号（必填）
        :param user_id: 用户 ID（可选，主页地址 user/profile/ 后的部分）
        :return: 账号信息字典
        """
        data: Dict[str, Any] = {"accountId": account_id}
        if user_id is not None:
            data["userId"] = user_id
        return self._client.post(
            "/story/api/xhsUser/queryAccountDetail", data=data, source=source
        )

    # ─── 作品相关 ───────────────────────────────────────────

    def search_articles(
        self,
        keyword: str,
        offset: int = 0,
        sort_type: str = None,
        source: str = "搜索小红书笔记-SDK",
    ) -> dict:
        """
        搜索关键词获取小红书作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param offset: 偏移量
        :param sort_type: 排序方式
        :return: 搜索结果字典
        """
        data: Dict[str, Any] = {"keyword": keyword}
        if offset is not None:
            data["offset"] = offset
        if sort_type is not None:
            data["sortType"] = sort_type
        return self._client.post(
            "/story/api/xhsUser/searchArticle", data=data, source=source
        )

    def get_work(
        self,
        work_id: str = None,
        work_link: str = None,
        source: str = "获取小红书笔记详情-SDK",
    ) -> dict:
        """
        获取小红书作品内容详情（优质库）

        work_id 和 work_link 至少传一个。

        :param work_id: 作品 ID
        :param work_link: 作品链接，如 https://www.xiaohongshu.com/explore/xxx
        :return: 作品详情字典
        """
        data: Dict[str, Any] = {}
        if work_id:
            data["workId"] = work_id
        if work_link:
            data["workLink"] = work_link
        return self._client.post(
            "/story/api/xhsUser/queryWorkDetail", data=data, source=source
        )

    def get_user_works(
        self,
        red_id: str = None,
        userid: str = None,
        offset: int = 0,
        sort_type: str = None,
        publish_time_start: str = None,
        publish_time_end: str = None,
        source: str = "查询小红书账号作品列表-SDK",
    ) -> dict:
        """
        查询小红书账号作品列表（优质库）

        red_id 和 userid 至少传一个。

        :param red_id: 账号平台展示 id
        :param userid: 账号主键 id
        :param offset: 偏移量，从 0 开始，每页 +20
        :param sort_type: 排序方式：_0=默认，_2=最新，_4=最热
        :param publish_time_start: 发布时间起始（格式 yyyy-MM-dd）
        :param publish_time_end: 发布时间结束（格式 yyyy-MM-dd）
        :return: 作品列表字典
        """
        data: Dict[str, Any] = {"offset": offset}
        if red_id:
            data["redId"] = red_id
        if userid:
            data["userid"] = userid
        if sort_type is not None:
            data["sortType"] = sort_type
        if publish_time_start is not None:
            data["publishTimeStart"] = publish_time_start
        if publish_time_end is not None:
            data["publishTimeEnd"] = publish_time_end
        return self._client.post(
            "/story/api/xhsUser/queryWorkList", data=data, source=source
        )

    # ─── AI 作品 ────────────────────────────────────────────

    def search_ai_articles(
        self,
        keyword: str,
        page_num: int = 1,
        page_size: int = 20,
        start_time: str = None,
        end_time: str = None,
        source: str = "搜索小红书 AI 创作相关笔记-SDK",
    ) -> dict:
        """
        搜索关键词获取小红书 AI 创作作品（优质库）

        :param keyword: 搜索关键词（必填）
        :param page_num: 页码，默认 1
        :param page_size: 每页条数，默认 20
        :param start_time: 起始时间，格式 "2026-06-01 00:00:00"
        :param end_time: 结束时间，格式 "2026-06-02 00:00:00"
        :param source: 调用来源标识（默认 "搜索小红书 AI 创作相关笔记-SDK"）
        :return: 搜索结果字典
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
        return self._client.post(
            "/story/api/parseWork/queryXhsAiMsgs", data=data, source=source
        )

    # ─── 评论相关 ───────────────────────────────────────────

    def comment_submit(self, opus_id: str, data_num: int, source: str = "获取小红书笔记一级评论-SDK") -> dict:
        """
        获取小红书一级评论（广域库）- 提交任务

        :param opus_id: 作品 id（必填）
        :param data_num: 所需条数，-1=全部（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/xhs/commentSubmit",
            data={"opusId": opus_id, "dataNum": data_num},
            source=source,
        )

    def comment_result(self, task_id: str, source: str = "查询小红书评论任务结果-SDK") -> dict:
        """
        获取小红书一级评论（广域库）- 查询结果

        :param task_id: 任务 ID（由 comment_submit 返回）
        :return: 评论结果字典
        """
        return self._client.post(
            "/story/api/xhs/commentResult", data={"taskId": task_id}, source=source
        )

    # ─── 榜单 ───────────────────────────────────────────

    def get_daily_hot_rank(self, rank_date: str, category: str, source: str = "小红书每日爆款笔记榜单-SDK") -> dict:
        """
        小红书每日爆款笔记榜单

        :param rank_date: 榜单日期，格式 yyyy-MM-dd（必填）
        :param category: 分类（必填）：综合全部、出行代步、医疗保健、时尚穿搭、美味佳肴等
        :return: 榜单字典
        """
        return self._client.get(
            "/story/api/cozeSkill/getXhsCozeSkillDataOne",
            params={"rankDate": rank_date, "category": category},
            source=source,
        )

    def get_weekly_hot_rank(
        self,
        rank_date: str = None,
        category: str = None,
        source: str = "小红书七日爆款笔记-SDK",
    ) -> dict:
        """
        小红书七日爆款笔记

        :param rank_date: 榜单日期（每天 19:00 更新「昨日」榜单）
        :param category: 分类：综合全部、出行代步、医疗保健、时尚穿搭、美味佳肴等
        :return: 榜单字典
        """
        params: Dict[str, Any] = {}
        if rank_date is not None:
            params["rankDate"] = rank_date
        if category is not None:
            params["category"] = category
        return self._client.get(
            "/story/api/cozeSkill/getXhsCozeSkillDataSeven", params=params, source=source
        )

    def get_hot_accounts(
        self,
        date_type: int = None,
        rank_date: str = None,
        type: str = None,
        source: str = "小红书热门账号推荐-SDK",
    ) -> dict:
        """
        小红书热门账号推荐

        :param date_type: 日期类型：1=日，2=周，3=月
        :param rank_date: 日期格式 yyyy-MM-dd。date_type=1 传所需日的起始时间（每晚 8 点更新昨日数据）；
            date_type=2 传所需周的周一时间（每周一更新上周数据）；date_type=3 传所需月的一号时间
        :param type: 类别：综合全部、出行代步、医疗保健、时尚穿搭、美味佳肴等
        :return: 热门账号字典
        """
        data: Dict[str, Any] = {}
        if date_type is not None:
            data["dateType"] = date_type
        if rank_date is not None:
            data["rankDate"] = rank_date
        if type is not None:
            data["type"] = type
        return self._client.post("/story/api/xhsData/query", data=data, source=source)

    def search_hot_notes(
        self,
        keyword: str = None,
        page_num: int = 1,
        page_size: int = 10,
        start_date: str = None,
        end_date: str = None,
        source: str = "小红书爆款笔记洞察-SDK",
    ) -> dict:
        """
        小红书爆款笔记洞察

        :param keyword: 搜索关键词（可选，不传则按互动数降序返回最热门数据）
        :param page_num: 页码，从 1 开始，默认 1（无关键词时生效）
        :param page_size: 每页条数，默认 10，最大 50（无关键词时生效）
        :param start_date: 开始日期，格式 yyyy-MM-dd
        :param end_date: 结束日期，格式 yyyy-MM-dd
        :return: 爆款笔记字典
        """
        data: Dict[str, Any] = {"pageNum": page_num, "pageSize": page_size}
        if keyword is not None:
            data["keyword"] = keyword
        if start_date is not None:
            data["startDate"] = start_date
        if end_date is not None:
            data["endDate"] = end_date
        return self._client.post("/story/api/xhs/search/search", data=data, source=source)

    def get_dark_horse_notes(self, keyword: str, start_date: str, source: str = "小红书黑马爆文榜-SDK") -> dict:
        """
        小红书黑马爆文榜

        :param keyword: 关键词（必填），多个关键词用逗号分隔，最多 5 个，总长度不超过 200
        :param start_date: 开始日期，格式 yyyy-MM-dd（必填），最长为最近 30 天，默认 30 天前
        :return: 黑马爆文榜字典
        """
        return self._client.post(
            "/story/api/cozeSkill/getLowPowderExplosiveArticle",
            data={"keyword": keyword, "startDate": start_date},
            source=source,
        )

    # ─── 视频提文案 ─────────────────────────────────────────

    def transcript_submit(self, url: str, source: str = "小红书视频提文案-SDK") -> dict:
        """
        小红书视频提文案 - 提交任务

        :param url: 视频链接（必填）
        :return: 包含 taskId 的字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/submit/xhs",
            data={"url": url},
            source=source,
        )

    def transcript_result(self, task_id: str, source: str = "查询小红书视频提文案任务结果-SDK") -> dict:
        """
        小红书视频提文案 - 查询结果

        :param task_id: 任务 ID（由 transcript_submit 返回）
        :return: 文案提取结果字典
        """
        return self._client.post(
            "/story/api/parseWork/audioTextExtract/result/xhs",
            data={"taskId": task_id},
            source=source,
        )
