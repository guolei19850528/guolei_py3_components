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
    from guolei_py3_components import database
    conn_config={
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": "test",
        "charset": "utf8",
        "cursorclass": pymysql.cursors.DictCursor
    },
    pymysql_conn_obj=database.get_pymysql_connection(**conn_config)
    use pymysql_conn_obj code ...
    """
    try:
        if "cursorclass" not in kwargs.keys():
            kwargs["cursorclass"] = pymysql.cursors.DictCursor
        return pymysql.Connect(**kwargs)
    except Exception as error:
        return False


def call_pymysql_execute(pymysql_conn_obj):
    """
    call pymysql execute by decorator
    :param pymysql_conn_obj:
    :return: (query_status:bool,affected_rows:int,lastrowid:int)
    example
    from guolei_py3_components import database
    pymysql_conn_config={}
    pymysql_conn_obj=database.get_pymysql_connection(**pymysql_conn_config)

    @database.call_pymysql_execute(pymysql_conn_obj)
    def pymysql_execute():
        query="insert into tables...;"
        args={}
        return query,args
    print(pymysql_execute())
    """

    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            query, args = func(*args, **kwargs)
            with pymysql_conn_obj.cursor() as cursor_obj:
                try:
                    cursor_obj.execute(query, args)
                    pymysql_conn_obj.commit()
                    return True, cursor_obj.rowcount, cursor_obj.lastrowid
                except Exception as error:
                    pymysql_conn_obj.rollback()
                    return False, -1, -1
                finally:
                    cursor_obj.close()

        return wrapper_func

    return decorator_func


def call_pymysql_find(pymysql_conn_obj):
    """
    call pymysql find by decorator
    :param pymysql_conn_obj:
    :return: (query_status:bool,data:list)
    example
    from guolei_py3_components import database
    pymysql_conn_config={}
    pymysql_conn_obj=database.get_pymysql_connection(**pymysql_conn_config)

    @database.call_pymysql_find(pymysql_conn_obj)
    def pymysql_find():
        query="select * from table;"
        args={}
        return query,args
    print(pymysql_find())
    """

    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            query, args = func(*args, **kwargs)
            with pymysql_conn_obj.cursor() as cursor_obj:
                try:
                    cursor_obj.execute(query, args)
                    pymysql_conn_obj.commit()
                    return True, cursor_obj.fetchall()
                except Exception as error:
                    pymysql_conn_obj.rollback()
                    return False, []
                finally:
                    cursor_obj.close()

        return wrapper_func

    return decorator_func


def call_pymysql_find_first(pymysql_conn_obj):
    """
    call pymysql find first by decorator
    :param pymysql_conn_obj:
    :return: (query_status:bool,data:dict)
    example
    from guolei_py3_components import database
    pymysql_conn_config={}
    pymysql_conn_obj=database.get_pymysql_connection(**pymysql_conn_config)

    @database.call_pymysql_find_first(pymysql_conn_obj)
    def pymysql_find_first():
        # You'd better add limit 1 at the end of SQL
        query="select * from table limit 1;"
        args={}
        return query,args
    print(pymysql_find_first())
    """

    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            query, args = func(*args, **kwargs)
            with pymysql_conn_obj.cursor() as cursor_obj:
                try:
                    cursor_obj.execute(query, args)
                    pymysql_conn_obj.commit()
                    return True, cursor_obj.fetchone()
                except Exception as error:
                    pymysql_conn_obj.rollback()
                    return False, {}
                finally:
                    cursor_obj.close()

        return wrapper_func

    return decorator_func


def get_strictredis_connection(**kwargs):
    """
    get strict redis connection
    :param kwargs:
    :return:
    example
    from guolei_py3_components import database
    conn_config={
        "host": "localhost",
        "port": 6379,
        "db": 0,
        "password": '123456'
    },
    strictredis_conn_obj=database.get_strictredis_connection(**conn_config)
    use strictredis_conn_obj code ...
    """
    try:
        return redis.StrictRedis(**kwargs)
    except Exception as error:
        return False


def call_strictredis_command(strictredis_conn_obj, attr):
    """
    call strictredis command by decorator
    :param strictredis_conn_obj:
    :param attr: redis command str
    :return:
    example
    from guolei_py3_components import database
    conn_config={...},
    strictredis_conn_obj=database.get_strictredis_connection(**conn_config)

    @call_strictredis_command(strictredis_conn_obj,get)
    def strictredis_command():
        return (args),{..kwargs}
    """

    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            if hasattr(strictredis_conn_obj, attr):
                call_attr = getattr(strictredis_conn_obj, attr)
            args, kwargs = func(*args, **kwargs)
            if isinstance(args, tuple) and len(args):
                return call_attr(*args)
            elif isinstance(kwargs, dict) and len(kwargs):
                return call_attr(**kwargs)
            raise TypeError("command error")

        return wrapper_func

    return decorator_func


class Paginator(object):
    def __init__(self, total=0, size=10, current=1, split=10):
        self._current = current
        self._first = 1
        self._last = 1
        self._previous = 1
        self._next = 1
        self._offset = 1
        self._size = size
        self._pages = 1
        self._total = total
        self._split = split
        self._previous_split = 0
        self._next_split = split
        self._currents = []

    @property
    def current(self):
        if int(self._current) < 1:
            self._current = 1
        if int(self._current) >= int(self.pages):
            self._current = self.pages
        return self._current

    @property
    def first(self):
        self._first = 1
        return self._first

    @property
    def last(self):
        self._last = int(self.pages)
        return self._last

    @property
    def previous(self):
        current = int(self.current)
        previous = current - 1
        if previous < 1:
            previous = 1
        self._previous = previous
        return self._previous

    @property
    def next(self):
        current = int(self.current)
        pages = int(self.pages)
        next = current + 1
        if next > pages:
            next = pages
        self._next = next
        return self._next

    @property
    def offset(self):
        current = int(self.current)
        size = int(self.size)
        offset = (current - 1) * size
        if int(offset) < 0:
            offset = 0
        self._offset = offset
        return self._offset

    @property
    def size(self):
        if int(self._size) <= 0:
            self._size = 10
        return self._size

    @property
    def pages(self):
        pages = 1
        total = int(self.total)
        size = int(self.size)
        if total % size == 0:
            pages = int(total / size)
        else:
            pages = int(total / size) + 1
        if int(pages) < 1:
            pages = 1
        self._pages = pages
        return self._pages

    @property
    def total(self):
        if int(self._total) <= 0:
            self._total = 0
        return self._total

    @property
    def split(self):
        if int(self._split) <= 0:
            self._split = 10
        return self._split

    @property
    def previous_split(self):
        if int(self.current) < int(self.split):
            self._previous_split = 1
        else:
            self._previous_split = int((int(self.current) / int(self.split))) * int(self.split)
        return self._previous_split

    @property
    def next_split(self):
        if int(self.current) < int(self.split):
            self._next_split = int(self.split) + 1
        else:
            self._next_split = int((int(self.current) / int(self.split))) * int(self.split) + int(self.split)
        if int(self._next_split) >= int(self.pages):
            self._next_split = int((int(self.pages) / int(self.split))) * int(self.split)
        return self._next_split

    @property
    def currents(self):
        if int(self.pages) <= int(self.split):
            self._currents = [i + 1 for i in range(int(self.pages))]
        else:
            if int(self.current) == int(self.previous_split):
                self._currents = [i + 1 for i in
                                  range((int(self.previous_split) - int(self.split)), int(self.previous_split))]
            else:
                if int(self.previous_split) == int(self.next_split):
                    self._currents = [i + 1 for i in
                                      range(int(self.previous_split) - int(self.split), int(self.previous_split))]
                else:
                    self._currents = [i + 1 for i in range(self.previous_split, int(self.next_split))]
        return self._currents

    def to_dict(self):
        return {
            "current": self.current,
            "first": self.first,
            "last": self.last,
            "previous": self.previous,
            "next": self.next,
            "offset": self.offset,
            "size": self.size,
            "pages": self.pages,
            "total": self.total,
            "split": self.split,
            "previous_split": self.previous_split,
            "next_split": self.next_split,
            "currents": self.currents,
        }
