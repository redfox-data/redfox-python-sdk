# RedFox Python SDK

红狐数据平台 Python SDK，支持通过简洁的 Python 接口调用红狐平台所有数据 API。

## 安装

```bash
pip install redfox-sdk
```

## 快速开始

```python
from redfox import RedFoxClient

client = RedFoxClient(api_key="your_api_key")

# 搜索抖音作品
result = client.douyin.search_articles(keyword="人工智能")
for item in result["list"]:
    print(f"{item['title']} - 点赞: {item['likeCount']}")
```

## 获取 API Key

前往 [API Keys 页面](https://redfox.hk/settings/api-keys?source=github) 获取。

## License

MIT
