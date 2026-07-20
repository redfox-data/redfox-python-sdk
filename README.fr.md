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

SDK Python [RedFoxHub](https://redfox.hk/?source=github), fournissant des API d'acquisition de données pour six grandes plateformes de contenu — [Douyin](https://redfox.hk/apis/douyin/0OT1E306), [Xiaohongshu](https://redfox.hk/apis/xiaohongshu/4IVIDHEN), [Comptes Officiels WeChat](https://redfox.hk/apis/gongzhonghao/6C4A77XR), [Bilibili](https://redfox.hk/apis/bilibili/TIN1NMTZ), [Toutiao](https://redfox.hk/apis/jinritoutiao/28CFGF5I), [TikTok](https://redfox.hk/apis/tool-tiktok/20070019) — et quatre capacités d'IA : Génération d'images GPT, Génération d'images/vidéos Doubao, et Recherche IA (Kimi/Doubao/Deepseek).

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

# Obtenir le profil d'un utilisateur Douyin
result = client.douyin.get_user(account_id="nxpt260212")

# Recherche IA
task = client.ai_search.kimi_submit(inquiry_text="Tendances de l'IA en 2026")
result = client.ai_search.kimi_result(task_id=task["taskId"])
```

## Plateformes Supportées

| Plateforme | Module | Méthodes | Description |
|----------|--------|---------|-------------|
| 📱 Douyin | `client.douyin` | 6 | Recherche de contenu/utilisateurs, profil utilisateur, détail du contenu, recherche IA |
| 📕 Xiaohongshu | `client.xiaohongshu` | 5 | Recherche de notes/utilisateurs, info compte, détail note, recherche IA |
| 💬 WeChat | `client.wechat` | 7 | Recherche d'articles/comptes, info compte, détail article, recherche IA |
| 📺 Bilibili | `client.bilibili` | 5 | Recherche de vidéos/créateurs, info créateur, liste vidéos, détail vidéo |
| 📰 Toutiao | `client.toutiao` | 2 | Recherche de contenu, détail du contenu |
| 🎵 TikTok | `client.tiktok` | 1 | Recherche d'utilisateurs |
| 🖼️ GPT Image | `client.gpt_image` | 2 | Génération d'images et requête de résultat |
| 🎨 Doubao Image | `client.doubao_image` | 4 | Génération d'images Pro/Lite et requête |
| 🎬 Doubao Vidéo | `client.doubao_video` | 2 | Génération de vidéos et requête de résultat |
| 🔍 Recherche IA | `client.ai_search` | 6 | Recherche Kimi/Doubao/Deepseek |

## Référence API

### Douyin

```python
# Rechercher des vidéos
client.douyin.search_articles(keyword="AI", offset=0, sort_type="0")

# Rechercher des utilisateurs
client.douyin.search_users(keyword="technologie", offset=0)

# Obtenir le profil utilisateur
client.douyin.get_user(account_id="nxpt260212")

# Obtenir la liste des vidéos d'un utilisateur
client.douyin.get_user_works(account_id="nxpt260212", offset=0)

# Obtenir le détail d'une vidéo
client.douyin.get_work(work_id="7654143095876898089")

# Rechercher des vidéos IA
client.douyin.search_ai_articles(keyword="AI", page_num=1, page_size=10)
```

### Xiaohongshu

```python
# Rechercher des notes
client.xiaohongshu.search_articles(keyword="voyage", offset=0, sort_type="0")

# Rechercher des créateurs
client.xiaohongshu.search_users(keyword="voyage", offset=0)

# Obtenir le profil d'un créateur
client.xiaohongshu.get_account(account_id="5e1e4c8c0000000001023027")

# Obtenir le détail d'une note
client.xiaohongshu.get_work(work_id="6a2ac3020000000035022d8e")

# Rechercher des notes IA
client.xiaohongshu.search_ai_articles(keyword="AI", page_num=1, page_size=10)
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
```

### Bilibili

```python
# Rechercher des vidéos
client.bilibili.search_articles(keyword="Python", page=1, page_size=10, order="time")

# Rechercher des créateurs
client.bilibili.search_users(keyword="technologie", page=1, page_size=10, order="follower")

# Obtenir le profil d'un créateur
client.bilibili.get_account(mid="946974")

# Obtenir la liste des vidéos d'un créateur
client.bilibili.get_user_works(mid="946974", page=1, page_size=10, order="time")

# Obtenir le détail d'une vidéo
client.bilibili.get_work(bvid="BV1ghJg6hEWV")
```

### Toutiao

```python
# Rechercher du contenu
client.toutiao.search_works(keyword="AI", offset=0)

# Obtenir le détail d'un contenu
client.toutiao.get_work(opus_id="7592180245936046626")
```

### TikTok

```python
# Rechercher des utilisateurs
client.tiktok.search_users(keyword="tech", cursor=0)
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
```

### Génération d'Images GPT

```python
# Texte → Image
task = client.gpt_image.submit(
    prompt="Un chat orange assis sur un rebord de fenêtre, la lumière du soleil sur son pelage",
    size="1024x1024",
    quality="medium",
    output_format="png",
    model_name="gpt-image-2",
    operation="generate",
)
result = client.gpt_image.result(task_id=task["taskId"])

# Édition d'image
task = client.gpt_image.submit(
    prompt="Remplacer l'arrière-plan par une plage",
    size="1024x1024",
    model_name="gpt-image-2",
    operation="edit",
    input_fidelity=5,
    images=[{"url": "https://example.com/your-image.jpg"}],
)
result = client.gpt_image.result(task_id=task["taskId"])
```

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
- requests >= 2.25.0

## Licence

MIT License
