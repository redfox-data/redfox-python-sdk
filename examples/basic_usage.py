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


def example_new_platforms():
    """新平台示例：快手 / 视频号 / YouTube / X / Instagram"""
    # 快手作品搜索
    client.kuaishou.search_works(keyword="美食", page=1, size=20, sort="综合")

    # 视频号作品搜索
    client.wechat_channels.search_works(keyword="旅行", page=1)

    # YouTube 视频搜索
    client.youtube.search_videos(search_query="AI tutorial")

    # X (Twitter) 推文搜索
    client.twitter.search_tweets(keyword="AI", search_type="Top")

    # Instagram 综合搜索
    client.instagram.search(keyword="travel")


def example_auto_platforms():
    """汽车平台示例：懂车帝 / 易车 / 汽车之家"""
    client.dongchedi.search_works(keyword="小米SU7", source_type="1")
    client.yiche.search_works(keyword="小米SU7", source_type="xinwen")
    client.autohome.search_works(keyword="小米SU7", source_type="video")


def example_hotspot():
    """多平台热点榜单"""
    # 抖音热点榜
    client.hotspot.get_platform_rank(
        platform=2, start_date="2026-08-20", end_date="2026-08-21"
    )

    # 全网聚合热点 TOP10
    client.hotspot.get_top10(
        start_date="2026-08-20 00:00:00", end_date="2026-08-21 00:00:00"
    )


def example_tools():
    """通用工具：短视频去水印下载 / 素材上传"""
    # 通用短视频下载（自动识别平台）
    result = client.tools.download(url="https://www.douyin.com/video/xxx")
    print(f"下载链接: {result}")

    # 上传图片
    # client.tools.upload_image(file="./cover.png", format="png")


def example_ai_search():
    """AI 搜索（Kimi/豆包/Deepseek/元宝/千问/百度）"""
    task = client.ai_search.kimi_submit(inquiry_text="2026年AI发展趋势")
    result = client.ai_search.kimi_result(task_id=task["taskId"])
    print(result)


if __name__ == "__main__":
    print("请先配置 API Key 后取消注释运行对应示例")
