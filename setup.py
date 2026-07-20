from setuptools import setup, find_packages

setup(
    name="redfox-sdk",
    version="0.1.0",
    description="RedFox 红狐数据平台 Python SDK",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RedFox",
    author_email="dev@redfox.hk",
    url="https://redfox.hk",
    packages=find_packages(include=["redfox*"]),
    python_requires=">=3.8",
    install_requires=["requests>=2.25.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
