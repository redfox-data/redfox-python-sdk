"""Amazon 电商平台 API 端点"""

from typing import Optional, Dict, Any


class AmazonAPI:
    """
    Amazon 电商平台 API 集合

    包含 Amazon 关键词搜索商品、商品详情、商品评论、竞品卖家报价等接口。
    """

    def __init__(self, client):
        self._client = client

    def search_products(
        self,
        query: str,
        country: str = None,
        page: int = None,
        cursor: str = None,
        source: str = "Amazon关键词搜索商品-SDK",
    ) -> dict:
        """
        Amazon关键词搜索商品

        通过关键词搜索商品并拿到 ASIN（其他接口的入参），支持 cursor/page 分页。

        :param query: 搜索关键词（必填），如 airpods pro
        :param country: 站点国家码，默认 US；可选 US/GB/CA/DE/FR/IT/ES/JP/IN/MX/BR/AU/NL
        :param page: 分页页码
        :param cursor: 分页 cursor，传上一页响应中的 paginationToken 翻页
        :return: 商品列表字典，包含 items/paginationToken
        """
        data: Dict[str, Any] = {"query": query}
        if country:
            data["country"] = country
        if page:
            data["page"] = page
        if cursor:
            data["cursor"] = cursor
        return self._client.post("/story/api/amazon/productSearch", data=data, source=source)

    def get_product(
        self,
        asin: str,
        country: str = None,
        source: str = "Amazon商品详情-SDK",
    ) -> dict:
        """
        Amazon商品详情

        通过 ASIN 获取商品完整目录信息（品牌、描述、价格、图片集、规格参数等）。

        :param asin: 商品 ASIN（必填，10 位商品标识符），从 search_products 结果的 asin 字段获取
        :param country: 站点国家码，默认 US；可选 US/GB/CA/DE/FR/IT/ES/JP/IN/MX/BR/AU/NL
        :return: 商品详情字典，包含 asin/title/brand/priceCurrent/ratingAvg 等
        """
        data: Dict[str, Any] = {"asin": asin}
        if country:
            data["country"] = country
        return self._client.post("/story/api/amazon/product", data=data, source=source)

    def get_reviews(
        self,
        asin: str,
        country: str = None,
        label: str = None,
        judgments: str = None,
        source: str = "Amazon商品评论-SDK",
    ) -> dict:
        """
        Amazon商品评论

        通过 ASIN 获取最有帮助的评论（正文、星级、评论者、验证购买、有用票、日期、配图）。

        :param asin: 商品 ASIN（必填），从 search_products 结果的 asin 字段获取
        :param country: 站点国家码，默认 US；可选 US/GB/CA/DE/FR/IT/ES/JP/IN/MX/BR/AU/NL
        :param label: 附加智能标签，如 label=reports，配合评论文本执行自定义判定
        :param judgments: 传 off 返回不带 computed.labels 的精简评论页；默认开启（不额外计费）
        :return: 评论列表字典，包含 reviews
        """
        data: Dict[str, Any] = {"asin": asin}
        if country:
            data["country"] = country
        if label:
            data["label"] = label
        if judgments:
            data["judgments"] = judgments
        return self._client.post("/story/api/amazon/reviews", data=data, source=source)

    def get_sellers(
        self,
        asin: str,
        country: str = None,
        source: str = "Amazon竞品卖家报价-SDK",
    ) -> dict:
        """
        Amazon竞品卖家报价

        通过 ASIN 获取该商品上的全部卖家报价（卖家名、价格、成色、评分等）。

        :param asin: 商品 ASIN（必填），从 search_products 结果的 asin 字段获取
        :param country: 站点国家码，默认 US；可选 US/GB/CA/DE/FR/IT/ES/JP/IN/MX/BR/AU/NL
        :return: 卖家报价列表字典，包含 items
        """
        data: Dict[str, Any] = {"asin": asin}
        if country:
            data["country"] = country
        return self._client.post("/story/api/amazon/sellers", data=data, source=source)
