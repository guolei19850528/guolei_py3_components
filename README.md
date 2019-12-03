# guolei_py3_components
a guolei python3 components  
# util
a common utile module
```python
  
```
# wechat  
a wechat operation class module
```python
    from guolei_py3_components import wechat
    # init wechat class
    wechat_obj = wechat.Wehcat("your appid", "your appsecret")
    # get access token
    access_token=wechat_obj.get_access_token()
    # get js api ticket
    js_api_ticket=wechat_obj.get_js_api_ticket(access_token)
    
    """
    get signatures
    :param js_api_ticket:
    :param url:
    :param type:
    :return:dict
    {
        "nonce_str": "",
        "signature": "",
        "timestamp": ""
    }
    """    
    wechat_obj.get_signatures(js_api_ticket="", url="", type="shar1")
```

