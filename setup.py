#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from setuptools import setup
setup(name="guolei_py3_components",
      version="1.0.0",
      description="guolei_py3_components",
      url="https://github.com/guolei19850528/guolei_py3_components",
      author="guolei",
      author_email="174000902@qq.com",
      license="MIT",
      packages=["guolei_py3_components"],
install_requires=["requests","ipapi","change_case","PyMySQL","redis"],
      zip_safe=False)