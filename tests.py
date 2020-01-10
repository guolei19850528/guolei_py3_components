#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from guolei_py3_components import util, logger, database, taobao, wechat
import pymysql
import unittest


class UtilTest(unittest.TestCase):
    def tearDown(self) -> None:
        super().tearDown()
        print("util test down by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def setUp(self) -> None:
        super().setUp()
        print("util test up by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def test_run(self):
        import os
        logging_logger_obj = logger.get_logging_logger(is_save_file=True)

        from guolei_py3_components.mail import Mail
        mail_obj = Mail()
        mail_obj.smtp_host = "smtp.exmail.qq.com"
        mail_obj.smtp_port = 465
        mail_obj.sender_name = "郭磊<174000902@qq.com>"
        mail_obj.sender_account = "guolei@ihmedia.com.cn"
        mail_obj.sender_password = "BvxjBcUaMydne7gp"
        mail_obj.to_addresses = ["guolei_qq<174000902@qq.com>"]
        mail_obj.cc_addresses = []
        mail_obj.bcc_addresses = []
        attachments = [
            {
                "name": "郭磊发送附件.txt",
                "path": os.path.join(os.getcwd(), "runtime", "a.txt")
            }
        ]
        print(mail_obj.smtp_ssl_send_mail(
            "郭磊test", "test content", attachments))

        pass


class DatabaseTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        print("database test up by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def tearDown(self) -> None:
        super().tearDown()
        print("database test down by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def test_run(self):
        # print(util.get_random_str(64))
        # data = {
        #     "id": None,
        #     "aaa": "1",
        #     "bbbb": "2"
        # }
        # fields = ["`{field}`".format(field=item[0]) for item in data.items()]
        # values = ["%({field})s".format(field=item[0]) for item in data.items()]
        # fields_str = ",".join(fields)
        # values_str = ",".join(values)
        # mysql_config = {
        #     "host": "121.42.166.250",
        #     "port": 3306,
        #     "user": "luis",
        #     "passwd": "123456",
        #     "db": "polyrich",
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
        print("wechat test up by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def tearDown(self) -> None:
        super().tearDown()
        print("wechat test down by {start_time_str}".format(
            start_time_str=util.get_time_str()))

    def test_run(self):
        wechat_obj = wechat.Wehcat(
            "wx41bd6621e194c939", "a3186dd5f20f045496fa49962d0df994")
        access_token = wechat_obj.get_access_token()
        print("access_token is {access_token}".format(
            access_token=access_token))
        js_api_ticket = wechat_obj.get_js_api_ticket(access_token)
        print("js_api_ticket is {js_api_ticket}".format(
            js_api_ticket=js_api_ticket))
        print(wechat_obj.get_signatures(js_api_ticket))
        pass


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(UtilTest('test_run'))
    # test_suite.addTest(DatabaseTest('test_run'))
    # test_suite.addTest(WechatTest('test_run'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    import os

    os._exit(0)
