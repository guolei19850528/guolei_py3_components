#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="guolei_py3_components",
      version="1.0.9",
      description="a python3 components by guolei",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/guolei19850528/guolei_py3_components",
      author="guolei",
      author_email="174000902@qq.com",
      license="MIT",
      keywors=["utils,wechat,database,pymysql,redis,requests"],
      packages=["guolei_py3_components"],
      install_requires=["requests", "ipapi", "change_case", "PyMySQL", "redis", "inflect"],
      python_requires='>=3.0',
      zip_safe=False)
