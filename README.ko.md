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

[RedFoxHub](https://redfox.hk/?source=github) Python SDK, 6대 콘텐츠 플랫폼 — [더우인](https://redfox.hk/apis/douyin/0OT1E306), [샤오홍슈](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [위챗 공식 계정](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [빌리빌리](https://redfox.hk/apis/bilibili/TIN1NMTZ), [진르터우탸오](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019) — 의 데이터 수집 API와 4가지 AI 기능(GPT 이미지 생성, Doubao 이미지/비디오 생성, Kimi/Doubao/Deepseek AI 검색)을 제공합니다.

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

# 더우인 사용자 프로필 조회
result = client.douyin.get_user(account_id="nxpt260212")

# AI 검색
task = client.ai_search.kimi_submit(inquiry_text="2026년 AI 발전 트렌드")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## 지원 플랫폼

| 플랫폼 | 모듈 | 메서드 수 | 설명 |
|----------|--------|---------|-------------|
| 📱 더우인 | `client.douyin` | 6 | 콘텐츠/사용자 검색, 사용자 정보, 콘텐츠 상세, AI 콘텐츠 검색 |
| 📕 샤오홍슈 | `client.xiaohongshu` | 5 | 노트/사용자 검색, 계정 정보, 노트 상세, AI 노트 검색 |
| 💬 위챗 | `client.wechat` | 7 | 글/계정 검색, 계정 정보, 글 상세, AI 글 검색 |
| 📺 빌리빌리 | `client.bilibili` | 5 | 비디오/크리에이터 검색, 크리에이터 정보, 비디오 목록, 비디오 상세 |
| 📰 진르터우탸오 | `client.toutiao` | 2 | 콘텐츠 검색, 콘텐츠 상세 |
| 🎵 TikTok | `client.tiktok` | 1 | 사용자 검색 |
| 🖼️ GPT 이미지 | `client.gpt_image` | 2 | 이미지 생성 및 결과 조회 |
| �� Doubao 이미지 | `client.doubao_image` | 4 | Pro/Lite 이미지 생성 및 조회 |
| 🎬 Doubao 비디오 | `client.doubao_video` | 2 | 비디오 생성 및 결과 조회 |
| 🔍 AI 검색 | `client.ai_search` | 6 | Kimi/Doubao/Deepseek 검색 |

## API 레퍼런스

### 더우인

```python
# 비디오 검색
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# 사용자 검색
client.douyin.search_users(keyword="기술", offset=0)

# 사용자 프로필 조회
client.douyin.get_user(account_id="nxpt260212")

# 사용자 비디오 목록 조회
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# 비디오 상세 조회
client.douyin.get_work(work_id="7654143095876898089")

# AI 비디오 검색
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### 샤오홍슈

```python
# 노트 검색
client.xiaohongshu.search_articles(keyword="여행", offset=0, sort_type="0")

# 크리에이터 검색
client.xiaohongshu.search_users(keyword="여행", offset=0)

# 크리에이터 프로필 조회
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# 노트 상세 조회
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# AI 노트 검색
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)
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
```

### 빌리빌리

```python
# 비디오 검색
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# 크리에이터 검색
client.bilibili.search_users(keyword="기술", page=1, page_size=10, order="follower")

# 크리에이터 프로필 조회
client.bilibili.get_account(mid="946974")

# 크리에이터 비디오 목록 조회
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# 비디오 상세 조회
client.bilibili.get_work(bvid="BV1ghJg6hEWV")
```

### 진르터우탸오

```python
# 콘텐츠 검색
client.toutiao.search_works(keyword="AI", offset=0)

# 콘텐츠 상세 조회
client.toutiao.get_work(opus_id="7592180245936046626")
```

### TikTok

```python
# 사용자 검색
client.tiktok.search_users(keyword="tech", cursor=0)
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
```

### GPT 이미지 생성

```python
# 텍스트 → 이미지
task = client.gpt_image.submit(
    prompt="햇살 아래 창틀에 앉아 있는 주황색 고양이",
    size="1024x1024",
    quality="medium",
    output_format="png",
    model_name="gpt-image-2",
    operation="generate",
)
result = client.gpt_image.result(task_id=task["taskId"])

# 이미지 편집
task = client.gpt_image.submit(
    prompt="배경을 해변으로 변경",
    size="1024x1024",
    model_name="gpt-image-2",
    operation="edit",
    input_fidelity=5,
    images=[{"url": "https://example.com/your-image.jpg"}],
)
result = client.gpt_image.result(task_id=task["taskId"])
```

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
- requests >= 2.25.0

## 라이선스

MIT License
