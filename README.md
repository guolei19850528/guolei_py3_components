# guolei_py3_components
## a python3 components by guolei  
# util
a common util module
```python
  from guolei_py3_components import util
  util.get_uuid_str(1)
  # use util other mehods ...
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
    #get openid
    open_id = wechat_obj.get_open_id(code="")
```
# database
a database module
```python
  from guolei_py3_components import database
  """
  get pymysql connection
  # kwargs 
  {
    "host": "host",
    "port": port,
    "user": "user",
    "passwd": "password",
    "db": "db",
    "charset": "charset",
  },
  """
  database.get_pymysql_connection(**kwargs)

  """
  get strictredis connection
  # kwargs 
  {
    'host': 'host',
    'port': port,
    'db': db,
    'password': 'password'
  },
  """
  database.get_strictredis_connection(**kwargs)
```
## other
other component developing...

