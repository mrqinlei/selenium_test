#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 3:51 下午
# @File    : homepage.py

from page.webpage import WebPage, sleep
from common.readelement import Element

homepage = Element('homepage')


class HomePage(WebPage):
    """首页"""

    def click_login(self):
        """点击登录"""
        self.is_click(homepage['pre登录'])

    def input_acount(self,content):
        """输入账号"""
        self.input_text(homepage['账号'],txt=content)
        sleep()

    def input_passwd(self,content):
        """输入密码"""
        self.input_text(homepage['密码'],txt=content)
        sleep()

    def submit_login(self):
        """点击登录"""
        self.is_click(homepage['true登录'])
        sleep(5)

