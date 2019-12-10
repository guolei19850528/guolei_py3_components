#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
common util
"""
import string


def get_uuid_str(option=1):
    """
    get uuid str
    use uuid4
    :param option: int
    if option is 1 0aa349e2-642c-4332-a996-f6bf4f7d49d4
    if option is 2 {0aa349e2-642c-4332-a996-f6bf4f7d49d4}
    if option is 3 [0aa349e2-642c-4332-a996-f6bf4f7d49d4]
    if option is 4 (0aa349e2-642c-4332-a996-f6bf4f7d49d4)
    if option is 5 0aa349e2642c4332a996f6bf4f7d49d4
    :return:str
    """
    import uuid
    uuid_str = str(uuid.uuid4())
    if option not in [1, 2, 3, 4, 5]:
        option = 1
    if option == 1:
        return uuid_str
    if option == 2:
        return "{" + uuid_str + "}"
    if option == 3:
        return "[" + uuid_str + "]"
    if option == 4:
        return "(" + uuid_str + ")"
    if option == 5:
        return uuid_str.replace("-", "")


def get_encrypt_str(encrypt_type="md5", need_encrypt_str=""):
    """
    get encrypt str
    :param encrypt_type:
    encrypt_name must in
    [
        md5
        sha1,
        sha224,
        sha256,
        sha384,
        sha512,
        blake2s,
        blake2b,
        sha3_224,
        sha3_256,
        sha3_384,
        sha3_512,
        shake_128,
        shake_256
    ]
    :param need_encrypt_str: need encrypt_str
    :return: encrypted str
    demo
    encrypted_str=get_encrypt_str(encrypt_type="md5", need_encrypt_str="123456")
    more...
    """
    import hashlib
    encrypted_str = hashlib.new(encrypt_type, need_encrypt_str.encode("utf-8")).hexdigest()
    return encrypted_str


def call_str_to_encrypt(encrypt_type="md5"):
    """
    call str to encrypt by decorator
    :param encrypt_type: see get_encrypt_str
    :return:
    demo
    @util.call_encrypt("md5")
    def a():
        return "123456"
    print(a())
    e10adc3949ba59abbe56e057f20f883e
    """

    def decorator_func(func):
        def wrapper_func(*args, **kw):
            need_encrypt_str = str(func(*args, **kw))
            return get_encrypt_str(encrypt_type=encrypt_type, need_encrypt_str=need_encrypt_str)

        return wrapper_func

    return decorator_func


def call_str_to_upper(func):
    """
    call str to upper by decorator
    :param func:
    :return:
    """

    def decorator_func():
        return str(func()).upper()

    return decorator_func


def call_str_to_lower(func):
    """
    call str to lower by decorator
    :param func:
    :return:
    """

    def decorator_func():
        return str(func()).lower()

    return decorator_func


def get_random_str(length=0, strings=string.ascii_letters + string.digits):
    """
    get random str
    :param length:int
    :param strings: str
    default string.ascii_letters + string.digits
    :return: str
    """
    return "".join([strings[get_random_choice(len(strings))] for i in range(length)])


def get_random_choice(max=1):
    """
    get random choice
    use random.choice
    :param max:int
    :return:int
    """
    import random
    return random.choice(range(max))


def get_timestamp(time_str="", formatter="%Y-%m-%d %H:%M:%S", is_millisecond=False):
    """
    get timestamp
    :param time_str:str
    if time_str is "" current timestamp
    :param formatter:str
    default %Y-%m-%d %H:%M:%S
    :param is_millisecond:bool
    is millisecond
    :return:int
    """
    import time
    if not isinstance(time_str, str) or not len(time_str):
        timestamp = time.time()
        if is_millisecond:
            return timestamp
        else:
            return int(timestamp)
    else:
        try:
            time_tuple = time.strptime(time_str, formatter)
            timestamp = time.mktime(time_tuple)
            if is_millisecond:
                return timestamp
            else:
                return int(timestamp)
        except Exception as error:
            return 0


def get_time_str(timestamp=0, formatter="%Y-%m-%d %H:%M:%S"):
    """
    get time str
    :param timestamp:int
    if timestamp is 0 current time str
    :param formatter:str
    default %Y-%m-%d %H:%M:%S
    :return:str
    """
    import time
    try:
        if timestamp > 0:
            return time.strftime(formatter, time.localtime(timestamp))
        return time.strftime(formatter, time.localtime(time.time()))
    except Exception as error:
        return None


def get_week_day_by_str(date_str="", monday_index=0, formatter="%Y-%m-%d"):
    """
    get week day by str
    :param date_str:str
    :param monday_index:int
    monday index
    :param formatter:str
    :return:int
    """
    import time
    try:
        week_day = time.strptime(date_str, formatter).tm_wday
        return week_day + monday_index
    except Exception as error:
        return None


def get_week_day_by_timestamp(timestamp=0, monday_index=0, formatter="%Y-%m-%d"):
    """
    get week day by timestamp
    :param timestamp:int current timestamp
    :param monday_index:int
    :param formatter:str
    :return:int
    """
    import time
    try:
        date_str = get_time_str(timestamp, formatter)
        week_day = time.strptime(date_str, formatter).tm_wday
        return week_day + monday_index
    except Exception as error:
        return None


def get_time_diff_tuple(timestamp1=0, timestamp2=0):
    """
    get time diff tuple
    :param timestamp1:int
    :param timestamp2:int
    :return:tuple
    """
    try:
        if not isinstance(timestamp1, (int, float)) or not isinstance(timestamp2, (int, float)):
            return 0, 0, 0, 0
        import math
        diff_val = abs(timestamp1 - timestamp2)
        return diff_val // get_day_seconds(1), (diff_val % get_day_seconds(1)) // 3600, (
                (diff_val % get_day_seconds(1)) % 3600) // 60, (((diff_val % get_day_seconds(1)) % 3600) % 60)
    except Exception as error:
        return 0, 0, 0, 0


def get_time_diff_by_str(time_str1="", formatter1="%Y-%m-%d %H:%M:%S", time_str2="", formatter2="%Y-%m-%d %H:%M:%S"):
    """
    get time diff by str
    :param time_str1:str
    :param formatter1:str
    :param time_str2:
    :param formatter2:str
    :return:tuple
    """
    return get_time_diff_tuple(get_timestamp(time_str1, formatter1), get_timestamp(time_str2, formatter2))


def get_day_seconds(days=1):
    """
    get days seconds
    :param days:int
    :return:int
    """
    return int((60 * 60 * 24) * abs(days))


def get_time_now_tuple():
    """
    get time now tuple
    :return:tuple
    """
    import time
    time_struct = time.localtime(time.time())
    return tuple(time_struct)


def is_leap_year(year=0):
    """
    is leap year
    :param year:int
    :return:bool
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def get_month_max_days(year=0, month=0):
    """
    get month max days
    :param year:int
    :param month:int
    :return:int
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return 28
    return None


def get_platform_name(is_use_sysconfig=False):
    """
    get platform name
    :param is_use_sysconfig:bool
    :return:str
    """
    import sys
    import sysconfig
    platform_name = sys.platform
    if is_use_sysconfig:
        return sysconfig.get_platform()
    if sys.platform == "win32":
        platform_name = "windows"
    if sys.platform == "darwin":
        platform_name = "macosx"
    return platform_name


def get_host_name():
    """
    get host name
    :return:str
    """
    import socket
    return socket.gethostname()


def get_intranet_ip():
    """
    get intranet ip
    :return:str
    """
    import socket
    return socket.gethostbyname(get_host_name())


def jsonp_convert_json(jsonp_str=""):
    """
    jsonp convert json
    :param jsonp_str:str
    :return:
    """
    try:
        l_index = jsonp_str.index("(") + 1
        r_index = jsonp_str.rindex(")")
        return jsonp_str[l_index:r_index]
    except Exception as error:
        return None


def get_external_network_ip():
    """
    get external network ip
    :return:str
    """
    try:
        ipapi_obj = get_ipapi_obj(ip=None, key=None, field=None)
        if ipapi_obj:
            return ipapi_obj["ip"]
        return None
    except Exception as error:
        return None


def get_ipapi_obj(ip=None, key=None, field=None):
    """
    get ipapi obj
    :param ip:str
    :param key:str
    :param field:str
    :return:json object
    """
    try:
        import ipapi
        ipapi_obj = ipapi.location(ip, key, field)
        return ipapi_obj
    except Exception as error:
        return None


def is_email(value=""):
    """
    is email
    :param value:
    :return:bool
    """
    import re
    return re.match(r"^[\w\-\.]+@[\w\-\.]+(\.\w+)+$", str(value))


def is_mobile(value=""):
    """
    is mobile
    :param value:
    :return:bool
    """
    import re
    return re.match(r"^(((13[0-9]{1})|(14[0-9]{1})|(16[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$",
                    str(value))


def is_ipad(value=""):
    """
    is ipad
    :param value:
    :return:bool
    """
    import re
    return re.search(r"(iPad).*OS\s([\d_]+)", str(value))


def is_iphone(value=""):
    """
    is iphone
    :param value:
    :return:bool
    """
    import re
    return re.search(r"(iPhone\sOS)\s([\d_]+)", str(value)) and not is_ipad(value)


def is_android(value=""):
    """
    is android
    :param value:
    :return:bool
    """
    import re
    return re.search(r"(Android)\s+([\d.]+)", str(value))


def is_wechat(value=""):
    """
    is wechat
    :param value:
    :return:bool
    """
    import re
    return re.search(r"MicroMessenger/i", str(value))


def is_url(value=""):
    """
    is url
    :param value:
    :return:bool
    """
    import re
    return re.match(r"^(http)|(https)://[^\s]*$", str(value))
