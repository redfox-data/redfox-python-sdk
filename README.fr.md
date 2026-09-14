# RedFox Python SDK

<div align="center">
<a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/v/redfox-python-sdk.svg" alt="PyPI version"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/pyversions/redfox-python-sdk.svg" alt="Python"></a> <a href="https://pypi.org/project/redfox-python-sdk/"><img src="https://img.shields.io/pypi/l/redfox-python-sdk.svg" alt="License"></a>

<a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.md">中文</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.en.md">English</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ko.md">한국어</a> | <a href="https://github.com/redfox-data/redfox-python-sdk/blob/main/README.ja.md">日本語</a> | <strong>Français</strong>

</div>
<p align="center">
  <a href="https://redfox.hk/?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-3.png" alt="RedFox" width="100%">
  </a>
</p>

SDK Python [RedFoxHub](https://redfox.hk/?source=github), fournissant des API d'acquisition de données pour 14 grandes plateformes de contenu — [Douyin](https://redfox.hk/apis/douyin/0OT1E306), [Xiaohongshu](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [Comptes Officiels WeChat](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ), [Toutiao](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019), Kuaishou, WeChat Channels, YouTube, X (Twitter), Instagram, Dongchedi, Yiche, Autohome — plus l'agrégation de tendances multi-plateformes, des outils de téléchargement de vidéos sans filigrane et d'upload de médias, et des capacités d'IA : Génération d'images GPT, Génération d'images/vidéos Doubao, et Recherche IA (Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu).

## Pourquoi Choisir RedFoxHub

<p align="center"><em>Tarification forfaitaire limitée, à partir de <strong style="color:#e53e3e">¥0.02/requête</strong></em></p>

<table align="center">
  <tr>
    <td align="center" width="25%">
      <b>⚡ Ultra-Rapide</b><br>
      <sub>Réponse API en millisecondes, accélération CDN mondiale pour des performances instantanées</sub>
    </td>
    <td align="center" width="25%">
      <b>🛡️ Sécurisé & Fiable</b><br>
      <sub>Sécurité de niveau entreprise, transmission chiffrée, garantie de disponibilité 99.99%</sub>
    </td>
    <td align="center" width="25%">
      <b>🌍 Couverture Mondiale</b><br>
      <sub>Prise en charge des principales plateformes mondiales, accès multi-plateforme en un clic</sub>
    </td>
    <td align="center" width="25%">
      <b>💎 Tarification Flexible</b><br>
      <sub>Paiement à l'usage, sans frais cachés, forfaits adaptés à toutes les échelles</sub>
    </td>
  </tr>
</table>

## Fonctionnalités du SDK

- **Zéro Configuration** — Définissez `REDFOX_API_KEY` et commencez à coder. Paramètres plats, sans objet de configuration.
- **Retry Exponentiel** — Retry automatique avec jitter sur timeout réseau, erreurs 5xx, limite de débit 429.
- **Clients Sync + Async** — `RedFoxClient` et `AsyncRedFoxClient` avec une API totalement identique.
- **Upload de Fichiers** — Upload multipart intégré, supportant chemins de fichiers / bytes / objets fichiers.
- **Exceptions Structurées** — `RedFoxAuthError` / `RedFoxRateLimitError` / `RedFoxAPIError` avec contexte de débogage complet.
- **Prêt pour la Production** — Basé sur `httpx` avec pool de connexions, contrôle de timeout, gestionnaire de contexte.

## Installation

```bash
pip install redfox-python-sdk
```

## Authentification

### Obtenir une API Key

1. Rendez-vous sur [https://redfox.hk/settings/api-keys?source=github](https://redfox.hk/settings/api-keys?source=github) pour vous inscrire / connecter.
2. Copiez votre API Key depuis la console.
3. Définissez-la comme variable d'environnement ou passez-la directement :

```bash
export REDFOX_API_KEY="YOUR_API_KEY"
```

## Documentation API Multi-Plateforme

<p align="center">
  <a href="https://redfox.hk/apis?source=github">
    <img src="https://lyy.redfox.hk/page/redfox-page-1.png" alt="RedFox API Docs" width="100%">
  </a>
</p>

### La documentation API comprend :

- Description des en-têtes de requête
- Description des paramètres de requête
- Champs de réponse et structure des données
- Exemples de requêtes
- Exemples de réponses
- Codes d'état courants

## Démarrage Rapide

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# Rechercher des vidéos Douyin
result = client.douyin.search_articles(keyword="AI")

# Rechercher des notes Xiaohongshu
result = client.xiaohongshu.search_articles(keyword="voyage")

# Rechercher des articles WeChat
result = client.wechat.search_articles(keyword="technologie")

# Rechercher des vidéos Kuaishou
result = client.kuaishou.search_works(keyword="cuisine")

# Rechercher des vidéos YouTube
result = client.youtube.search_videos(search_query="AI tutorial")

# TOP10 des tendances agrégées
result = client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)

# Téléchargement de vidéo sans filigrane
result = client.tools.download(url="https://www.douyin.com/video/xxx")

# Recherche IA
task = client.ai_search.kimi_submit(inquiry_text="Tendances de l'IA en 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## Plateformes Supportées

| Plateforme | Module | Méthodes | Description |
|----------|--------|---------|-------------|
| 📱 Douyin | `client.douyin` | 16 | Recherche contenu/utilisateurs (premium + étendue), profil utilisateur, détail contenu, recherche IA, classements populaires/en hausse, comptes populaires, transcription |
| 📕 Xiaohongshu | `client.xiaohongshu` | 15 | Recherche notes/utilisateurs, info compte, détail note, liste notes, recherche IA, commentaires, classements quotidien/hebdo/dark-horse, comptes populaires, insights notes populaires, transcription |
| 💬 WeChat | `client.wechat` | 16 | Recherche articles/comptes (premium + étendue), info compte, détail article, liste articles, recherche IA, classements 100K+ lectures/original/force/croissance |
| 📺 Bilibili | `client.bilibili` | 8 | Recherche vidéos/créateurs, info créateur, liste vidéos, détail vidéo, extraction audio, transcription |
| 📰 Toutiao | `client.toutiao` | 5 | Recherche de contenu, détail du contenu, commentaires, recherche de comptes, liste de contenus |
| 🎵 TikTok | `client.tiktok` | 4 | Recherche d'utilisateurs, recherche de vidéos, détail vidéo, vidéos d'un utilisateur |
| 🎬 Kuaishou | `client.kuaishou` | 6 | Recherche de contenu, détail du contenu, contenus d'un compte, recherche de comptes, transcription |
| 💚 WeChat Channels | `client.wechat_channels` | 7 | Recherche de contenu, détail du contenu, contenus d'un compte, détail temps réel par lien, recherche de comptes, transcription |
| ▶️ YouTube | `client.youtube` | 4 | Recherche de vidéos, détail vidéo, commentaires, transcription (sous-titres) |
| 🐦 X (Twitter) | `client.twitter` | 4 | Recherche de tweets, détail tweet, info utilisateur, commentaires |
| 📸 Instagram | `client.instagram` | 4 | Recherche générale, détail post, commentaires, info utilisateur |
| 🚗 Dongchedi | `client.dongchedi` | 4 | Recherche de contenu, détail du contenu, contenus utilisateur, recherche d'utilisateurs |
| 🚙 Yiche | `client.yiche` | 5 | Recherche de contenu, détail article, détail vidéo, contenus d'un compte, recherche de comptes |
| 🚘 Autohome | `client.autohome` | 4 | Recherche de contenu, détail article, détail vidéo, contenus d'un compte |
| 🔥 Tendances | `client.hotspot` | 3 | Classements par plateforme, recherche par mots-clés multi-plateformes, TOP10 agrégé |
| 🖼️ GPT Image | `client.gpt_image` | 2 | Génération d'images et requête de résultat |
| 🎨 Doubao Image | `client.doubao_image` | 4 | Génération d'images Pro/Lite et requête |
| 🎬 Doubao Vidéo | `client.doubao_video` | 2 | Génération de vidéos et requête de résultat |
| 🔍 Recherche IA | `client.ai_search` | 12 | Recherche Kimi/Doubao/Deepseek/Yuanbao/Qianwen/Baidu |
| 🛠️ Outils | `client.tools` | 12 | Téléchargement de vidéos sans filigrane multi-plateformes, upload d'images/médias |

## Référence API

### Douyin

```python
# Rechercher des vidéos (premium)
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# Rechercher des utilisateurs (premium)
client.douyin.search_users(keyword="technologie", offset=0)

# Obtenir le profil utilisateur
client.douyin.get_user(account_id="nxpt260212")

# Obtenir la liste des vidéos d'un utilisateur
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# Obtenir le détail d'une vidéo (work_id ou work_url)
client.douyin.get_work(work_id="7654143095876898089")

# Rechercher des vidéos IA
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Couverture étendue ───
client.douyin.search_works_wide(keyword="AI", start_date="2026-08-01", end_date="2026-08-20")
client.douyin.search_accounts_wide(keyword="technologie")
client.douyin.get_work_wide(video_id="7654143095876898089")
client.douyin.get_user_works_wide(unique_name="nxpt260212")

# ─── Classements ───
client.douyin.get_daily_hot_rank(type="美食")                          # Contenus populaires du jour
client.douyin.get_daily_surge_rank(type="全部")                        # Hausse de likes du jour
client.douyin.get_weekly_surge_rank(type="全部")                       # Hausse de likes hebdo
client.douyin.get_hot_accounts(date_type="days", rank_date="2026-08-20", type="全部")

# ─── Transcription vidéo ───
task = client.douyin.transcript_submit(url="https://www.douyin.com/video/xxx")
result = client.douyin.transcript_result(task_id=task["taskId"])
```

### Xiaohongshu

```python
# Rechercher des notes
client.xiaohongshu.search_articles(keyword="voyage", offset=0, sort_type="0")

# Rechercher des créateurs
client.xiaohongshu.search_users(keyword="voyage", offset=0)

# Obtenir le profil d'un créateur
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# Obtenir le détail d'une note (work_id ou work_link)
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# Obtenir la liste des notes d'un créateur
client.xiaohongshu.get_user_works(red_id="nxpt260212", offset=0)

# Rechercher des notes IA
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Commentaires ───
task = client.xiaohongshu.comment_submit(opus_id="6a2ac3020000000035022d8e", data_num=-1)
result = client.xiaohongshu.comment_result(task_id=task["taskId"])

# ─── Classements / insights ───
client.xiaohongshu.get_daily_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_weekly_hot_rank(rank_date="2026-08-20", category="综合全部")
client.xiaohongshu.get_hot_accounts(date_type=1, rank_date="2026-08-20", type="综合全部")
client.xiaohongshu.search_hot_notes(keyword="穿搭", start_date="2026-08-01", end_date="2026-08-20")
client.xiaohongshu.get_dark_horse_notes(keyword="AI,穿搭", start_date="2026-08-01")

# ─── Transcription vidéo ───
task = client.xiaohongshu.transcript_submit(url="https://www.xiaohongshu.com/explore/xxx")
result = client.xiaohongshu.transcript_result(task_id=task["taskId"])
```

### Comptes Officiels WeChat

```python
# Rechercher des articles
client.wechat.search_articles(keyword="AI", offset=0)

# Rechercher des comptes
client.wechat.search_users(keyword="technologie", offset=0)

# Obtenir les informations d'un compte
client.wechat.get_account(account="rmrbwx")

# Obtenir le détail d'un article (contenu complet)
client.wechat.get_article_detail(url="https://mp.weixin.qq.com/s/...")

# Obtenir les métadonnées d'un article
client.wechat.get_work(work_uuid="3F4DE056583609162E0816FBE8C183A3")

# Obtenir la liste des articles d'un compte
client.wechat.get_user_works(
    account="rmrbwx", offset=0,
    sort_type="_2",
    publish_time_start="2026-07-01",
    publish_time_end="2026-07-20"
)

# Rechercher des articles IA
client.wechat.search_ai_articles(keyword="AI", page_num=1, page_size=10)

# ─── Couverture étendue ───
client.wechat.search_articles_wide(keyword="AI", offset=0)
client.wechat.search_users_wide(keyword="technologie")
client.wechat.get_work_wide(work_uuid="3F4DE056583609162E0816FBE8C183A3")
client.wechat.get_user_works_wide(account="rmrbwx")
client.wechat.get_account_wide(wx_id="gh_5c7e8b7f586b")

# ─── Classements ───
client.wechat.get_ten_w_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_original_rank(type="科技数码", start_date="2026-08-19", end_date="2026-08-20")
client.wechat.get_strength_rank(rank_type="day", rank_date="2026-08-20", category="科技数码")
client.wechat.get_reading_growth_rank(rank_date="2026-08-20")
```

### WeChat Channels

```python
# Rechercher des vidéos
client.wechat_channels.search_works(keyword="voyage", sort="综合", page=1, size=20)

# Obtenir le détail d'une vidéo
client.wechat_channels.get_work(video_id="export/UzFfAgtgekIEAQAAAAAAxx8")

# Obtenir les vidéos d'un compte (correspondance exacte du pseudo)
client.wechat_channels.get_user_works(nickname="央视新闻", page=1)

# Détail temps réel par lien
client.wechat_channels.get_work_by_link(url="https://weixin.qq.com/sph/xxx")

# Rechercher des comptes
client.wechat_channels.search_users(account_name="央视", page=1)

# Transcription par lien
task = client.wechat_channels.transcript_submit(url="https://weixin.qq.com/sph/xxx")
result = client.wechat_channels.transcript_result(task_id=task["taskId"])
```

### Bilibili

```python
# Rechercher des vidéos
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# Rechercher des créateurs
client.bilibili.search_users(keyword="technologie", page=1, page_size=10, order="follower")

# Obtenir le profil d'un créateur
client.bilibili.get_account(mid="946974")

# Obtenir la liste des vidéos d'un créateur (mid ou account_url)
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# Obtenir le détail d'une vidéo (bvid ou work_url)
client.bilibili.get_work(bvid="BV1ghJg6hEWV")

# Obtenir l'URL audio d'une vidéo
client.bilibili.get_audio(url="https://www.bilibili.com/video/BV1ghJg6hEWV")

# Transcription vidéo
task = client.bilibili.transcript_submit(url="https://www.bilibili.com/video/BV1ghJg6hEWV")
result = client.bilibili.transcript_result(task_id=task["taskId"])
```

### Toutiao

```python
# Rechercher du contenu
client.toutiao.search_works(keyword="AI", offset=0)

# Obtenir le détail d'un contenu
client.toutiao.get_work(opus_id="7592180245936046626")

# Obtenir les commentaires d'un contenu
client.toutiao.get_comments(opus_id="7592180245936046626")

# Rechercher des comptes
client.toutiao.search_users(name="technologie")

# Obtenir la liste des contenus d'un compte
client.toutiao.get_user_works(category="profile_all", token="MS4wLjABAAAA...")
```

### Kuaishou

```python
# Rechercher du contenu
client.kuaishou.search_works(keyword="cuisine", page=1, size=20, sort="综合")

# Obtenir le détail d'un contenu
client.kuaishou.get_work(photo_id="3x9sm2nqxmbfbuq")

# Obtenir les contenus d'un compte (kwai_id ou three_x_id)
client.kuaishou.get_user_works(three_x_id="3x4wxhrrzefrq4y", page=1)

# Rechercher des comptes
client.kuaishou.search_users(account_name="王刚", page=1)

# Transcription vidéo
task = client.kuaishou.transcript_submit(url="https://www.kuaishou.com/short-video/xxx")
result = client.kuaishou.transcript_result(task_id=task["taskId"])
```

### TikTok

```python
# Rechercher des utilisateurs
client.tiktok.search_users(keyword="tech", cursor=0)

# Rechercher des vidéos
client.tiktok.search_videos(keyword="AI", count="20", sort_type="0", region="US")

# Obtenir le détail d'une vidéo
client.tiktok.get_work(aweme_id="7532000000000000000")

# Obtenir les vidéos d'un utilisateur
client.tiktok.get_user_works(sec_user_id="MS4wLjABAAAA...")
```

### YouTube

```python
# Rechercher des vidéos
client.youtube.search_videos(search_query="AI tutorial")

# Obtenir le détail d'une vidéo
client.youtube.get_video(video_id="sa8AzBK4dao")

# Obtenir les commentaires d'une vidéo
client.youtube.get_comments(video_id="sa8AzBK4dao", sort_by="top")

# Transcription vidéo (sous-titres / parole)
client.youtube.get_transcript(video_url="https://www.youtube.com/watch?v=sa8AzBK4dao")
```

### X (Twitter)

```python
# Rechercher des tweets
client.twitter.search_tweets(keyword="AI", search_type="Top")

# Obtenir le détail d'un tweet
client.twitter.get_tweet(tweet_id="1957000000000000000")

# Obtenir les infos d'un utilisateur (screen_name ou rest_id)
client.twitter.get_user(screen_name="elonmusk")

# Obtenir les commentaires d'un tweet
client.twitter.get_comments(tweet_id="1957000000000000000")
```

### Instagram

```python
# Recherche générale
client.instagram.search(keyword="travel")

# Obtenir le détail d'un post (Shortcode ou URL complète)
client.instagram.get_post(code_or_url="DRhvwVLAHAG")

# Obtenir les commentaires d'un post
client.instagram.get_comments(code_or_url="DRhvwVLAHAG", sort_by="recent")

# Obtenir les infos d'un utilisateur (username ou user_id)
client.instagram.get_user(username="natgeo")
```

### Dongchedi

```python
# Rechercher du contenu
client.dongchedi.search_works(keyword="小米SU7", offset="0", source_type="1")

# Obtenir le détail d'un contenu
client.dongchedi.get_work(work_id="7532000000000000000", work_type="video")

# Obtenir les contenus d'un utilisateur
client.dongchedi.get_user_works(user_id="60480000000000000", cursor=0)

# Rechercher des utilisateurs
client.dongchedi.search_users(keyword="陈震", offset=0)
```

### Yiche

```python
# Rechercher du contenu (club=communauté / shipin=vidéo / xinwen=article)
client.yiche.search_works(keyword="小米SU7", page=1, source_type="xinwen")

# Obtenir le détail d'un article
client.yiche.get_article(url="https://news.yiche.com/hao/wenzhang/xxx.html")

# Obtenir le détail d'une vidéo
client.yiche.get_video(work_id="50000000")

# Obtenir les contenus d'un compte
client.yiche.get_user_works(user_id="600000000")

# Rechercher des comptes
client.yiche.search_users(keyword="陈震", page=1)
```

### Autohome

```python
# Rechercher du contenu (club / article / video)
client.autohome.search_works(keyword="小米SU7", source_type="video")

# Obtenir le détail d'un article (Chejiahao)
client.autohome.get_article(work_id="3000000")

# Obtenir le détail d'une vidéo (0=compte original, 4=Chejiahao)
client.autohome.get_video(video_id="5000000", video_type=4)

# Obtenir les contenus d'un compte
client.autohome.get_user_works(author_id="7000000", page=0)
```

### Tendances

```python
# Classement par plateforme : 1=Kuaishou 2=Douyin 5=Weibo 6=Xiaohongshu 7=Baidu 8=Bilibili 9=Zhihu 10=Toutiao
client.hotspot.get_platform_rank(
    platform=2,
    start_date="2026-08-20",
    end_date="2026-08-21",
)

# Recherche de tendances par mots-clés (plage jusqu'à 30 jours)
client.hotspot.search_by_keywords(
    keywords=["Samsung"],
    start_date="2026-08-01",
    end_date="2026-08-21",
    platforms=[2, 5, 10],
)

# TOP10 des tendances agrégées
client.hotspot.get_top10(
    start_date="2026-08-20 00:00:00",
    end_date="2026-08-21 00:00:00",
)
```

### Outils

```python
# Téléchargeur vidéo universel (détection automatique de la plateforme)
client.tools.download(url="https://www.douyin.com/video/xxx")

# Téléchargement sans filigrane par plateforme
client.tools.download_douyin(url="https://www.douyin.com/video/xxx")
client.tools.download_kuaishou(url="https://www.kuaishou.com/short-video/xxx")
client.tools.download_xiaohongshu(url="https://www.xiaohongshu.com/explore/xxx")
client.tools.download_bilibili(url="https://www.bilibili.com/video/BV1xxx")
client.tools.download_wechat_channels(url="https://weixin.qq.com/sph/xxx")
client.tools.download_tiktok(url="https://www.tiktok.com/@user/video/xxx")
client.tools.download_youtube(url="https://www.youtube.com/watch?v=xxx")
client.tools.download_instagram(url="https://www.instagram.com/reel/xxx")
client.tools.download_twitter(url="https://x.com/user/status/xxx")

# Upload d'image (png / jpeg / webp)
client.tools.upload_image(file="./cover.png", format="png")

# Upload de média vidéo/audio/image
client.tools.upload_file(file="./clip.mp4", format="mp4")
```

### Recherche IA

```python
# Recherche Kimi
task = client.ai_search.kimi_submit(inquiry_text="Tendances de l'IA en 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])

# Recherche Doubao
task = client.ai_search.doubao_submit(inquiry_text="Recommandations de boissons d'été")
result = client.ai_search.doubao_result(task_id=task["taskId"])

# Recherche Deepseek
task = client.ai_search.deepseek_submit(inquiry_text="Optimisation des performances Python")
result = client.ai_search.deepseek_result(task_id=task["taskId"])

# Recherche Yuanbao
task = client.ai_search.yuanbao_submit(inquiry_text="Recommandations de véhicules électriques")
result = client.ai_search.yuanbao_result(task_id=task["taskId"])

# Recherche Qianwen
task = client.ai_search.qianwen_submit(inquiry_text="Guide de voyage Hangzhou")
result = client.ai_search.qianwen_result(task_id=task["taskId"])

# Recherche Baidu
task = client.ai_search.baidu_submit(inquiry_text="Actualités financières du jour")
result = client.ai_search.baidu_result(task_id=task["taskId"])
```

### Génération d'Images GPT

```python
# Texte → Image
task = client.gpt_image.submit(
    prompt="Un chat orange assis sur un rebord de fenêtre, la lumière du soleil sur son pelage",
    resolution="1k",   # 1k / 2k / 4k
    size="1:1",        # ratio — 13 valeurs dont 1:1, 16:9, 9:16
    n=1,               # nombre d'images, jusqu'à 4
)
result = client.gpt_image.result(task_id=task["taskId"])
print(result["status"], result["imageUrls"])

# Édition d'image
task = client.gpt_image.submit(
    prompt="Remplacer l'arrière-plan par une plage",
    resolution="2k",
    size="16:9",
    n=2,
    reference_images=["https://example.com/your-image.jpg"],  # URL d'images de référence, jusqu'à 2
)
result = client.gpt_image.result(task_id=task["taskId"])
```

> **Remarque** : les `imageUrls` renvoyés par `result()` expirent en quelques minutes (404 ensuite) — téléchargez-les immédiatement. `status` vaut `queued`/`in_progress`/`completed`/`failed` ; seuls les deux derniers sont terminaux. Pour réutiliser une image générée comme référence, soumettez avant son expiration.

### Génération d'Images Doubao

```python
# Modèle Pro
task = client.doubao_image.pro_submit(
    prompt="Une ville futuriste flottant dans les nuages",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    watermark=False,
)
result = client.doubao_image.pro_result(task_id=task["taskId"])

# Modèle Lite (supporte les images multiples)
task = client.doubao_image.lite_submit(
    prompt="Peintures de paysages des quatre saisons",
    size="2048x2048",
    output_format="jpeg",
    response_format="url",
    sequential="auto",
    max_images=4,
)
result = client.doubao_image.lite_result(task_id=task["taskId"])
```

### Génération de Vidéos Doubao

```python
# Texte → Vidéo
task = client.doubao_video.submit(
    content=[{"type": "text", "text": "Un chat qui bâille au soleil, son pelage ondulant doucement dans la brise"}],
    resolution="720p",
    ratio="16:9",
    duration=5,
    watermark=False,
    generate_audio=True,
)
result = client.doubao_video.result(task_id=task["taskId"])

# Image → Vidéo
task = client.doubao_video.submit(
    content=[
        {"type": "text", "text": "Faire sourire et saluer la personne dans l'image"},
        {"type": "image_url", "image_url": "https://example.com/photo.jpg"},
    ],
    resolution="720p",
    duration=5,
)
result = client.doubao_video.result(task_id=task["taskId"])
```

## Gestion des Erreurs

Le SDK fournit trois types d'exceptions :

```python
from redfox import RedFoxAPIError, RedFoxAuthError, RedFoxRateLimitError

try:
    result = client.douyin.search_articles(keyword="AI")
except RedFoxAuthError as e:
    print(f"Échec d'authentification : {e}")
except RedFoxRateLimitError as e:
    print(f"Limite de requêtes dépassée : {e}")
except RedFoxAPIError as e:
    print(f"Erreur API : code={e.code}, msg={e}")
```

## Prérequis

- Python >= 3.8
- httpx >= 0.25.0

## Licence

MIT License
