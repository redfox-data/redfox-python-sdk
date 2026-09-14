# RedFox Python SDK

<div align="center">
<a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/v/redfox-python-sdk.svg" alt="PyPI version"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/pyversions/redfox-python-sdk.svg" alt="Python"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/l/redfox-python-sdk.svg" alt="License"></a>

<a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.md">中文</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.en.md">English</a> | <strong>한국어</strong> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ja.md">日本語</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.fr.md">Français</a>

</div>
<p align="center">
  <a href="https://redfox.hk/?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-3.png" alt="RedFox" width="100%">
  </a>
</p>

[RedFoxHub](https://redfox.hk/?source=github) Python SDK — 14대 콘텐츠 플랫폼([더우인](https://redfox.hk/apis/douyin/0OT1E306), [샤오홍슈](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [위챗 공식 계정](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [빌리빌리](https://redfox.hk/apis/bilibili/TIN1NMTZ), [진르터우탸오](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019), 콰이쇼우, 위챗 채널스, YouTube, X (Twitter), Instagram, 둥처디, 이처, 오토홈)의 데이터 수집 API, 멀티 플랫폼 실시간 인기 순위 집계, 워터마크 제거 영상 다운로드 및 미디어 업로드 도구, 그리고 AI 기능(GPT 이미지 생성, Doubao 이미지/비디오 생성, Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu AI 검색)을 제공합니다.

## RedFoxHub를 선택해야 하는 이유

<p align="center"><em>기간 한정 균일 가격, 최저 <strong style="color:#e53e3e">¥0.02/회</strong></em></p>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <b>⚡ 초고속 응답</b><br>
      <sub>밀리초 단위 API 응답, 글로벌 CDN 가속으로 즉각적인 성능 제공</sub>
    </td>
    <td align="center" width="25%">
      <b>🛡️ 안전하고 신뢰성 있는</b><br>
      <sub>엔터프라이즈급 보안, 데이터 암호화 전송, 99.99% 가용성 보장</sub>
    </td>
    <td align="center" width="25%">
      <b>🌍 글로벌 커버리지</b><br>
      <sub>전 세계 주요 뉴미디어 플랫폼 지원, 원클릭 멀티 플랫폼 접근</sub>
    </td>
    <td align="center" width="25%">
      <b>💎 유연한 과금</b><br>
      <sub>사용량 기반 과금, 숨겨진 비용 없음, 모든 규모에 맞는 유연한 플랜</sub>
    </td>
  </tr>
</table>

## SDK 핵심 기능

- **제로 구성** — `REDFOX_API_KEY` 환경 변수 설정만으로 사용 가능. 평면 파라미터, 구성 객체 불필요.
- **지수 백오프 재시도** — 네트워크 타임아웃, 서버 5xx, 속도 제한 429에서 지터 포함 자동 재시도.
- **동기 + 비동기 듀얼 클라이언트** — `RedFoxClient`와 `AsyncRedFoxClient`, 완전히 동일한 API.
- **파일 업로드** — multipart 업로드 내장, 파일 경로 / bytes / 파일 객체 지원.
- **구조화된 예외** — `RedFoxAuthError` / `RedFoxRateLimitError` / `RedFoxAPIError`, 전체 디버그 컨텍스트 포함.
- **프로덕션 준비 완료** — `httpx` 기반, 커넥션 풀링, 타임아웃 제어, 컨텍스트 매니저 지원.

## 설치

```bash
pip install redfox-python-sdk
```

## 인증

### API Key 발급받기

1. [https://redfox.hk/settings/api-keys?source=github](https://redfox.hk/settings/api-keys?source=github) 에서 회원가입 / 로그인하세요.
2. 콘솔에서 API Key를 복사하세요.
3. 환경 변수로 설정하거나 직접 전달하세요:

```bash
export REDFOX_API_KEY="YOUR_API_KEY"
```

## 멀티 플랫폼 API 문서

<p align="center">
  <a href="https://redfox.hk/apis?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-1.png" alt="RedFox API Docs" width="100%">
  </a>
</p>

### API 문서 포함 내용:

- 요청 헤더 설명
- 요청 파라미터 설명
- 응답 필드 및 데이터 구조
- 요청 예제
- 응답 예제
- 일반 상태 코드

## 빠른 시작

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# 더우인 콘텐츠 검색
result = client.douyin.search_articles(keyword="AI")

# 샤오홍슈 노트 검색
result = client.xiaohongshu.search_articles(keyword="여행")

# 위챗 공식 계정 글 검색
result = client.wechat.search_articles(keyword="기술")

# 콰이쇼우 콘텐츠 검색
result = client.kuaishou.search_works(keyword="음식")

# YouTube 비디오 검색
result = client.youtube.search_videos(search_query="AI tutorial")

# 전 플랫폼 통합 인기 TOP10
result = client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)

# 워터마크 제거 영상 다운로드
result = client.tools.download(url="https://www.douyin.com/video/xxx")

# AI 검색
task = client.ai_search.kimi_submit(inquiry_text="2026년 AI 발전 트렌드")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## 지원 플랫폼

| 플랫폼 | 모듈 | 메서드 수 | 설명 |
|----------|--------|---------|-------------|
| 📱 더우인 | `client.douyin` | 16 | 콘텐츠/사용자 검색(프리미엄+광역), 사용자 정보, 콘텐츠 상세, AI 콘텐츠 검색, 인기/급상승 순위, 인기 계정, 영상 텍스트 추출 |
| 📕 샤오홍슈 | `client.xiaohongshu` | 15 | 노트/사용자 검색, 계정 정보, 노트 상세, 노트 목록, AI 노트 검색, 댓글, 일간/주간/다크호스 순위, 인기 계정, 인기 노트 인사이트, 영상 텍스트 추출 |
| 💬 위챗 | `client.wechat` | 16 | 글/계정 검색(프리미엄+광역), 계정 정보, 글 상세, 글 목록, AI 글 검색, 10만+ 읽기/오리지널/종합/성장 순위 |
| 📺 빌리빌리 | `client.bilibili` | 8 | 비디오/크리에이터 검색, 크리에이터 정보, 비디오 목록, 비디오 상세, 오디오 추출, 영상 텍스트 추출 |
| 📰 진르터우탸오 | `client.toutiao` | 5 | 콘텐츠 검색, 콘텐츠 상세, 댓글, 계정 검색, 계정 콘텐츠 목록 |
| 🎵 TikTok | `client.tiktok` | 4 | 사용자 검색, 비디오 검색, 비디오 상세, 사용자 비디오 목록 |
| 🎬 콰이쇼우 | `client.kuaishou` | 6 | 콘텐츠 검색, 콘텐츠 상세, 계정 콘텐츠, 계정 검색, 영상 텍스트 추출 |
| 💚 위챗 채널스 | `client.wechat_channels` | 7 | 콘텐츠 검색, 콘텐츠 상세, 계정 콘텐츠, 링크 실시간 상세, 계정 검색, 링크 텍스트 추출 |
| ▶️ YouTube | `client.youtube` | 4 | 비디오 검색, 비디오 상세, 비디오 댓글, 영상 텍스트 추출(자막) |
| 🐦 X (Twitter) | `client.twitter` | 4 | 트윗 검색, 트윗 상세, 사용자 정보, 트윗 댓글 |
| 📸 Instagram | `client.instagram` | 4 | 통합 검색, 게시물 상세, 게시물 댓글, 사용자 정보 |
| 🚗 둥처디 | `client.dongchedi` | 4 | 콘텐츠 검색, 콘텐츠 상세, 사용자 콘텐츠, 사용자 검색 |
| 🚙 이처 | `client.yiche` | 5 | 콘텐츠 검색, 글 상세, 비디오 상세, 계정 콘텐츠, 계정 검색 |
| 🚘 오토홈 | `client.autohome` | 4 | 콘텐츠 검색, 글 상세, 비디오 상세, 계정 콘텐츠 |
| 🔥 인기 순위 | `client.hotspot` | 3 | 플랫폼별 인기 순위, 전 플랫폼 키워드 검색, 통합 인기 TOP10 |
| 🖼️ GPT 이미지 | `client.gpt_image` | 2 | 이미지 생성 및 결과 조회 |
| 🎨 Doubao 이미지 | `client.doubao_image` | 4 | Pro/Lite 이미지 생성 및 조회 |
| 🎬 Doubao 비디오 | `client.doubao_video` | 2 | 비디오 생성 및 결과 조회 |
| 🔍 AI 검색 | `client.ai_search` | 12 | Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu 검색 |
| 🛠️ 도구 | `client.tools` | 12 | 멀티 플랫폼 워터마크 제거 영상 다운로드, 이미지/미디어 업로드 |

## API 레퍼런스

### 더우인

```python
# 비디오 검색 (프리미엄)
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# 사용자 검색 (프리미엄)
client.douyin.search_users(keyword="기술", offset=0)

# 사용자 프로필 조회
client.douyin.get_user(account_id="nxpt260212")

# 사용자 비디오 목록 조회
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# 비디오 상세 조회 (work_id 또는 work_url)
client.douyin.get_work(work_id="7654143095876898089")

# AI 비디오 검색
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── 광역 커버리지 ───
client.douyin.search_works_wide(keyword="AI", start_date="2026-08-01", end_date="2026-08-20")
client.douyin.search_accounts_wide(keyword="기술")
client.douyin.get_work_wide(video_id="7654143095876898089")
client.douyin.get_user_works_wide(unique_name="nxpt260212")

# ─── 순위 ───
client.douyin.get_daily_hot_rank(type="美食")                          # 일간 인기 콘텐츠
client.douyin.get_daily_surge_rank(type="全部")                        # 일간 좋아요 급상승
client.douyin.get_weekly_surge_rank(type="全部")                       # 주간 좋아요 급상승
client.douyin.get_hot_accounts(date_type="days", rank_date="2026-08-20", type="全部")

# ─── 영상 텍스트 추출 ───
task = client.douyin.transcript_submit(url="https://www.douyin.com/video/xxx")
result = client.douyin.transcript_result(task_id=task["taskId"])
```

### 샤오홍슈

```python
# 노트 검색
client.xiaohongshu.search_articles(keyword="여행", offset=0, sort_type="0")

# 크리에이터 검색
client.xiaohongshu.search_users(keyword="여행", offset=0)

# 크리에이터 프로필 조회
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# 노트 상세 조회 (work_id 또는 work_link)
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# 크리에이터 노트 목록 조회
client.xiaohongshu.get_user_works(red_id="nxpt260212", offset=0)

# AI 노트 검색
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── 댓글 ───
task = client.xiaohongshu.comment_submit(opus_id="6a2ac3020000000035022d8e", data_num=-1)
result = client.xiaohongshu.comment_result(task_id=task["taskId"])

# ─── 순위 / 인사이트 ───
client.xiaohongshu.get_daily_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_weekly_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_hot_accounts(date_type=1, rank_date="2026-08-20", type="综合全部")
client.xiaohongshu.search_hot_notes(keyword="穿搭", start_date="2026-08-01", end_date="2026-08-20")
client.xiaohongshu.get_dark_horse_notes(keyword="AI,穿搭", start_date="2026-08-01")

# ─── 영상 텍스트 추출 ───
task = client.xiaohongshu.transcript_submit(url="https://www.xiaohongshu.com/explore/xxx")
result = client.xiaohongshu.transcript_result(task_id=task["taskId"])
```

### 위챗 공식 계정

```python
# 글 검색
client.wechat.search_articles(keyword="AI", offset=0)

# 계정 검색
client.wechat.search_users(keyword="기술", offset=0)

# 계정 정보 조회
client.wechat.get_account(account="rmrbwx")

# 글 상세 조회 (전체 콘텐츠)
client.wechat.get_article_detail(url="https://mp.weixin.qq.com/s/...")

# 글 메타데이터 조회
client.wechat.get_work(work_uuid="3F4DE056583609162E0816FBE8C183A3")

# 계정 글 목록 조회
client.wechat.get_user_works(
    account="rmrbwx", offset=0,
    sort_type="_2",
    publish_time_start="2026-07-01",
    publish_time_end="2026-07-20"
)

# AI 글 검색
client.wechat.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── 광역 커버리지 ───
client.wechat.search_articles_wide(keyword="AI", offset=0)
client.wechat.search_users_wide(keyword="기술")
client.wechat.get_work_wide(work_uuid="3F4DE056583609162E0816FBE8C183A3")
client.wechat.get_user_works_wide(account="rmrbwx")
client.wechat.get_account_wide(wx_id="gh_5c7e8b7f586b")

# ─── 순위 ───
client.wechat.get_ten_w_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_original_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_strength_rank(rank_type="day", rank_date="2026-08-20", category="科技数码")
client.wechat.get_reading_growth_rank(rank_date="2026-08-20")
```

### 위챗 채널스

```python
# 콘텐츠 검색
client.wechat_channels.search_works(keyword="여행", sort="综合", page=1, size=20)

# 콘텐츠 상세 조회
client.wechat_channels.get_work(video_id="export/UzFfAgtgekIEAQAAAAAAxx8")

# 계정 콘텐츠 목록 (닉네임 정확 일치)
client.wechat_channels.get_user_works(nickname="央视新闻", page=1)

# 링크 실시간 상세 조회
client.wechat_channels.get_work_by_link(url="https://weixin.qq.com/sph/xxx")

# 계정 검색
client.wechat_channels.search_users(account_name="央视", page=1)

# 링크 텍스트 추출
task = client.wechat_channels.transcript_submit(url="https://weixin.qq.com/sph/xxx")
result = client.wechat_channels.transcript_result(task_id=task["taskId"])
```

### 빌리빌리

```python
# 비디오 검색
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# 크리에이터 검색
client.bilibili.search_users(keyword="기술", page=1, page_size=10, order="follower")

# 크리에이터 프로필 조회
client.bilibili.get_account(mid="946974")

# 크리에이터 비디오 목록 조회 (mid 또는 account_url)
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# 비디오 상세 조회 (bvid 또는 work_url)
client.bilibili.get_work(bvid="BV1ghJg6hEWV")

# 비디오 오디오 주소 조회
client.bilibili.get_audio(url="https://www.bilibili.com/video/BV1ghJg6hEWV")

# 영상 텍스트 추출
task = client.bilibili.transcript_submit(url="https://www.bilibili.com/video/BV1ghJg6hEWV")
result = client.bilibili.transcript_result(task_id=task["taskId"])
```

### 진르터우탸오

```python
# 콘텐츠 검색
client.toutiao.search_works(keyword="AI", offset=0)

# 콘텐츠 상세 조회
client.toutiao.get_work(opus_id="7592180245936046626")

# 콘텐츠 댓글 조회
client.toutiao.get_comments(opus_id="7592180245936046626")

# 계정 검색
client.toutiao.search_users(name="기술")

# 계정 콘텐츠 목록 조회
client.toutiao.get_user_works(category="profile_all", token="MS4wLjABAAAA...")
```

### 콰이쇼우

```python
# 콘텐츠 검색
client.kuaishou.search_works(keyword="음식", page=1, size=20, sort="综合")

# 콘텐츠 상세 조회
client.kuaishou.get_work(photo_id="3x9sm2nqxmbfbuq")

# 계정 콘텐츠 목록 (kwai_id / three_x_id 중 하나)
client.kuaishou.get_user_works(three_x_id="3x4wxhrrzefrq4y", page=1)

# 계정 검색
client.kuaishou.search_users(account_name="王刚", page=1)

# 영상 텍스트 추출
task = client.kuaishou.transcript_submit(url="https://www.kuaishou.com/short-video/xxx")
result = client.kuaishou.transcript_result(task_id=task["taskId"])
```

### TikTok

```python
# 사용자 검색
client.tiktok.search_users(keyword="tech", cursor=0)

# 비디오 검색
client.tiktok.search_videos(keyword="AI", count="20", sort_type="0", region="US")

# 비디오 상세 조회
client.tiktok.get_work(aweme_id="7532000000000000000")

# 사용자 비디오 목록 조회
client.tiktok.get_user_works(sec_user_id="MS4wLjABAAAA...")
```

### YouTube

```python
# 비디오 검색
client.youtube.search_videos(search_query="AI tutorial")

# 비디오 상세 조회
client.youtube.get_video(video_id="sa8AzBK4dao")

# 비디오 댓글 조회
client.youtube.get_comments(video_id="sa8AzBK4dao", sort_by="top")

# 영상 텍스트 추출 (자막/음성)
client.youtube.get_transcript(video_url="https://www.youtube.com/watch?v=sa8AzBK4dao")
```

### X (Twitter)

```python
# 트윗 검색
client.twitter.search_tweets(keyword="AI", search_type="Top")

# 트윗 상세 조회
client.twitter.get_tweet(tweet_id="1957000000000000000")

# 사용자 정보 조회 (screen_name / rest_id 중 하나 이상)
client.twitter.get_user(screen_name="elonmusk")

# 트윗 댓글 조회
client.twitter.get_comments(tweet_id="1957000000000000000")
```

### Instagram

```python
# 통합 검색
client.instagram.search(keyword="travel")

# 게시물 상세 조회 (Shortcode 또는 전체 URL)
client.instagram.get_post(code_or_url="DRhvwVLAHAG")

# 게시물 댓글 조회
client.instagram.get_comments(code_or_url="DRhvwVLAHAG", sort_by="recent")

# 사용자 정보 조회 (username / user_id 중 하나 이상)
client.instagram.get_user(username="natgeo")
```

### 둥처디

```python
# 콘텐츠 검색
client.dongchedi.search_works(keyword="小米SU7", offset="0", source_type="1")

# 콘텐츠 상세 조회
client.dongchedi.get_work(work_id="7532000000000000000", work_type="video")

# 사용자 콘텐츠 목록 조회
client.dongchedi.get_user_works(user_id="60480000000000000", cursor=0)

# 사용자 검색
client.dongchedi.search_users(keyword="陈震", offset=0)
```

### 이처

```python
# 콘텐츠 검색 (club=커뮤니티 / shipin=비디오 / xinwen=글)
client.yiche.search_works(keyword="小米SU7", page=1, source_type="xinwen")

# 글 상세 조회
client.yiche.get_article(url="https://news.yiche.com/hao/wenzhang/xxx.html")

# 비디오 상세 조회
client.yiche.get_video(work_id="50000000")

# 계정 콘텐츠 목록 조회
client.yiche.get_user_works(user_id="600000000")

# 계정 검색
client.yiche.search_users(keyword="陈震", page=1)
```

### 오토홈

```python
# 콘텐츠 검색 (club / article / video)
client.autohome.search_works(keyword="小米SU7", source_type="video")

# 글 상세 조회 (처자하오)
client.autohome.get_article(work_id="3000000")

# 비디오 상세 조회 (0=오리지널 계정, 4=처자하오)
client.autohome.get_video(video_id="5000000", video_type=4)

# 계정 콘텐츠 목록 조회
client.autohome.get_user_works(author_id="7000000", page=0)
```

### 인기 순위

```python
# 플랫폼별 인기 순위: 1=콰이쇼우 2=더우인 5=웨이보 6=샤오홍슈 7=바이두 8=빌리빌리 9=즈후 10=진르터우탸오
client.hotspot.get_platform_rank(
    platform=2,
    start_date="2026-08-20",
    end_date="2026-08-21",
)

# 전 플랫폼 키워드 인기 검색 (최대 30일 범위)
client.hotspot.search_by_keywords(
    keywords=["삼성"],
    start_date="2026-08-01",
    end_date="2026-08-21",
    platforms=[2, 5, 10],
)

# 전 플랫폼 통합 인기 TOP10
client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)
```

### 도구

```python
# 통합 영상 다운로더 (플랫폼 자동 감지)
client.tools.download(url="https://www.douyin.com/video/xxx")

# 플랫폼별 워터마크 제거 다운로드
client.tools.download_douyin(url="https://www.douyin.com/video/xxx")
client.tools.download_kuaishou(url="https://www.kuaishou.com/short-video/xxx")
client.tools.download_xiaohongshu(url="https://www.xiaohongshu.com/explore/xxx")
client.tools.download_bilibili(url="https://www.bilibili.com/video/BV1xxx")
client.tools.download_wechat_channels(url="https://weixin.qq.com/sph/xxx")
client.tools.download_tiktok(url="https://www.tiktok.com/@user/video/xxx")
client.tools.download_youtube(url="https://www.youtube.com/watch?v=xxx")
client.tools.download_instagram(url="https://www.instagram.com/reel/xxx")
client.tools.download_twitter(url="https://x.com/user/status/xxx")

# 이미지 업로드 (png / jpeg / webp)
client.tools.upload_image(file="./cover.png", format="png")

# 비디오/오디오/이미지 미디어 업로드
client.tools.upload_file(file="./clip.mp4", format="mp4")
```

### AI 검색

```python
# Kimi 검색
task = client.ai_search.kimi_submit(inquiry_text="2026년 AI 발전 트렌드")
result = client.ai_search.kimi_result(task_id=task["taskId"])

# Doubao 검색
task = client.ai_search.doubao_submit(inquiry_text="여름 음료 추천")
result = client.ai_search.doubao_result(task_id=task["taskId"])

# Deepseek 검색
task = client.ai_search.deepseek_submit(inquiry_text="Python 성능 최적화")
result = client.ai_search.deepseek_result(task_id=task["taskId"])

# Yuanbao 검색
task = client.ai_search.yuanbao_submit(inquiry_text="전기차 추천")
result = client.ai_search.yuanbao_result(task_id=task["taskId"])

# Qianwen 검색
task = client.ai_search.qianwen_submit(inquiry_text="항저우 여행 가이드")
result = client.ai_search.qianwen_result(task_id=task["taskId"])

# Baidu 검색
task = client.ai_search.baidu_submit(inquiry_text="오늘의 경제 뉴스")
result = client.ai_search.baidu_result(task_id=task["taskId"])
```

### GPT 이미지 생성

```python
# 텍스트 → 이미지
task = client.gpt_image.submit(
    prompt="햇살 아래 창틀에 앉아 있는 주황색 고양이",
    resolution="1k",   # 1k / 2k / 4k
    size="1:1",        # 가로세로 비율 (1:1, 16:9, 9:16 등 13종)
    n=1,               # 생성 개수, 최대 4
)
result = client.gpt_image.result(task_id=task["taskId"])
print(result["status"], result["imageUrls"])

# 이미지 편집
task = client.gpt_image.submit(
    prompt="배경을 해변으로 변경",
    resolution="2k",
    size="16:9",
    n=2,
    reference_images=["https://example.com/your-image.jpg"],  # 참조 이미지 URL, 최대 2장
)
result = client.gpt_image.result(task_id=task["taskId"])
```

> **참고**: `result()`가 반환하는 `imageUrls`는 몇 분 후 만료되어 404가 되므로 즉시 다운로드하세요. `status`는 `queued`/`in_progress`/`completed`/`failed` 중 하나이며 종료 상태는 뒤의 둘뿐입니다. 생성된 이미지를 참조 이미지로 쓰려면 만료 전에 제출하세요.

### Doubao 이미지 생성

```python
# Pro 모델
task = client.doubao_image.pro_submit(
    prompt="구름 위에 떠 있는 미래 도시",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    watermark=False,
)
result = client.doubao_image.pro_result(task_id=task["taskId"])

# Lite 모델 (멀티 이미지 지원)
task = client.doubao_image.lite_submit(
    prompt="사계절 풍경화",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    sequential="auto",
    max_images=4,
)
result = client.doubao_image.lite_result(task_id=task["taskId"])
```

### Doubao 비디오 생성

```python
# 텍스트 → 비디오
task = client.doubao_video.submit(
    content=[{"type": "text", "text": "햇살 아래 하품하는 고양이, 바람에 살랑이는 털"}],
    resolution="720p",
    ratio="16:9",
    duration=5,
    watermark=False,
    generate_audio=True,
)
result = client.doubao_video.result(task_id=task["taskId"])

# 이미지 → 비디오
task = client.doubao_video.submit(
    content=[
        {"type": "text", "text": "이미지 속 인물이 미소 지으며 손을 흔들도록"},
        {"type": "image_url", "image_url": "https://example.com/photo.jpg"},
    ],
    resolution="720p",
    duration=5,
)
result = client.doubao_video.result(task_id=task["taskId"])
```

## 오류 처리

SDK는 세 가지 예외 유형을 제공합니다:

```python
from redfox import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

try:
    result = client.douyin.search_articles(keyword="AI")
except RedFoxAuthError as e:
    print(f"인증 실패: {e}")
except RedFoxRateLimitError as e:
    print(f"요청 한도 초과: {e}")
except RedFoxAPIError as e:
    print(f"API 오류: code={e.code}, msg={e}")
```

## 요구 사항

- Python >= 3.8
- httpx >= 0.25.0

## 라이선스

MIT License
