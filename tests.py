#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from guolei_py3_components import util, logger, database, taobao, wechat
import pymysql
import unittest


class UtilTest(unittest.TestCase):
    def tearDown(self) -> None:
        super().tearDown()
        print("util test down by {start_time_str}".format(start_time_str=util.get_time_str()))

    def setUp(self) -> None:
        super().setUp()
        print("util test up by {start_time_str}".format(start_time_str=util.get_time_str()))

    def test_run(self):
        print("uuid format 1 is {uuid}".format(uuid=util.get_uuid_str(1)))
        print("uuid format 2 is {uuid}".format(uuid=util.get_uuid_str(2)))
        print("uuid format 3 is {uuid}".format(uuid=util.get_uuid_str(3)))
        print("uuid format 4 is {uuid}".format(uuid=util.get_uuid_str(4)))
        print("uuid format 5 is {uuid}".format(uuid=util.get_uuid_str(5)))
        print("platform name is {platform_name}".format(platform_name=util.get_platform_name()))
        print("host name is {host_name}".format(host_name=util.get_host_name()))
        print("intranet ip is {intranet_ip}".format(intranet_ip=util.get_intranet_ip()))
        print("external network ip is {external_network_ip}".format(external_network_ip=util.get_external_network_ip()))
        print("current timestamp is {timestamp}".format(timestamp=util.get_timestamp()))
        print("2019-01-01 00:00:00 timestamp is {timestamp}".format(
            timestamp=util.get_timestamp(time_str="2019-01-01", formatter="%Y-%m-%d")))
        print("current time str is {time_str}".format(time_str=util.get_time_str()))
        print("taobao ip data is {ip_data}".format(ip_data=taobao.get_ip_data(util.get_external_network_ip())))
        print("current week day is {week_day}".format(week_day=util.get_week_day_by_timestamp(monday_index=1)))


class DatabaseTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        print("database test up by {start_time_str}".format(start_time_str=util.get_time_str()))

    def tearDown(self) -> None:
        super().tearDown()
        print("database test down by {start_time_str}".format(start_time_str=util.get_time_str()))

    def test_run(self):
        # mysql_config = {
        #     "host": "loclhost",
        #     "port": 3306,
        #     "user": "root",
        #     "passwd": "123456",
        #     "db": "test",
        #     "charset": "utf8",
        #     "cursorclass": pymysql.cursors.DictCursor
        # }
        # pymysql_conn_obj = database.get_pymysql_connection(**mysql_config)
        # with pymysql_conn_obj.cursor() as cursor_ob:
        #     cursor_ob.execute("select * from table1;")
        #     results=cursor_ob.fetchall()
        # redis_config={
        #     'host': 'localhost',
        #     'port': 6379,
        #     'db': 0,
        #     'password': '123456'
        # }
        # strictredis_conn_obj=database.get_strictredis_connection(**redis_config)
        # print(strictredis_conn_obj.keys("*"))
        pass


class WechatTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        print("wechat test up by {start_time_str}".format(start_time_str=util.get_time_str()))

    def tearDown(self) -> None:
        super().tearDown()
        print("wechat test down by {start_time_str}".format(start_time_str=util.get_time_str()))

    def test_run(self):

        wechat_obj = wechat.Wehcat("wx41bd6621e194c939", "a3186dd5f20f045496fa49962d0df994")
        access_token=wechat_obj.get_access_token()
        print("access_token is {access_token}".format(access_token=access_token))
        js_api_ticket=wechat_obj.get_js_api_ticket(access_token)
        print("js_api_ticket is {js_api_ticket}".format(js_api_ticket=js_api_ticket))
        print(wechat_obj.get_signatures(js_api_ticket))
        pass


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    # test_suite.addTest(UtilTest('test_run'))
    # test_suite.addTest(DatabaseTest('test_run'))
    test_suite.addTest(WechatTest('test_run'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
