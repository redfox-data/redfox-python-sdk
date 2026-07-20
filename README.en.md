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

[RedFoxHub](https://redfox.hk/?source=github) Python SDK, providing data acquisition APIs for six major content platforms — [Douyin](https://redfox.hk/apis/douyin/0OT1E306), [Xiaohongshu](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [WeChat Official Accounts](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ), [Toutiao](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019) — and four AI capabilities: GPT Image Generation, Doubao Image/Video Generation, and AI Search (Kimi/Doubao/Deepseek).

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

# Get Douyin user profile
result = client.douyin.get_user(account_id="nxpt260212")

# AI Search
task = client.ai_search.kimi_submit(inquiry_text="Latest AI trends in 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## Supported Platforms

| Platform | Module | Methods | Description |
|----------|--------|---------|-------------|
| 📱 Douyin | `client.douyin` | 6 | Content/user search, user info, work detail, AI content search |
| 📕 Xiaohongshu | `client.xiaohongshu` | 5 | Note/user search, account info, note detail, AI note search |
| 💬 WeChat | `client.wechat` | 7 | Article/user search, account info, article detail, AI article search |
| 📺 Bilibili | `client.bilibili` | 5 | Video/creator search, creator info, video list, video detail |
| 📰 Toutiao | `client.toutiao` | 2 | Content search, work detail |
| 🎵 TikTok | `client.tiktok` | 1 | User search |
| 🖼️ GPT Image | `client.gpt_image` | 2 | Image generation & result query |
| 🎨 Doubao Image | `client.doubao_image` | 4 | Pro/Lite image generation & query |
| 🎬 Doubao Video | `client.doubao_video` | 2 | Video generation & result query |
| 🔍 AI Search | `client.ai_search` | 6 | Kimi/Doubao/Deepseek search |

## API Reference

### Douyin

```python
# Search videos
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# Search users
client.douyin.search_users(keyword="tech", offset=0)

# Get user profile
client.douyin.get_user(account_id="nxpt260212")

# Get user's video list
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# Get video detail
client.douyin.get_work(work_id="7654143095876898089")

# Search AI videos
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### Xiaohongshu

```python
# Search notes
client.xiaohongshu.search_articles(keyword="travel", offset=0, sort_type="0")

# Search creators
client.xiaohongshu.search_users(keyword="travel", offset=0)

# Get creator profile
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# Get note detail
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# Search AI notes
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)
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
```

### Bilibili

```python
# Search videos
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# Search creators
client.bilibili.search_users(keyword="tech", page=1, page_size=10, order="follower")

# Get creator profile
client.bilibili.get_account(mid="946974")

# Get creator's video list
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# Get video detail
client.bilibili.get_work(bvid="BV1ghJg6hEWV")
```

### Toutiao

```python
# Search content
client.toutiao.search_works(keyword="AI", offset=0)

# Get work detail
client.toutiao.get_work(opus_id="7592180245936046626")
```

### TikTok

```python
# Search users
client.tiktok.search_users(keyword="tech", cursor=0)
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
- requests >= 2.25.0

## License

MIT License
