#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import parseaddr, formataddr


class Mail(object):
    """
    邮件发送类
    """

    def __init__(self):
        # sender account
        self._sender_account = ""
        # sender name
        self._sender_name = ""
        # sender password
        self._sender_password = ""
        # smtp host
        self._smtp_host = ""
        # smtp port
        self._smtp_port = 0
        # to addresses
        self._to_addresses = []
        # cc addresses
        self._cc_addresses = []
        # bcc addresses
        self._bcc_addresses = []
        return

    @property
    def sender_account(self):
        return self._sender_account

    @sender_account.setter
    def sender_account(self, sender_account):
        self._sender_account = sender_account
        return

    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        self._sender_name = sender_name
        return

    @property
    def sender_password(self):
        return self._sender_password

    @sender_password.setter
    def sender_password(self, sender_password):
        self._sender_password = sender_password
        return

    @property
    def smtp_host(self):
        return self._smtp_host

    @smtp_host.setter
    def smtp_host(self, smtp_host):
        self._smtp_host = smtp_host
        return

    @property
    def smtp_port(self):
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        self._smtp_port = smtp_port
        return

    @property
    def to_addresses(self):
        return self._to_addresses

    @to_addresses.setter
    def to_addresses(self, to_addresses):
        self._to_addresses = to_addresses
        return

    @property
    def cc_addresses(self):
        return self._cc_addresses

    @cc_addresses.setter
    def cc_addresses(self, cc_addresses):
        self._cc_addresses = cc_addresses
        return

    @property
    def bcc_addresses(self):
        return self._bcc_addresses

    @bcc_addresses.setter
    def bcc_addresses(self, bcc_addresses):
        self._bcc_addresses = bcc_addresses
        return

    def smtp_send_mail(self, subject="", message="", attachments=[], sub_type="plain", charset="utf-8",
                       timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """
        smtp send mail
        :param subject:
        :param message:
        :param attachments:
        :param sub_type:
        :param charset:
        :param timeout:
        :return:
        """
        try:
            with smtplib.SMTP(host=self.smtp_host, port=self.smtp_port) as smtp_obj:
                smtp_obj.login(self.sender_account, self.sender_password)
                smtp_obj.timeout = timeout
                message_obj = MIMEMultipart()
                message_obj["From"] = formataddr(parseaddr(self._sender_name))
                message_obj["Subject"] = subject
                message_obj.attach(MIMEText(message, sub_type, charset))
                if self.cc_addresses and isinstance(self.cc_addresses, list) and len(self.cc_addresses):
                    message_obj["Cc"] = ",".join(self.cc_addresses)
                if self.bcc_addresses and isinstance(self.bcc_addresses, list) and len(self.bcc_addresses):
                    message_obj["Bcc"] = ",".join(self.bcc_addresses)
                if attachments and isinstance(attachments, list) and len(attachments):
                    for attachment in attachments:
                        attachment_path = attachment["path"]
                        attachment_name = attachment["name"]
                        attachment_obj = MIMEApplication(open(attachment_path, "rb").read())
                        attachment_obj.add_header("Content-Disposition", "attachment", filename=attachment_name)
                        message_obj.attach(attachment_obj)
                smtp_obj.sendmail(self.sender_account, self.to_addresses,
                                  message_obj.as_string())
                return True
        except Exception as error:
            return False

    def smtp_ssl_send_mail(self, subject="", message="", attachments=[], sub_type="plain", charset="utf-8",
                           timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """
        smtp ssl send mail
        :param subject:
        :param message:
        :param attachments:
        :param sub_type:
        :param charset:
        :param timeout:
        :return:
        """
        try:
            with smtplib.SMTP_SSL(host=self.smtp_host, port=self.smtp_port) as smtp_ssl_obj:
                smtp_ssl_obj.login(self.sender_account, self.sender_password)
                smtp_ssl_obj.timeout = timeout
                message_obj = MIMEMultipart()
                message_obj["From"] = formataddr(parseaddr(self._sender_name))
                message_obj["Subject"] = subject
                message_obj.attach(MIMEText(message, sub_type, charset))
                if self.cc_addresses and isinstance(self.cc_addresses, list) and len(self.cc_addresses):
                    message_obj["Cc"] = ",".join(self.cc_addresses)
                if self.bcc_addresses and isinstance(self.bcc_addresses, list) and len(self.bcc_addresses):
                    message_obj["Bcc"] = ",".join(self.bcc_addresses)
                if attachments and isinstance(attachments, list) and len(attachments):
                    for attachment in attachments:
                        attachment_path = attachment["path"]
                        attachment_name = attachment["name"]
                        attachment_obj = MIMEApplication(open(attachment_path, "rb").read())
                        attachment_obj.add_header("Content-Disposition", "attachment", filename=attachment_name)
                        message_obj.attach(attachment_obj)
                smtp_ssl_obj.sendmail(self.sender_account, self.to_addresses,
                                      message_obj.as_string())
                return True
        except Exception as error:
            return False
