# RedFox Python SDK

<div align="center">
<a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/v/redfox-python-sdk.svg" alt="PyPI version"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/pyversions/redfox-python-sdk.svg" alt="Python"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/l/redfox-python-sdk.svg" alt="License"></a>

<a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.md">中文</a> | <strong>English</strong> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ko.md">한국어</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ja.md">日本語</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.fr.md">Français</a>

</div>
<p align="center">
  <a href="https://redfox.hk/?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-3.png" alt="RedFox" width="100%">
  </a>
</p>

[RedFoxHub](https://redfox.hk/?source=github) Python SDK, providing data acquisition APIs for 14 major content platforms — [Douyin](https://redfox.hk/apis/douyin/0OT1E306), [Xiaohongshu](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [WeChat Official Accounts](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ), [Toutiao](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019), Kuaishou, WeChat Channels, YouTube, X (Twitter), Instagram, Dongchedi, Yiche, Autohome — plus multi-platform hot-trend aggregation, watermark-free video download & media upload tools, and AI capabilities: GPT Image Generation, Doubao Image/Video Generation, and AI Search (Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu).

## Why Choose RedFoxHub

<p align="center"><em>Limited-time flat pricing, as low as <strong style="color:#e53e3e">¥0.02/request</strong></em></p>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <b>⚡ Lightning Fast</b><br>
      <sub>Millisecond API response, global CDN acceleration for instant performance</sub>
    </td>
    <td align="center" width="25%">
      <b>🛡️ Secure & Reliable</b><br>
      <sub>Enterprise-grade security, encrypted transmission, 99.99% uptime guarantee</sub>
    </td>
    <td align="center" width="25%">
      <b>🌍 Global Coverage</b><br>
      <sub>Support major global new media platforms, one-click multi-platform access</sub>
    </td>
    <td align="center" width="25%">
      <b>💎 Flexible Pricing</b><br>
      <sub>Pay as you go, no hidden fees, flexible plans for every scale</sub>
    </td>
  </tr>
</table>

## SDK Core Features

- **Zero Config** — Set `REDFOX_API_KEY` environment variable and start coding. Flat parameters, no config objects.
- **Exponential Backoff Retry** — Automatic retry with jitter on network timeout, server 5xx, rate limit 429.
- **Sync + Async Dual Clients** — `RedFoxClient` and `AsyncRedFoxClient` with fully identical API.
- **File Upload** — Built-in multipart upload supporting file paths / bytes / file objects.
- **Structured Exceptions** — `RedFoxAuthError` / `RedFoxRateLimitError` / `RedFoxAPIError` with full debug context.
- **Production Ready** — Built on `httpx` with connection pooling, timeout control, context manager support.

## Installation

```bash
pip install redfox-python-sdk
```

## Authentication

### Get API Key

1. Go to [https://redfox.hk/settings/api-keys?source=github](https://redfox.hk/settings/api-keys?source=github) to register / login.
2. Copy your API Key from the console.
3. Set as environment variable or pass directly:

```bash
export REDFOX_API_KEY="YOUR_API_KEY"
```

## Multi-Platform API Documentation

<p align="center">
  <a href="https://redfox.hk/apis?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-1.png" alt="RedFox API Docs" width="100%">
  </a>
</p>

### API documentation includes:

- Request headers specification
- Request parameters description
- Response fields and data structure
- Request examples
- Response examples
- Common status codes

## Quick Start

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# Search Douyin videos
result = client.douyin.search_articles(keyword="AI")

# Search Xiaohongshu notes
result = client.xiaohongshu.search_articles(keyword="travel")

# Search WeChat Official Account articles
result = client.wechat.search_articles(keyword="tech")

# Search Kuaishou videos
result = client.kuaishou.search_works(keyword="food")

# Search YouTube videos
result = client.youtube.search_videos(search_query="AI tutorial")

# Aggregated hot trends TOP10
result = client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)

# Watermark-free video download
result = client.tools.download(url="https://www.douyin.com/video/xxx")

# AI Search
task = client.ai_search.kimi_submit(inquiry_text="Latest AI trends in 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## Supported Platforms

| Platform | Module | Methods | Description |
|----------|--------|---------|-------------|
| 📱 Douyin | `client.douyin` | 16 | Video/user search (premium + wide), user info, video detail, AI video search, hot/surge rankings, hot accounts, transcript |
| 📕 Xiaohongshu | `client.xiaohongshu` | 15 | Note/user search, account info, note detail, note list, AI note search, comments, daily/weekly/dark-horse rankings, hot accounts, hot note insights, transcript |
| 💬 WeChat | `client.wechat` | 16 | Article/user search (premium + wide), account info, article detail, article list, AI article search, 100K+ reads/original/strength/growth rankings |
| 📺 Bilibili | `client.bilibili` | 8 | Video/creator search, creator info, creator videos, video detail, audio extraction, transcript |
| 📰 Toutiao | `client.toutiao` | 5 | Content search, work detail, comments, user search, user works |
| 🎵 TikTok | `client.tiktok` | 4 | User search, video search, video detail, user videos |
| 🎬 Kuaishou | `client.kuaishou` | 6 | Video search, video detail, user videos, user search, transcript |
| 💚 WeChat Channels | `client.wechat_channels` | 7 | Video search, video detail, user videos, realtime detail by link, user search, transcript |
| ▶️ YouTube | `client.youtube` | 4 | Video search, video detail, video comments, transcript (subtitle extraction) |
| 🐦 X (Twitter) | `client.twitter` | 4 | Tweet search, tweet detail, user info, tweet comments |
| 📸 Instagram | `client.instagram` | 4 | General search, post detail, post comments, user info |
| 🚗 Dongchedi | `client.dongchedi` | 4 | Work search, work detail, user works, user search |
| 🚙 Yiche | `client.yiche` | 5 | Work search, article detail, video detail, user works, user search |
| 🚘 Autohome | `client.autohome` | 4 | Work search, article detail, video detail, user works |
| 🔥 Hot Trends | `client.hotspot` | 3 | Per-platform hot rankings, cross-platform keyword search, aggregated TOP10 |
| 🖼️ GPT Image | `client.gpt_image` | 2 | Image generation & result query |
| 🎨 Doubao Image | `client.doubao_image` | 4 | Pro/Lite image generation & query |
| 🎬 Doubao Video | `client.doubao_video` | 2 | Video generation & result query |
| 🔍 AI Search | `client.ai_search` | 12 | Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu search |
| 🛠️ Tools | `client.tools` | 12 | Multi-platform watermark-free video download, image/media upload |

## API Reference

### Douyin

```python
# Search videos (premium)
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# Search users (premium)
client.douyin.search_users(keyword="tech", offset=0)

# Get user profile
client.douyin.get_user(account_id="nxpt260212")

# Get user's video list
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# Get video detail (work_id or work_url)
client.douyin.get_work(work_id="7654143095876898089")

# Search AI videos
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Wide coverage ───
client.douyin.search_works_wide(keyword="AI", start_date="2026-08-01", end_date="2026-08-20")
client.douyin.search_accounts_wide(keyword="tech")
client.douyin.get_work_wide(video_id="7654143095876898089")
client.douyin.get_user_works_wide(unique_name="nxpt260212")

# ─── Rankings ───
client.douyin.get_daily_hot_rank(type="美食")                          # Daily hot videos
client.douyin.get_daily_surge_rank(type="全部")                        # Daily like-surge
client.douyin.get_weekly_surge_rank(type="全部")                       # Weekly like-surge
client.douyin.get_hot_accounts(date_type="days", rank_date="2026-08-20", type="全部")

# ─── Video transcript ───
task = client.douyin.transcript_submit(url="https://www.douyin.com/video/xxx")
result = client.douyin.transcript_result(task_id=task["taskId"])
```

### Xiaohongshu

```python
# Search notes
client.xiaohongshu.search_articles(keyword="travel", offset=0, sort_type="0")

# Search creators
client.xiaohongshu.search_users(keyword="travel", offset=0)

# Get creator profile
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# Get note detail (work_id or work_link)
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# Get creator's note list
client.xiaohongshu.get_user_works(red_id="nxpt260212", offset=0)

# Search AI notes
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Comments ───
task = client.xiaohongshu.comment_submit(opus_id="6a2ac3020000000035022d8e", data_num=-1)
result = client.xiaohongshu.comment_result(task_id=task["taskId"])

# ─── Rankings / insights ───
client.xiaohongshu.get_daily_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_weekly_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_hot_accounts(date_type=1, rank_date="2026-08-20", type="综合全部")
client.xiaohongshu.search_hot_notes(keyword="穿搭", start_date="2026-08-01", end_date="2026-08-20")
client.xiaohongshu.get_dark_horse_notes(keyword="AI,穿搭", start_date="2026-08-01")

# ─── Video transcript ───
task = client.xiaohongshu.transcript_submit(url="https://www.xiaohongshu.com/explore/xxx")
result = client.xiaohongshu.transcript_result(task_id=task["taskId"])
```

### WeChat Official Accounts

```python
# Search articles
client.wechat.search_articles(keyword="AI", offset=0)

# Search accounts
client.wechat.search_users(keyword="tech", offset=0)

# Get account info
client.wechat.get_account(account="rmrbwx")

# Get article detail (full content)
client.wechat.get_article_detail(url="https://mp.weixin.qq.com/s/...")

# Get article metadata
client.wechat.get_work(work_uuid="3F4DE056583609162E0816FBE8C183A3")

# Get account's article list
client.wechat.get_user_works(
    account="rmrbwx", offset=0,
    sort_type="_2",
    publish_time_start="2026-07-01",
    publish_time_end="2026-07-20"
)

# Search AI articles
client.wechat.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Wide coverage ───
client.wechat.search_articles_wide(keyword="AI", offset=0)
client.wechat.search_users_wide(keyword="tech")
client.wechat.get_work_wide(work_uuid="3F4DE056583609162E0816FBE8C183A3")
client.wechat.get_user_works_wide(account="rmrbwx")
client.wechat.get_account_wide(wx_id="gh_5c7e8b7f586b")

# ─── Rankings ───
client.wechat.get_ten_w_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_original_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_strength_rank(rank_type="day", rank_date="2026-08-20", category="科技数码")
client.wechat.get_reading_growth_rank(rank_date="2026-08-20")
```

### WeChat Channels

```python
# Search videos
client.wechat_channels.search_works(keyword="travel", sort="综合", page=1, size=20)

# Get video detail
client.wechat_channels.get_work(video_id="export/UzFfAgtgekIEAQAAAAAAxx8")

# Get account's video list (exact nickname match)
client.wechat_channels.get_user_works(nickname="央视新闻", page=1)

# Realtime detail by link
client.wechat_channels.get_work_by_link(url="https://weixin.qq.com/sph/xxx")

# Search accounts
client.wechat_channels.search_users(account_name="央视", page=1)

# Video transcript
task = client.wechat_channels.transcript_submit(url="https://weixin.qq.com/sph/xxx")
result = client.wechat_channels.transcript_result(task_id=task["taskId"])
```

### Bilibili

```python
# Search videos
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# Search creators
client.bilibili.search_users(keyword="tech", page=1, page_size=10, order="follower")

# Get creator profile
client.bilibili.get_account(mid="946974")

# Get creator's video list (mid or account_url)
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# Get video detail (bvid or work_url)
client.bilibili.get_work(bvid="BV1ghJg6hEWV")

# Get video audio URL
client.bilibili.get_audio(url="https://www.bilibili.com/video/BV1ghJg6hEWV")

# Video transcript
task = client.bilibili.transcript_submit(url="https://www.bilibili.com/video/BV1ghJg6hEWV")
result = client.bilibili.transcript_result(task_id=task["taskId"])
```

### Toutiao

```python
# Search content
client.toutiao.search_works(keyword="AI", offset=0)

# Get work detail
client.toutiao.get_work(opus_id="7592180245936046626")

# Get work comments
client.toutiao.get_comments(opus_id="7592180245936046626")

# Search accounts
client.toutiao.search_users(name="tech")

# Get account's work list
client.toutiao.get_user_works(category="profile_all", token="MS4wLjABAAAA...")
```

### Kuaishou

```python
# Search videos
client.kuaishou.search_works(keyword="food", page=1, size=20, sort="综合")

# Get video detail
client.kuaishou.get_work(photo_id="3x9sm2nqxmbfbuq")

# Get user's video list (kwai_id or three_x_id)
client.kuaishou.get_user_works(three_x_id="3x4wxhrrzefrq4y", page=1)

# Search users
client.kuaishou.search_users(account_name="王刚", page=1)

# Video transcript
task = client.kuaishou.transcript_submit(url="https://www.kuaishou.com/short-video/xxx")
result = client.kuaishou.transcript_result(task_id=task["taskId"])
```

### TikTok

```python
# Search users
client.tiktok.search_users(keyword="tech", cursor=0)

# Search videos
client.tiktok.search_videos(keyword="AI", count="20", sort_type="0", region="US")

# Get video detail
client.tiktok.get_work(aweme_id="7532000000000000000")

# Get user's videos
client.tiktok.get_user_works(sec_user_id="MS4wLjABAAAA...")
```

### YouTube

```python
# Search videos
client.youtube.search_videos(search_query="AI tutorial")

# Get video detail
client.youtube.get_video(video_id="sa8AzBK4dao")

# Get video comments
client.youtube.get_comments(video_id="sa8AzBK4dao", sort_by="top")

# Video transcript (subtitle / speech-to-text)
client.youtube.get_transcript(video_url="https://www.youtube.com/watch?v=sa8AzBK4dao")
```

### X (Twitter)

```python
# Search tweets
client.twitter.search_tweets(keyword="AI", search_type="Top")

# Get tweet detail
client.twitter.get_tweet(tweet_id="1957000000000000000")

# Get user info (screen_name or rest_id)
client.twitter.get_user(screen_name="elonmusk")

# Get tweet comments
client.twitter.get_comments(tweet_id="1957000000000000000")
```

### Instagram

```python
# General search
client.instagram.search(keyword="travel")

# Get post detail (Shortcode or full URL)
client.instagram.get_post(code_or_url="DRhvwVLAHAG")

# Get post comments
client.instagram.get_comments(code_or_url="DRhvwVLAHAG", sort_by="recent")

# Get user info (username or user_id)
client.instagram.get_user(username="natgeo")
```

### Dongchedi

```python
# Search works
client.dongchedi.search_works(keyword="小米SU7", offset="0", source_type="1")

# Get work detail
client.dongchedi.get_work(work_id="7532000000000000000", work_type="video")

# Get user's works
client.dongchedi.get_user_works(user_id="60480000000000000", cursor=0)

# Search users
client.dongchedi.search_users(keyword="陈震", offset=0)
```

### Yiche

```python
# Search works (club / shipin / xinwen)
client.yiche.search_works(keyword="小米SU7", page=1, source_type="xinwen")

# Get article detail
client.yiche.get_article(url="https://news.yiche.com/hao/wenzhang/xxx.html")

# Get video detail
client.yiche.get_video(work_id="50000000")

# Get user's works
client.yiche.get_user_works(user_id="600000000")

# Search users
client.yiche.search_users(keyword="陈震", page=1)
```

### Autohome

```python
# Search works (club / article / video)
client.autohome.search_works(keyword="小米SU7", source_type="video")

# Get article detail
client.autohome.get_article(work_id="3000000")

# Get video detail (0=creator, 4=Chejiahao)
client.autohome.get_video(video_id="5000000", video_type=4)

# Get creator's works
client.autohome.get_user_works(author_id="7000000", page=0)
```

### Hot Trends

```python
# Per-platform hot ranking: 1=Kuaishou 2=Douyin 5=Weibo 6=Xiaohongshu 7=Baidu 8=Bilibili 9=Zhihu 10=Toutiao
client.hotspot.get_platform_rank(
    platform=2,
    start_date="2026-08-20",
    end_date="2026-08-21",
)

# Cross-platform keyword hot search (range up to 30 days)
client.hotspot.search_by_keywords(
    keywords=["Samsung"],
    start_date="2026-08-01",
    end_date="2026-08-21",
    platforms=[2, 5, 10],
)

# Aggregated hot trends TOP10
client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)
```

### Tools

```python
# Universal video downloader (auto-detect platform)
client.tools.download(url="https://www.douyin.com/video/xxx")

# Per-platform watermark-free download
client.tools.download_douyin(url="https://www.douyin.com/video/xxx")
client.tools.download_kuaishou(url="https://www.kuaishou.com/short-video/xxx")
client.tools.download_xiaohongshu(url="https://www.xiaohongshu.com/explore/xxx")
client.tools.download_bilibili(url="https://www.bilibili.com/video/BV1xxx")
client.tools.download_wechat_channels(url="https://weixin.qq.com/sph/xxx")
client.tools.download_tiktok(url="https://www.tiktok.com/@user/video/xxx")
client.tools.download_youtube(url="https://www.youtube.com/watch?v=xxx")
client.tools.download_instagram(url="https://www.instagram.com/reel/xxx")
client.tools.download_twitter(url="https://x.com/user/status/xxx")

# Upload image (png / jpeg / webp)
client.tools.upload_image(file="./cover.png", format="png")

# Upload video/audio/image media
client.tools.upload_file(file="./clip.mp4", format="mp4")
```

### AI Search

```python
# Kimi search
task = client.ai_search.kimi_submit(inquiry_text="Latest AI trends in 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])

# Doubao search
task = client.ai_search.doubao_submit(inquiry_text="Summer drink recommendations")
result = client.ai_search.doubao_result(task_id=task["taskId"])

# Deepseek search
task = client.ai_search.deepseek_submit(inquiry_text="Python performance optimization")
result = client.ai_search.deepseek_result(task_id=task["taskId"])

# Yuanbao search
task = client.ai_search.yuanbao_submit(inquiry_text="Best EV recommendations")
result = client.ai_search.yuanbao_result(task_id=task["taskId"])

# Qianwen search
task = client.ai_search.qianwen_submit(inquiry_text="Hangzhou travel guide")
result = client.ai_search.qianwen_result(task_id=task["taskId"])

# Baidu search
task = client.ai_search.baidu_submit(inquiry_text="Today's financial news")
result = client.ai_search.baidu_result(task_id=task["taskId"])
```

### GPT Image Generation

```python
# Text-to-image
task = client.gpt_image.submit(
    prompt="An orange cat sitting on a windowsill with sunlight on its fur",
    size="1024x1024",
    quality="medium",
    output_format="png",
    model_name="gpt-image-2",
    operation="generate",
)
result = client.gpt_image.result(task_id=task["taskId"])

# Image-to-image / editing
task = client.gpt_image.submit(
    prompt="Replace the background with a beach",
    size="1024x1024",
    model_name="gpt-image-2",
    operation="edit",
    input_fidelity=5,
    images=[{"url": "https://example.com/your-image.jpg"}],
)
result = client.gpt_image.result(task_id=task["taskId"])
```

### Doubao Image Generation

```python
# Pro model
task = client.doubao_image.pro_submit(
    prompt="A futuristic city floating in the clouds",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    watermark=False,
)
result = client.doubao_image.pro_result(task_id=task["taskId"])

# Lite model (supports multi-image)
task = client.doubao_image.lite_submit(
    prompt="Four seasons landscape paintings",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    sequential="auto",
    max_images=4,
)
result = client.doubao_image.lite_result(task_id=task["taskId"])
```

### Doubao Video Generation

```python
# Text-to-video
task = client.doubao_video.submit(
    content=[{"type": "text", "text": "A cat yawning in the sunlight, fur gently blowing in the breeze"}],
    resolution="720p",
    ratio="16:9",
    duration=5,
    watermark=False,
    generate_audio=True,
)
result = client.doubao_video.result(task_id=task["taskId"])

# Image-to-video
task = client.doubao_video.submit(
    content=[
        {"type": "text", "text": "Make the person in the image smile and wave"},
        {"type": "image_url", "image_url": "https://example.com/photo.jpg"},
    ],
    resolution="720p",
    duration=5,
)
result = client.doubao_video.result(task_id=task["taskId"])
```

## Error Handling

The SDK provides three exception types:

```python
from redfox import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

try:
    result = client.douyin.search_articles(keyword="AI")
except RedFoxAuthError as e:
    print(f"Authentication failed: {e}")
except RedFoxRateLimitError as e:
    print(f"Rate limit exceeded: {e}")
except RedFoxAPIError as e:
    print(f"API error: code={e.code}, msg={e}")
```

## Requirements

- Python >= 3.8
- httpx >= 0.25.0

## License

MIT License
