"""RedFox SDK 自定义异常"""


class RedFoxAPIError(Exception):
    """RedFox API 调用异常基类"""

    def __init__(self, message: str, code: int = None, response: dict = None):
        self.message = message
        self.code = code
        self.response = response
        super().__init__(self.message)

    def __str__(self):
        if self.code:
            return f"RedFoxAPIError(code={self.code}): {self.message}"
        return f"RedFoxAPIError: {self.message}"


class RedFoxAuthError(RedFoxAPIError):
    """鉴权失败（API Key 无效或缺失）"""
    pass


class RedFoxRateLimitError(RedFoxAPIError):
    """请求频率超限"""
    pass
