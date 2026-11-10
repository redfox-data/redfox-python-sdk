"""Walmart 电商平台 API 端点"""

from typing import Optional, Dict, Any


class WalmartAPI:
    """
    Walmart 电商平台 API 集合

    包含 Walmart 关键词搜索商品、商品详情、商品评论、市场卖家报价等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_products(
        self,
        query: str,
        country: str = None,
        zip_code: str = None,
        state: str = None,
        store_id: str = None,
        min_price: float = None,
        max_price: float = None,
        sort_by: str = None,
        facet: str = None,
        page: int = None,
        cursor: str = None,
        source: str = "Walmart关键词搜索商品-SDK",
    ) -> dict:
        """
        Walmart关键词搜索商品

        通过关键词搜索商品并拿到 productId（其他接口的入参），支持 cursor/page 分页与门店级定位。

        :param query: 搜索关键词（必填），如 airpods pro
        :param country: 站点国家码，默认 US；可选 US（walmart.com）/CA（walmart.ca）
        :param zip_code: 邮编，传后返回门店级价格与库存，不传则为国家目录价
        :param state: 州（配合定位取门店价）
        :param store_id: 门店 ID（配合定位取门店价）
        :param min_price: 价格下限
        :param max_price: 价格上限
        :param sort_by: 排序方式
        :param facet: 分面过滤
        :param page: 分页页码
        :param cursor: 分页 cursor，传上一页响应中的 paginationToken 翻页
        :return: 商品列表字典，包含 items/paginationToken
        """
        data: Dict[str, Any] = {"query": query}
        if country:
            data["country"] = country
        if zip_code:
            data["zipCode"] = zip_code
        if state:
            data["state"] = state
        if store_id:
            data["storeId"] = store_id
        if min_price:
            data["minPrice"] = min_price
        if max_price:
            data["maxPrice"] = max_price
        if sort_by:
            data["sortBy"] = sort_by
        if facet:
            data["facet"] = facet
        if page:
            data["page"] = page
        if cursor:
            data["cursor"] = cursor
        return self._client.post("/story/api/walmart/search", data=data, source=source)

    def get_product(
        self,
        product_id: str,
        country: str = None,
        source: str = "Walmart商品详情-SDK",
    ) -> dict:
        """
        Walmart商品详情

        通过 productId 获取商品完整目录信息（品牌、描述、价格、图片集、规格参数等）。

        :param product_id: 商品 ID（必填，商品 URL 结尾的数字，如 17835006350；字母目录 id 如 34J2GQ9D9TFM 亦可），
            从 search_products 结果的 productId 字段获取
        :param country: 站点国家码，默认 US；可选 US（walmart.com）/CA（walmart.ca），product id 分站点不可跨用
        :return: 商品详情字典，包含 productId/title/brand/priceCurrent 等
        """
        data: Dict[str, Any] = {"productId": product_id}
        if country:
            data["country"] = country
        return self._client.post("/story/api/walmart/product", data=data, source=source)

    def get_reviews(
        self,
        product_id: str,
        country: str = None,
        limit: int = None,
        page: int = None,
        sort: str = None,
        rating: int = None,
        label: str = None,
        judgments: str = None,
        cursor: str = None,
        source: str = "Walmart商品评论-SDK",
    ) -> dict:
        """
        Walmart商品评论

        通过 productId 获取评论（正文、星级、作者、日期、有用票、验证购买、配图，
        默认附带情感/问题标签）。

        :param product_id: 商品 ID（必填），从 search_products 结果的 productId 字段获取
        :param country: 站点国家码，默认 US；可选 US（walmart.com）/CA（walmart.ca）
        :param limit: 每页评论数，1~50，默认 10
        :param page: 分页页码
        :param sort: 排序方式（仅做筛选非严格排序，需要顺序时自行排序）
        :param rating: 按星级筛选，精确匹配单个星值
        :param label: 附加智能标签，如 label=reports
        :param judgments: 传 off 返回不带 computed.labels 的精简评论页；默认开启（不额外计费）
        :param cursor: 分页 cursor，传上一页响应中的 paginationToken 翻页
        :return: 评论列表字典，包含 items/paginationToken
        """
        data: Dict[str, Any] = {"productId": product_id}
        if country:
            data["country"] = country
        if limit:
            data["limit"] = limit
        if page:
            data["page"] = page
        if sort:
            data["sort"] = sort
        if rating:
            data["rating"] = rating
        if label:
            data["label"] = label
        if judgments:
            data["judgments"] = judgments
        if cursor:
            data["cursor"] = cursor
        return self._client.post("/story/api/walmart/reviews", data=data, source=source)

    def get_offers(
        self,
        product_id: str,
        country: str = None,
        source: str = "Walmart市场卖家报价-SDK",
    ) -> dict:
        """
        Walmart市场卖家报价

        通过 productId 获取该商品上的全部市场报价（卖家名与 id、价格、库存、成色、退货期等）。

        :param product_id: 商品 ID（必填），从 search_products 结果的 productId 字段获取
        :param country: 站点国家码，默认 US；可选 US（walmart.com）/CA（walmart.ca）
        :return: 市场报价列表字典，包含 items
        """
        data: Dict[str, Any] = {"productId": product_id}
        if country:
            data["country"] = country
        return self._client.post("/story/api/walmart/offers", data=data, source=source)
