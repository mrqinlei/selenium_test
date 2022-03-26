#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 3:51 下午
# @File    : loginpage.py

from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class LoginPage(WebPage):
    """登录类"""

    def click_login(self):
        """点击登录"""
        self.is_click(login['pre登录'])

    def input_acount(self,content):
        """输入账号"""
        self.input_text(login['账号'],txt=content)

    def input_passwd(self,content):
        """输入密码"""
        self.input_text(login['密码'],txt=content)

    def submit_login(self):
        """点击登录"""
        self.is_click(login['true登录'])

    def login_success(self):
        """判断是否登录成功"""
        return self.is_exists(login['进入工作台'])


    def click_enter_workspace(self):
        """点击进入工作台"""
        self.is_click(login['进入工作台'])

    def login_fail_alert(self):
        """登录失败提示"""
        return self.is_exists(login['失败提示'])



    def quit_login(self):
        """退出登录"""
        self.is_click('右上角名称')
        self.is_click('退出登录')