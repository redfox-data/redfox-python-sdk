# RedFox Python SDK

<div align="center">
<a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/v/redfox-python-sdk.svg" alt="PyPI version"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/pyversions/redfox-python-sdk.svg" alt="Python"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/l/redfox-python-sdk.svg" alt="License"></a>

<a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.md">中文</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.en.md">English</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ko.md">한국어</a> | <strong>日本語</strong> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.fr.md">Français</a>

</div>
<p align="center">
  <a href="https://redfox.hk/?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-3.png" alt="RedFox" width="100%">
  </a>
</p>

[RedFoxHub](https://redfox.hk/?source=github) Python SDK。6大コンテンツプラットフォーム — [抖音](https://redfox.hk/apis/douyin/0OT1E306)、[小紅書](https://redfox.hk/apis/xiaohongshu/4IVIDHEN)、[WeChat公衆号](https://redfox.hk/apis/gongzhonghao/6C4A77XR)、[Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ)、[今日頭条](https://redfox.hk/apis/jinritoutiao/28CFGF5I)、[TikTok](https://redfox.hk/apis/tool-tiktok/20070019) — のデータ取得APIと、4つのAI機能（GPT画像生成、Doubao画像/動画生成、Kimi/Doubao/Deepseek AI検索）を提供します。

## RedFoxHubを選ぶ理由

<p align="center"><em>期間限定均一価格、最低 <strong style="color:#e53e3e">¥0.02/回</strong></em></p>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <b>⚡ 高速レスポンス</b><br>
      <sub>ミリ秒単位のAPIレスポンス、グローバルCDN加速で瞬時のパフォーマンス</sub>
    </td>
    <td align="center" width="25%">
      <b>🛡️ 安全・信頼性</b><br>
      <sub>エンタープライズ級セキュリティ、暗号化転送、99.99%の可用性保証</sub>
    </td>
    <td align="center" width="25%">
      <b>🌍 グローバルカバレッジ</b><br>
      <sub>世界の主要ニューメディアプラットフォームに対応、ワンクリックでマルチプラットフォーム接続</sub>
    </td>
    <td align="center" width="25%">
      <b>💎 柔軟な課金</b><br>
      <sub>従量課金制、隠れた費用なし、あらゆる規模に対応する柔軟なプラン</sub>
    </td>
  </tr>
</table>

## SDK 主な機能

- **ゼロ設定** — 環境変数 `REDFOX_API_KEY` を設定するだけ。フラットなパラメータ、設定オブジェクト不要。
- **指数バックオフリトライ** — ネットワークタイムアウト、サーバー5xx、レート制限429でジッター付き自動リトライ。
- **同期 + 非同期デュアルクライアント** — `RedFoxClient` と `AsyncRedFoxClient`、完全同一API。
- **構造化例外** — `RedFoxAuthError` / `RedFoxRateLimitError` / `RedFoxAPIError`、完全なデバッグコンテキスト付き。
- **プロダクション対応** — `httpx` ベース、コネクションプーリング、タイムアウト制御、コンテキストマネージャ対応。

## インストール

```bash
pip install redfox-python-sdk
```

## 認証

### APIキーの取得

1. [https://redfox.hk/settings/api-keys?source=github](https://redfox.hk/settings/api-keys?source=github) で登録 / ログインします。
2. コンソールでAPIキーをコピーします。
3. 環境変数として設定するか、直接渡します：

```bash
export REDFOX_API_KEY="YOUR_API_KEY"
```

## マルチプラットフォームAPIドキュメント

<p align="center">
  <a href="https://redfox.hk/apis?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-1.png" alt="RedFox API Docs" width="100%">
  </a>
</p>

### APIドキュメントの内容:

- リクエストヘッダーの説明
- リクエストパラメータの説明
- レスポンスフィールドとデータ構造
- リクエスト例
- レスポンス例
- 一般的なステータスコード

## クイックスタート

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# 抖音のコンテンツ検索
result = client.douyin.search_articles(keyword="AI")

# 小紅書のノート検索
result = client.xiaohongshu.search_articles(keyword="旅行")

# WeChat公衆号の記事検索
result = client.wechat.search_articles(keyword="テクノロジー")

# 抖音ユーザープロフィール取得
result = client.douyin.get_user(account_id="nxpt260212")

# AI検索
task = client.ai_search.kimi_submit(inquiry_text="2026年AI発展トレンド")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## 対応プラットフォーム

| プラットフォーム | モジュール | メソッド数 | 説明 |
|----------|--------|---------|-------------|
| 📱 抖音 | `client.douyin` | 6 | コンテンツ/ユーザー検索、ユーザー情報、コンテンツ詳細、AIコンテンツ検索 |
| 📕 小紅書 | `client.xiaohongshu` | 5 | ノート/ユーザー検索、アカウント情報、ノート詳細、AIノート検索 |
| 💬 WeChat | `client.wechat` | 7 | 記事/アカウント検索、アカウント情報、記事詳細、AI記事検索 |
| 📺 Bilibili | `client.bilibili` | 5 | 動画/クリエイター検索、クリエイター情報、動画一覧、動画詳細 |
| 📰 今日頭条 | `client.toutiao` | 2 | コンテンツ検索、コンテンツ詳細 |
| 🎵 TikTok | `client.tiktok` | 1 | ユーザー検索 |
| 🖼️ GPT画像 | `client.gpt_image` | 2 | 画像生成と結果照会 |
| 🎨 Doubao画像 | `client.doubao_image` | 4 | Pro/Lite画像生成と照会 |
| 🎬 Doubao動画 | `client.doubao_video` | 2 | 動画生成と結果照会 |
| 🔍 AI検索 | `client.ai_search` | 6 | Kimi/Doubao/Deepseek検索 |

## APIリファレンス

### 抖音

```python
# 動画検索
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# ユーザー検索
client.douyin.search_users(keyword="テクノロジー", offset=0)

# ユーザープロフィール取得
client.douyin.get_user(account_id="nxpt260212")

# ユーザー動画一覧取得
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# 動画詳細取得
client.douyin.get_work(work_id="7654143095876898089")

# AI動画検索
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### 小紅書

```python
# ノート検索
client.xiaohongshu.search_articles(keyword="旅行", offset=0, sort_type="0")

# クリエイター検索
client.xiaohongshu.search_users(keyword="旅行", offset=0)

# クリエイタープロフィール取得
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# ノート詳細取得
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# AIノート検索
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### WeChat公衆号

```python
# 記事検索
client.wechat.search_articles(keyword="AI", offset=0)

# アカウント検索
client.wechat.search_users(keyword="テクノロジー", offset=0)

# アカウント情報取得
client.wechat.get_account(account="rmrbwx")

# 記事詳細取得（全文コンテンツ）
client.wechat.get_article_detail(url="https://mp.weixin.qq.com/s/...")

# 記事メタデータ取得
client.wechat.get_work(work_uuid="3F4DE056583609162E0816FBE8C183A3")

# アカウント記事一覧取得
client.wechat.get_user_works(
    account="rmrbwx", offset=0,
    sort_type="_2",
    publish_time_start="2026-07-01",
    publish_time_end="2026-07-20"
)
```

### Bilibili

```python
# 動画検索
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# クリエイター検索
client.bilibili.search_users(keyword="テクノロジー", page=1, page_size=10, order="follower")

# クリエイタープロフィール取得
client.bilibili.get_account(mid="946974")

# クリエイター動画一覧取得
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# 動画詳細取得
client.bilibili.get_work(bvid="BV1ghJg6hEWV")
```

### 今日頭条

```python
# コンテンツ検索
client.toutiao.search_works(keyword="AI", offset=0)

# コンテンツ詳細取得
client.toutiao.get_work(opus_id="7592180245936046626")
```

### TikTok

```python
# ユーザー検索
client.tiktok.search_users(keyword="tech", cursor=0)
```

### AI検索

```python
# Kimi検索
task = client.ai_search.kimi_submit(inquiry_text="2026年AI発展トレンド")
result = client.ai_search.kimi_result(task_id=task["taskId"])

# Doubao検索
task = client.ai_search.doubao_submit(inquiry_text="夏のドリンクおすすめ")
result = client.ai_search.doubao_result(task_id=task["taskId"])

# Deepseek検索
task = client.ai_search.deepseek_submit(inquiry_text="Pythonパフォーマンス最適化")
result = client.ai_search.deepseek_result(task_id=task["taskId"])
```

### GPT画像生成

```python
# テキスト → 画像
task = client.gpt_image.submit(
    prompt="窓辺に座る日差しを浴びたオレンジ色の猫",
    size="1024x1024",
    quality="medium",
    output_format="png",
    model_name="gpt-image-2",
    operation="generate",
)
result = client.gpt_image.result(task_id=task["taskId"])

# 画像編集
task = client.gpt_image.submit(
    prompt="背景をビーチに変更",
    size="1024x1024",
    model_name="gpt-image-2",
    operation="edit",
    input_fidelity=5,
    images=[{"url": "https://example.com/your-image.jpg"}],
)
result = client.gpt_image.result(task_id=task["taskId"])
```

### Doubao画像生成

```python
# Proモデル
task = client.doubao_image.pro_submit(
    prompt="雲の上に浮かぶ未来都市",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    watermark=False,
)
result = client.doubao_image.pro_result(task_id=task["taskId"])

# Liteモデル（複数画像対応）
task = client.doubao_image.lite_submit(
    prompt="春夏秋冬の風景画",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    sequential="auto",
    max_images=4,
)
result = client.doubao_image.lite_result(task_id=task["taskId"])
```

### Doubao動画生成

```python
# テキスト → 動画
task = client.doubao_video.submit(
    content=[{"type": "text", "text": "日差しの中で欠伸をする猫、そよ風に揺れる毛並み"}],
    resolution="720p",
    ratio="16:9",
    duration=5,
    watermark=False,
    generate_audio=True,
)
result = client.doubao_video.result(task_id=task["taskId"])

# 画像 → 動画
task = client.doubao_video.submit(
    content=[
        {"type": "text", "text": "画像の人物が微笑んで手を振るように"},
        {"type": "image_url", "image_url": "https://example.com/photo.jpg"},
    ],
    resolution="720p",
    duration=5,
)
result = client.doubao_video.result(task_id=task["taskId"])
```

## エラーハンドリング

SDKは3種類の例外を提供します：

```python
from redfox import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

try:
    result = client.douyin.search_articles(keyword="AI")
except RedFoxAuthError as e:
    print(f"認証失敗: {e}")
except RedFoxRateLimitError as e:
    print(f"リクエスト制限超過: {e}")
except RedFoxAPIError as e:
    print(f"APIエラー: code={e.code}, msg={e}")
```

## 要件

- Python >= 3.8
- requests >= 2.25.0

## ライセンス

MIT License
