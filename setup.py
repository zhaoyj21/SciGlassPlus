from setuptools import setup, find_packages

setup(
    name="SciGlassPlus",
    version="1.0.0",
    author="Wei Chen, Yingjie Zhao, Zhiping Xu",
    author_email="wchen314@qq.com",
    description="The access interface of the SciGlassPlus database",
    long_description=open("README.md").read(),
    url="https://github.com/zhaoyj21/SciGlassPlus",

    packages=find_packages(),
    include_package_data=True,
    package_data={
        "SciGlassPlus": ["*.xlsx", "*.json"],
    },

    install_requires=[
        "python>=3.10",
        "pandas>=2.3.2",
        "openpyxl>=3.1.5"
    ],
)