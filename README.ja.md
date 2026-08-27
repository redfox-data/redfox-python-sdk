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

[RedFoxHub](https://redfox.hk/?source=github) Python SDK。14大コンテンツプラットフォーム（[抖音](https://redfox.hk/apis/douyin/0OT1E306)、[小紅書](https://redfox.hk/apis/xiaohongshu/4IVIDHEN)、[WeChat公衆号](https://redfox.hk/apis/gongzhonghao/6C4A77XR)、[Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ)、[今日頭条](https://redfox.hk/apis/jinritoutiao/28CFGF5I)、[TikTok](https://redfox.hk/apis/tool-tiktok/20070019)、快手、WeChatチャンネル、YouTube、X (Twitter)、Instagram、懂車帝、易車、汽車之家）のデータ取得API、マルチプラットフォーム急上昇ランキング集約、透かし除去動画ダウンロード・メディアアップロードツール、およびAI機能（GPT画像生成、Doubao画像/動画生成、Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu AI検索）を提供します。

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
- **ファイルアップロード** — multipartアップロード内蔵、ファイルパス / bytes / ファイルオブジェクト対応。
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

# 快手のコンテンツ検索
result = client.kuaishou.search_works(keyword="グルメ")

# YouTubeの動画検索
result = client.youtube.search_videos(search_query="AI tutorial")

# 全プラットフォーム統合急上昇TOP10
result = client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)

# 透かし除去動画ダウンロード
result = client.tools.download(url="https://www.douyin.com/video/xxx")

# AI検索
task = client.ai_search.kimi_submit(inquiry_text="2026年AI発展トレンド")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## 対応プラットフォーム

| プラットフォーム | モジュール | メソッド数 | 説明 |
|----------|--------|---------|-------------|
| 📱 抖音 | `client.douyin` | 16 | コンテンツ/ユーザー検索（プレミアム+広域）、ユーザー情報、コンテンツ詳細、AIコンテンツ検索、人気/急上昇ランキング、人気アカウント、動画テキスト抽出 |
| 📕 小紅書 | `client.xiaohongshu` | 15 | ノート/ユーザー検索、アカウント情報、ノート詳細、ノート一覧、AIノート検索、コメント、デイリー/ウィークリー/ダークホースランキング、人気アカウント、人気ノートインサイト、動画テキスト抽出 |
| 💬 WeChat | `client.wechat` | 16 | 記事/アカウント検索（プレミアム+広域）、アカウント情報、記事詳細、記事一覧、AI記事検索、10万+読了/オリジナル/総合/成長ランキング |
| 📺 Bilibili | `client.bilibili` | 8 | 動画/クリエイター検索、クリエイター情報、動画一覧、動画詳細、音声抽出、動画テキスト抽出 |
| 📰 今日頭条 | `client.toutiao` | 5 | コンテンツ検索、コンテンツ詳細、コメント、アカウント検索、アカウントコンテンツ一覧 |
| 🎵 TikTok | `client.tiktok` | 4 | ユーザー検索、動画検索、動画詳細、ユーザー動画一覧 |
| 🎬 快手 | `client.kuaishou` | 6 | コンテンツ検索、コンテンツ詳細、アカウントコンテンツ、アカウント検索、動画テキスト抽出 |
| 💚 WeChatチャンネル | `client.wechat_channels` | 7 | コンテンツ検索、コンテンツ詳細、アカウントコンテンツ、リンクリアルタイム詳細、アカウント検索、リンクテキスト抽出 |
| ▶️ YouTube | `client.youtube` | 4 | 動画検索、動画詳細、動画コメント、動画テキスト抽出（字幕） |
| 🐦 X (Twitter) | `client.twitter` | 4 | ツイート検索、ツイート詳細、ユーザー情報、ツイートコメント |
| 📸 Instagram | `client.instagram` | 4 | 総合検索、投稿詳細、投稿コメント、ユーザー情報 |
| 🚗 懂車帝 | `client.dongchedi` | 4 | コンテンツ検索、コンテンツ詳細、ユーザーコンテンツ、ユーザー検索 |
| 🚙 易車 | `client.yiche` | 5 | コンテンツ検索、記事詳細、動画詳細、アカウントコンテンツ、アカウント検索 |
| 🚘 汽車之家 | `client.autohome` | 4 | コンテンツ検索、記事詳細、動画詳細、アカウントコンテンツ |
| 🔥 急上昇ランキング | `client.hotspot` | 3 | プラットフォーム別急上昇ランキング、全プラットフォームキーワード検索、統合急上昇TOP10 |
| 🖼️ GPT画像 | `client.gpt_image` | 2 | 画像生成と結果照会 |
| 🎨 Doubao画像 | `client.doubao_image` | 4 | Pro/Lite画像生成と照会 |
| 🎬 Doubao動画 | `client.doubao_video` | 2 | 動画生成と結果照会 |
| 🔍 AI検索 | `client.ai_search` | 12 | Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu検索 |
| 🛠️ ツール | `client.tools` | 12 | マルチプラットフォーム透かし除去動画ダウンロード、画像/メディアアップロード |

## APIリファレンス

### 抖音

```python
# 動画検索（プレミアム）
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# ユーザー検索（プレミアム）
client.douyin.search_users(keyword="テクノロジー", offset=0)

# ユーザープロフィール取得
client.douyin.get_user(account_id="nxpt260212")

# ユーザー動画一覧取得
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# 動画詳細取得（work_id または work_url）
client.douyin.get_work(work_id="7654143095876898089")

# AI動画検索
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── 広域カバレッジ ───
client.douyin.search_works_wide(keyword="AI", start_date="2026-08-01", end_date="2026-08-20")
client.douyin.search_accounts_wide(keyword="テクノロジー")
client.douyin.get_work_wide(video_id="7654143095876898089")
client.douyin.get_user_works_wide(unique_name="nxpt260212")

# ─── ランキング ───
client.douyin.get_daily_hot_rank(type="美食")                          # デイリー人気コンテンツ
client.douyin.get_daily_surge_rank(type="全部")                        # デイリーいいね急上昇
client.douyin.get_weekly_surge_rank(type="全部")                       # ウィークリーいいね急上昇
client.douyin.get_hot_accounts(date_type="days", rank_date="2026-08-20", type="全部")

# ─── 動画テキスト抽出 ───
task = client.douyin.transcript_submit(url="https://www.douyin.com/video/xxx")
result = client.douyin.transcript_result(task_id=task["taskId"])
```

### 小紅書

```python
# ノート検索
client.xiaohongshu.search_articles(keyword="旅行", offset=0, sort_type="0")

# クリエイター検索
client.xiaohongshu.search_users(keyword="旅行", offset=0)

# クリエイタープロフィール取得
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# ノート詳細取得（work_id または work_link）
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# クリエイターノート一覧取得
client.xiaohongshu.get_user_works(red_id="nxpt260212", offset=0)

# AIノート検索
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── コメント ───
task = client.xiaohongshu.comment_submit(opus_id="6a2ac3020000000035022d8e", data_num=-1)
result = client.xiaohongshu.comment_result(task_id=task["taskId"])

# ─── ランキング / インサイト ───
client.xiaohongshu.get_daily_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_weekly_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_hot_accounts(date_type=1, rank_date="2026-08-20", type="综合全部")
client.xiaohongshu.search_hot_notes(keyword="穿搭", start_date="2026-08-01", end_date="2026-08-20")
client.xiaohongshu.get_dark_horse_notes(keyword="AI,穿搭", start_date="2026-08-01")

# ─── 動画テキスト抽出 ───
task = client.xiaohongshu.transcript_submit(url="https://www.xiaohongshu.com/explore/xxx")
result = client.xiaohongshu.transcript_result(task_id=task["taskId"])
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

# AI記事検索
client.wechat.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── 広域カバレッジ ───
client.wechat.search_articles_wide(keyword="AI", offset=0)
client.wechat.search_users_wide(keyword="テクノロジー")
client.wechat.get_work_wide(work_uuid="3F4DE056583609162E0816FBE8C183A3")
client.wechat.get_user_works_wide(account="rmrbwx")
client.wechat.get_account_wide(wx_id="gh_5c7e8b7f586b")

# ─── ランキング ───
client.wechat.get_ten_w_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_original_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_strength_rank(rank_type="day", rank_date="2026-08-20", category="科技数码")
client.wechat.get_reading_growth_rank(rank_date="2026-08-20")
```

### WeChatチャンネル

```python
# コンテンツ検索
client.wechat_channels.search_works(keyword="旅行", sort="综合", page=1, size=20)

# コンテンツ詳細取得
client.wechat_channels.get_work(video_id="export/UzFfAgtgekIEAQAAAAAAxx8")

# アカウントコンテンツ一覧（ニックネーム完全一致）
client.wechat_channels.get_user_works(nickname="央视新闻", page=1)

# リンクリアルタイム詳細取得
client.wechat_channels.get_work_by_link(url="https://weixin.qq.com/sph/xxx")

# アカウント検索
client.wechat_channels.search_users(account_name="央视", page=1)

# リンクテキスト抽出
task = client.wechat_channels.transcript_submit(url="https://weixin.qq.com/sph/xxx")
result = client.wechat_channels.transcript_result(task_id=task["taskId"])
```

### Bilibili

```python
# 動画検索
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# クリエイター検索
client.bilibili.search_users(keyword="テクノロジー", page=1, page_size=10, order="follower")

# クリエイタープロフィール取得
client.bilibili.get_account(mid="946974")

# クリエイター動画一覧取得（mid または account_url）
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# 動画詳細取得（bvid または work_url）
client.bilibili.get_work(bvid="BV1ghJg6hEWV")

# 動画の音声URL取得
client.bilibili.get_audio(url="https://www.bilibili.com/video/BV1ghJg6hEWV")

# 動画テキスト抽出
task = client.bilibili.transcript_submit(url="https://www.bilibili.com/video/BV1ghJg6hEWV")
result = client.bilibili.transcript_result(task_id=task["taskId"])
```

### 今日頭条

```python
# コンテンツ検索
client.toutiao.search_works(keyword="AI", offset=0)

# コンテンツ詳細取得
client.toutiao.get_work(opus_id="7592180245936046626")

# コンテンツコメント取得
client.toutiao.get_comments(opus_id="7592180245936046626")

# アカウント検索
client.toutiao.search_users(name="テクノロジー")

# アカウントコンテンツ一覧取得
client.toutiao.get_user_works(category="profile_all", token="MS4wLjABAAAA...")
```

### 快手

```python
# コンテンツ検索
client.kuaishou.search_works(keyword="グルメ", page=1, size=20, sort="综合")

# コンテンツ詳細取得
client.kuaishou.get_work(photo_id="3x9sm2nqxmbfbuq")

# アカウントコンテンツ一覧（kwai_id / three_x_id のいずれか）
client.kuaishou.get_user_works(three_x_id="3x4wxhrrzefrq4y", page=1)

# アカウント検索
client.kuaishou.search_users(account_name="王刚", page=1)

# 動画テキスト抽出
task = client.kuaishou.transcript_submit(url="https://www.kuaishou.com/short-video/xxx")
result = client.kuaishou.transcript_result(task_id=task["taskId"])
```

### TikTok

```python
# ユーザー検索
client.tiktok.search_users(keyword="tech", cursor=0)

# 動画検索
client.tiktok.search_videos(keyword="AI", count="20", sort_type="0", region="US")

# 動画詳細取得
client.tiktok.get_work(aweme_id="7532000000000000000")

# ユーザー動画一覧取得
client.tiktok.get_user_works(sec_user_id="MS4wLjABAAAA...")
```

### YouTube

```python
# 動画検索
client.youtube.search_videos(search_query="AI tutorial")

# 動画詳細取得
client.youtube.get_video(video_id="sa8AzBK4dao")

# 動画コメント取得
client.youtube.get_comments(video_id="sa8AzBK4dao", sort_by="top")

# 動画テキスト抽出（字幕/音声）
client.youtube.get_transcript(video_url="https://www.youtube.com/watch?v=sa8AzBK4dao")
```

### X (Twitter)

```python
# ツイート検索
client.twitter.search_tweets(keyword="AI", search_type="Top")

# ツイート詳細取得
client.twitter.get_tweet(tweet_id="1957000000000000000")

# ユーザー情報取得（screen_name / rest_id のいずれか必須）
client.twitter.get_user(screen_name="elonmusk")

# ツイートコメント取得
client.twitter.get_comments(tweet_id="1957000000000000000")
```

### Instagram

```python
# 総合検索
client.instagram.search(keyword="travel")

# 投稿詳細取得（Shortcode または完全なURL）
client.instagram.get_post(code_or_url="DRhvwVLAHAG")

# 投稿コメント取得
client.instagram.get_comments(code_or_url="DRhvwVLAHAG", sort_by="recent")

# ユーザー情報取得（username / user_id のいずれか必須）
client.instagram.get_user(username="natgeo")
```

### 懂車帝

```python
# コンテンツ検索
client.dongchedi.search_works(keyword="小米SU7", offset="0", source_type="1")

# コンテンツ詳細取得
client.dongchedi.get_work(work_id="7532000000000000000", work_type="video")

# ユーザーコンテンツ一覧取得
client.dongchedi.get_user_works(user_id="60480000000000000", cursor=0)

# ユーザー検索
client.dongchedi.search_users(keyword="陈震", offset=0)
```

### 易車

```python
# コンテンツ検索（club=コミュニティ / shipin=動画 / xinwen=記事）
client.yiche.search_works(keyword="小米SU7", page=1, source_type="xinwen")

# 記事詳細取得
client.yiche.get_article(url="https://news.yiche.com/hao/wenzhang/xxx.html")

# 動画詳細取得
client.yiche.get_video(work_id="50000000")

# アカウントコンテンツ一覧取得
client.yiche.get_user_works(user_id="600000000")

# アカウント検索
client.yiche.search_users(keyword="陈震", page=1)
```

### 汽車之家

```python
# コンテンツ検索（club / article / video）
client.autohome.search_works(keyword="小米SU7", source_type="video")

# 記事詳細取得（車家号）
client.autohome.get_article(work_id="3000000")

# 動画詳細取得（0=オリジナルアカウント、4=車家号）
client.autohome.get_video(video_id="5000000", video_type=4)

# アカウントコンテンツ一覧取得
client.autohome.get_user_works(author_id="7000000", page=0)
```

### 急上昇ランキング

```python
# プラットフォーム別急上昇ランキング: 1=快手 2=抖音 5=微博 6=小紅書 7=百度 8=Bilibili 9=知乎 10=今日頭条
client.hotspot.get_platform_rank(
    platform=2,
    start_date="2026-08-20",
    end_date="2026-08-21",
)

# 全プラットフォームキーワード急上昇検索（最大30日範囲）
client.hotspot.search_by_keywords(
    keywords=["サムスン"],
    start_date="2026-08-01",
    end_date="2026-08-21",
    platforms=[2, 5, 10],
)

# 全プラットフォーム統合急上昇TOP10
client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)
```

### ツール

```python
# 統合動画ダウンローダー（プラットフォーム自動検出）
client.tools.download(url="https://www.douyin.com/video/xxx")

# プラットフォーム別透かし除去ダウンロード
client.tools.download_douyin(url="https://www.douyin.com/video/xxx")
client.tools.download_kuaishou(url="https://www.kuaishou.com/short-video/xxx")
client.tools.download_xiaohongshu(url="https://www.xiaohongshu.com/explore/xxx")
client.tools.download_bilibili(url="https://www.bilibili.com/video/BV1xxx")
client.tools.download_wechat_channels(url="https://weixin.qq.com/sph/xxx")
client.tools.download_tiktok(url="https://www.tiktok.com/@user/video/xxx")
client.tools.download_youtube(url="https://www.youtube.com/watch?v=xxx")
client.tools.download_instagram(url="https://www.instagram.com/reel/xxx")
client.tools.download_twitter(url="https://x.com/user/status/xxx")

# 画像アップロード（png / jpeg / webp）
client.tools.upload_image(file="./cover.png", format="png")

# 動画/音声/画像メディアアップロード
client.tools.upload_file(file="./clip.mp4", format="mp4")
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

# Yuanbao検索
task = client.ai_search.yuanbao_submit(inquiry_text="おすすめ電気自動車")
result = client.ai_search.yuanbao_result(task_id=task["taskId"])

# Qianwen検索
task = client.ai_search.qianwen_submit(inquiry_text="杭州旅行ガイド")
result = client.ai_search.qianwen_result(task_id=task["taskId"])

# Baidu検索
task = client.ai_search.baidu_submit(inquiry_text="今日の経済ニュース")
result = client.ai_search.baidu_result(task_id=task["taskId"])
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
- httpx >= 0.25.0

## ライセンス

MIT License
