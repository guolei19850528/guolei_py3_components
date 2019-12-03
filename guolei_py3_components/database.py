#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
import redis

"""
database component
dependents
PyMySQL
redis
"""


def get_pymysql_connection(**kwargs):
    """
    get pymysql connection
    :param kwargs:
    :return:
    example
    {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": "test",
        "charset": "utf8",
        "cursorclass": pymysql.cursors.DictCursor
    },
    """
    try:
        if "cursorclass" not in kwargs.keys():
            kwargs["cursorclass"] = pymysql.cursors.DictCursor
        return pymysql.Connect(**kwargs)
    except Exception as error:
        return False


def get_strictredis_connection(**kwargs):
    """
    get strictredis connection
    :param kwargs:
    :return:
    example
    {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'password': '123456'
    },
    """
    try:
        return redis.StrictRedis(**kwargs)
    except Exception as error:
        return False
