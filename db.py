#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
import redis


def get_pymysql_connection(**kwargs):
    """
    get pymysql connection
    :param kwargs:
    :return:
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
    """
    try:
        return redis.StrictRedis(**kwargs)
    except Exception as error:
        return False
