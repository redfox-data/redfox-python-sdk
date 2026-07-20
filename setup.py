from setuptools import setup, find_packages

setup(
    name="redfox-python-sdk",
    version="0.2.2",
    description="RedFox 红狐数据平台 Python SDK — 同步+异步双客户端，自动重试，零配置",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RedFox",
    author_email="dev@redfox.hk",
    url="https://redfox.hk",
    packages=find_packages(include=["redfox*"]),
    python_requires=">=3.8",
    install_requires=["httpx>=0.25.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
