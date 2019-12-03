#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from .util import *
import requests
import json


def get_ip_data(ip=""):
    """
    get ip data
    :param ip:
    :return:
    """
    assert isinstance(ip, str) and len(ip), "ip must string and not empty"
    if ip and isinstance(ip, str) and len(ip):
        url = "http://ip.taobao.com/service/getIpInfo.php?ip={ip}&_t={t}".format(ip=ip, t=get_timestamp())
        response = requests.get(
            url=url, timeout=30)
        if response.status_code == 200:
            return json.loads(response.text)
    return None
