# guolei_py3_components
## a python3 components by guolei  
# util
a common util module
```python
from guolei_py3_components import util
util.get_uuid_str(1)
# use util other mehods ...
@util.call_str_to_encrypt("md5")
def encrypt_str():
    return "123456"
print(encrypt_str())
# output e10adc3949ba59abbe56e057f20f883e
  
```
# taobao
a taobao module
```python
from guolei_py3_components import taobao
# get ip data
# @see http://ip.taobao.com/instructions.html
taobao.get_ip_data(ip="")
```
# wechat  
a wechat operation class module
```python
from guolei_py3_components import wechat

# init wechat class
wechat_obj = wechat.Wehcat("your appid", "your appsecret")
# get access token
access_token = wechat_obj.get_access_token()
# get js api ticket
js_api_ticket = wechat_obj.get_js_api_ticket(access_token)
# get signatures
signatures = wechat_obj.get_signatures(js_api_ticket="", url="", type="shar1")
# get code url
code_url = wechat_obj.get_code_url(url="")
# get openid
open_id = wechat_obj.get_open_id(code="")   
```
# database
a database module
```python
# get pymysql conn obj
from guolei_py3_components import database
pymysql_conn_config = {
    "host": "localhost",
    "port": "root",
    "user": "luis",
    "passwd": "123456",
    "db": "test",
    "charset": "utf8",
}
pymysql_conn_obj = database.get_pymysql_connection(**pymysql_conn_config)


# call pymysql execute by decorator
pymysql_conn_config = {
    "host": "localhost",
    "port": "root",
    "user": "luis",
    "passwd": "123456",
    "db": "test",
    "charset": "utf8",
}
pymysql_conn_obj = database.get_pymysql_connection(**pymysql_conn_config)


@database.call_pymysql_execute(pymysql_conn_obj)
def pymysql_execute():
    query = "insert into tables...;"
    args = {}
    return query, args


print(pymysql_execute())


# call pymysql find by decorator
from guolei_py3_components import database

pymysql_conn_config = {
    "host": "localhost",
    "port": "root",
    "user": "luis",
    "passwd": "123456",
    "db": "test",
    "charset": "utf8",
}
pymysql_conn_obj = database.get_pymysql_connection(**pymysql_conn_config)


@database.call_pymysql_find(pymysql_conn_obj)
def pymysql_find():
    query = "select * from table;"
    args = {}
    return query, args


print(pymysql_find())


# call pymysql find first by decorator
from guolei_py3_components import database

pymysql_conn_config = {
    "host": "localhost",
    "port": "root",
    "user": "luis",
    "passwd": "123456",
    "db": "test",
    "charset": "utf8",
}
pymysql_conn_obj = database.get_pymysql_connection(**pymysql_conn_config)


@database.call_pymysql_find_first(pymysql_conn_obj)
def pymysql_find_first():
    # You'd better add limit 1 at the end of SQL
    query = "select * from table limit 1;"
    args = {}
    return query, args


print(pymysql_find_first())


# get strictredis conn obj
from guolei_py3_components import database

conn_config = {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "password": '123456'
}
strictredis_conn_obj = database.get_strictredis_connection(**conn_config)


# call strictredis command by decorator
from guolei_py3_components import database

conn_config = {...},
strictredis_conn_obj = database.get_strictredis_connection(**conn_config)


@call_strictredis_command(strictredis_conn_obj, get)
def strictredis_command():
    return (args), {..kwargs}

```
## logger
```python
from guolei_py3_components import logger
get logging logger obj
logging_logger_obj = logger.get_logging_logger(is_save_file=True)

# call logging logger log by decorator
from guolei_py3_components import logger

logging_logger_obj = logger.get_logging_logger(is_save_file=True)


@logger.call_logging_logger_log(logging_logger_obj, attr, prefix)
def a():
    return ""

```
## other
other component developing...

