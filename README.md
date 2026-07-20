# RedFox Python SDK

<div align="center">
<a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/v/redfox-python-sdk.svg" alt="PyPI version"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/pyversions/redfox-python-sdk.svg" alt="Python"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/l/redfox-python-sdk.svg" alt="License"></a>

<strong>中文</strong> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.en.md">English</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ko.md">한국어</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ja.md">日本語</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.fr.md">Français</a>

</div>
<p align="center">
  <a href="https://redfox.hk/?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-3.png" alt="RedFox Logo" width="100%">
  </a>
</p>

[RedFoxHub](https://redfox.hk/?source=github) Python SDK，提供[抖音](https://redfox.hk/apis/douyin/0OT1E306)、[小红书](https://redfox.hk/apis/xiaohongshu/4IVIDHEN)、[公众号](https://redfox.hk/apis/gongzhonghao/6C4A77XR)、[B站](https://redfox.hk/apis/bilibili/TIN1NMTZ)、[今日头条](https://redfox.hk/apis/jinritoutiao/28CFGF5I)、[TikTok](https://redfox.hk/apis/tool-tiktok/20070019) 六大内容平台的数据采集接口，以及 GPT 图片生成、豆包图片/视频生成、AI 搜索（Kimi/豆包/Deepseek）四大 AI 能力接口。

## 为什么选择 RedFoxHub

<p align="center"><em>平台数据限时统一定价，最低可至 <strong style="color:#e53e3e">¥0.02/次</strong></em></p>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <b>⚡ 极速响应</b><br>
      <sub>毫秒级 API 响应，全球 CDN 加速，让您的应用快如闪电</sub>
    </td>
    <td align="center" width="25%">
      <b>🛡️ 安全可靠</b><br>
      <sub>企业级安全防护，数据加密传输，99.99% 可用性保证</sub>
    </td>
    <td align="center" width="25%">
      <b>🌍 全球覆盖</b><br>
      <sub>支持全球主流新媒体平台，一键接入多平台数据</sub>
    </td>
    <td align="center" width="25%">
      <b>💎 弹性计费</b><br>
      <sub>按需付费，无隐藏费用，灵活的套餐满足不同需求</sub>
    </td>
  </tr>
</table>

## SDK 核心特性

- **零配置** — 设置环境变量 `REDFOX_API_KEY` 即可使用，无需配置对象，扁平化参数
- **指数退避自动重试** — 网络超时、服务端 5xx、限流 429 自动重试（含随机抖动防惊群）
- **同步 + 异步双客户端** — `RedFoxClient` 与 `AsyncRedFoxClient`，API 完全一致
- **结构化异常** — `RedFoxAuthError` / `RedFoxRateLimitError` / `RedFoxAPIError`，含完整调试上下文
- **生产就绪** — 基于 `httpx` 构建，支持连接复用、超时控制、上下文管理器

## 安装

```bash
pip install redfox-python-sdk
```

## 身份认证

### 获取 API Key

1. 前往 [https://redfox.hk/settings/api-keys?source=github](https://redfox.hk/settings/api-keys?source=github) 注册 / 登录。
2. 在控制台复制你的 API Key。
3. 设置为环境变量或直接传入：

```bash
export REDFOX_API_KEY="YOUR_API_KEY"
```

## 多平台API文档

<p align="center">
  <a href="https://redfox.hk/apis?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-1.png" alt="RedFox Logo" width="100%">
  </a>
</p>

### API文档中包含：

- 请求头说明
- 请求参数说明
- 返回值和数据结构说明
- 请求示例
- 响应示例
- 常见状态码说明

## 快速开始

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# 搜索抖音作品
result = client.douyin.search_articles(keyword="AI")

# 搜索小红书笔记
result = client.xiaohongshu.search_articles(keyword="旅行")

# 搜索公众号文章
result = client.wechat.search_articles(keyword="科技")

# 获取抖音用户主页
result = client.douyin.get_user(account_id="nxpt260212")

# AI 搜索
task = client.ai_search.kimi_submit(inquiry_text="2026年AI发展趋势")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## 支持的平台

| 平台 | 模块 | 方法数 | 说明 |
|------|------|--------|------|
| 📱 抖音 | `client.douyin` | 6 | 作品搜索、账号搜索、用户信息、作品详情、AI作品搜索 |
| 📕 小红书 | `client.xiaohongshu` | 5 | 笔记搜索、账号搜索、账号信息、笔记详情、AI笔记搜索 |
| 💬 公众号 | `client.wechat` | 7 | 文章搜索、账号搜索、账号信息、文章详情、用户作品列表、AI文章搜索 |
| 📺 B站 | `client.bilibili` | 5 | 视频搜索、UP主搜索、UP主信息、UP主作品、视频详情 |
| 📰 今日头条 | `client.toutiao` | 2 | 内容搜索、作品详情 |
| 🎵 TikTok | `client.tiktok` | 1 | 用户搜索 |
| 🖼️ GPT 图片 | `client.gpt_image` | 2 | 图片生成、结果查询 |
| 🎨 豆包图片 | `client.doubao_image` | 4 | Pro/Lite 图片生成及查询 |
| 🎬 豆包视频 | `client.doubao_video` | 2 | 视频生成、结果查询 |
| 🔍 AI 搜索 | `client.ai_search` | 6 | Kimi/豆包/Deepseek 搜索 |

## API 参考

### 抖音

```python
# 搜索抖音作品
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# 搜索抖音用户
client.douyin.search_users(keyword="科技", offset=0)

# 获取账号信息
client.douyin.get_user(account_id="nxpt260212")

# 获取账号作品列表
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# 获取作品详情
client.douyin.get_work(work_id="7654143095876898089")

# 搜索AI作品
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### 小红书

```python
# 搜索笔记
client.xiaohongshu.search_articles(keyword="旅行", offset=0, sort_type="0")

# 搜索博主
client.xiaohongshu.search_users(keyword="旅行", offset=0)

# 获取博主信息
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# 获取笔记详情
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# 搜索AI笔记
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### 公众号

```python
# 搜索文章
client.wechat.search_articles(keyword="AI", offset=0)

# 搜索账号
client.wechat.search_users(keyword="科技", offset=0)

# 获取账号信息
client.wechat.get_account(account="rmrbwx")

# 获取文章详情（支持全文内容）
client.wechat.get_article_detail(url="https://mp.weixin.qq.com/s/...")

# 获取文章元数据
client.wechat.get_work(work_uuid="3F4DE056583609162E0816FBE8C183A3")

# 获取账号文章列表
client.wechat.get_user_works(
    account="rmrbwx", offset=0,
    sort_type="_2",
    publish_time_start="2026-07-01",
    publish_time_end="2026-07-20"
)
```

### B站

```python
# 搜索视频
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# 搜索UP主
client.bilibili.search_users(keyword="影视飓风", page=1, page_size=10, order="follower")

# 获取UP主信息
client.bilibili.get_account(mid="946974")

# 获取UP主视频列表
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# 获取视频详情
client.bilibili.get_work(bvid="BV1ghJg6hEWV")
```

### 今日头条

```python
# 搜索内容
client.toutiao.search_works(keyword="AI", offset=0)

# 获取作品详情
client.toutiao.get_work(opus_id="7592180245936046626")
```

### TikTok

```python
# 搜索用户
client.tiktok.search_users(keyword="tech", cursor=0)
```

### AI 搜索

```python
# Kimi 搜索
task = client.ai_search.kimi_submit(inquiry_text="2026年AI发展趋势")
result = client.ai_search.kimi_result(task_id=task["taskId"])

# 豆包搜索
task = client.ai_search.doubao_submit(inquiry_text="夏日茶饮推荐")
result = client.ai_search.doubao_result(task_id=task["taskId"])

# Deepseek 搜索
task = client.ai_search.deepseek_submit(inquiry_text="Python性能优化")
result = client.ai_search.deepseek_result(task_id=task["taskId"])
```

### GPT 图片生成

```python
# 文生图
task = client.gpt_image.submit(
    prompt="一只坐在窗台上的橘猫，阳光洒在毛发上",
    size="1024x1024",
    quality="medium",
    output_format="png",
    model_name="gpt-image-2",
    operation="generate",
)
result = client.gpt_image.result(task_id=task["taskId"])

# 图生图/编辑
task = client.gpt_image.submit(
    prompt="将背景替换成海滩",
    size="1024x1024",
    model_name="gpt-image-2",
    operation="edit",
    input_fidelity=5,
    images=[{"url": "https://example.com/your-image.jpg"}],
)
result = client.gpt_image.result(task_id=task["taskId"])
```

### 豆包图片生成

```python
# Pro 模型
task = client.doubao_image.pro_submit(
    prompt="一座漂浮在云端的未来城市",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    watermark=False,
)
result = client.doubao_image.pro_result(task_id=task["taskId"])

# Lite 模型（支持组图）
task = client.doubao_image.lite_submit(
    prompt="春夏秋冬四季风景画",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    sequential="auto",
    max_images=4,
)
result = client.doubao_image.lite_result(task_id=task["taskId"])
```

### 豆包视频生成

```python
# 文生视频
task = client.doubao_video.submit(
    content=[{"type": "text", "text": "一只猫在阳光下打哈欠，毛发随着微风轻轻飘动"}],
    resolution="720p",
    ratio="16:9",
    duration=5,
    watermark=False,
    generate_audio=True,
)
result = client.doubao_video.result(task_id=task["taskId"])

# 图生视频
task = client.doubao_video.submit(
    content=[
        {"type": "text", "text": "让图中的人物微笑并挥手"},
        {"type": "image_url", "image_url": "https://example.com/photo.jpg"},
    ],
    resolution="720p",
    duration=5,
)
result = client.doubao_video.result(task_id=task["taskId"])
```

## 错误处理

SDK 提供三种异常类型：

```python
from redfox import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

try:
    result = client.douyin.search_articles(keyword="AI")
except RedFoxAuthError as e:
    print(f"认证失败: {e}")
except RedFoxRateLimitError as e:
    print(f"频率超限: {e}")
except RedFoxAPIError as e:
    print(f"API错误: code={e.code}, msg={e}")
```

## 依赖

- Python >= 3.8
- requests >= 2.25.0

## 许可证

MIT License
