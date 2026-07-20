"""RedFox SDK 使用示例"""

from redfox import RedFoxClient, RedFoxAPIError

# 初始化客户端（请在 https://redfox.hk/settings/api-keys?source=github 获取 API Key）
client = RedFoxClient(api_key="your_api_key")


def example_search_articles():
    """搜索抖音作品"""
    result = client.douyin.search_articles(keyword="人工智能", offset=0)
    print(f"总数: {result.get('total')}")
    for item in result.get("list", []):
        print(f"  {item.get('title')} - 点赞: {item.get('likeCount')}")


def example_get_user():
    """获取账号信息"""
    user = client.douyin.get_user(account_id="dy_user123")
    print(f"昵称: {user.get('nickname')}, 粉丝: {user.get('followerCount')}")


if __name__ == "__main__":
    print("请先配置 API Key 后取消注释运行对应示例")
