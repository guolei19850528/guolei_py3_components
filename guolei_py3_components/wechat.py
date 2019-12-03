#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests, json
from .util import get_random_str, get_timestamp, get_md5_str, get_sha1_str


class Wehcat:
    def __init__(self, app_id="", app_secret=""):
        self._app_id = app_id
        self._app_secret = app_secret

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        self._app_id = app_id
        return

    @property
    def app_secret(self):
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        self._app_secret = app_secret
        return

    def get_access_token(self):
        """
        get access token
        :return:
        """
        assert isinstance(self.app_id, str) and len(self.app_id), "app_id must string and not empty"
        assert isinstance(self.app_secret, str) and len(self.app_secret), "app_secret must string and not empty"
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}".format(
            app_id=self.app_id, app_secret=self.app_secret)
        response = requests.get(url=url, timeout=30)
        if response.status_code == 200:
            result = json.loads(response.text)
            if result and isinstance(result, dict) and len(result):
                access_token = result["access_token"] if "access_token" in result else None
                return access_token
        return None

    def get_js_api_ticket(self, access_token=""):
        """
        get js api ticket
        :param access_token:
        :return:
        """
        assert isinstance(self.app_id, str) and len(self.app_id), "app_id must string and not empty"
        assert isinstance(self.app_secret, str) and len(self.app_secret), "app_secret must string and not empty"
        assert isinstance(access_token, str) and len(access_token), "access_token must string and not empty"
        url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={access_token}&type=jsapi".format(
            access_token=access_token)
        response = requests.get(url=url, timeout=30)
        if response.status_code == 200:
            result = json.loads(response.text)
            if result and isinstance(result, dict) and len(result):
                js_api_ticket = result["ticket"] if "ticket" in result else None
                return js_api_ticket
        return None

    def get_signatures(self, js_api_ticket="", url="", type="shar1"):
        """
        get signatures
        :param js_api_ticket:
        :param url:
        :param type:
        :return:
        """
        nonce_str = get_random_str(64);
        timestamp = get_timestamp();
        str1 = "jsapi_ticket={js_api_ticket}&noncestr={nonce_str}&timestamp={timestamp}&url={url}".format(
            js_api_ticket=js_api_ticket, nonce_str=nonce_str, timestamp=timestamp, url=url)
        signature = get_sha1_str(str1);
        if type == "md5":
            signature = get_md5_str(str1)
        return {
            "nonce_str": nonce_str,
            "signature": signature,
            "timestamp": timestamp
        }

    def get_code_url(self, url=""):
        """
        get code url
        :param url:
        :return:
        """
        assert isinstance(url, str) and len(url), "url must string and not empty"
        import urllib.parse
        return "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri={url}&response_type=code&scope=snsapi_base&state=1#wechat_redirect".format(
            url=urllib.parse.urlencode(url))

    def get_open_id(self, code=""):
        """
        get open id
        :param code:
        :return:
        """
        assert isinstance(self.app_id, str) and len(self.app_id), "app_id must string and not empty"
        assert isinstance(self.app_secret, str) and len(self.app_secret), "app_secret must string and not empty"
        assert isinstance(code, str) and len(code), "code must string and not empty"
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={app_id}&secret={app_secret}&code={code}&grant_type=authorization_code".format(
            app_id=self.app_id, app_secret=self.app_secret, code=code)
        response = requests.get(url=url, timeout=30)
        if response.status_code == 200:
            result = json.loads(response.text)
            if result and isinstance(result, dict) and len(result):
                open_id = result["openid"] if "openid" in result else None
                return open_id
        return None
