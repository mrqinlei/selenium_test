#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 10:17 上午
# @File    : login.py
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage
from common.readconfig import ReadConfig
from utils.times import sleep

class LoginClass:

    def open_ezone(self, drivers):
        '''打开ezone网页'''
        login = LoginPage(drivers)
        login.get_url(ini.url)

    def login(self,drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()
        sleep()
        res = login.login_fail_alert()
        # login.click_enter_workspace()
        if res:
            # assert res == "连续失败5次，请15分钟之后再试"
            print("登录失败")
        elif login.login_success():
            print("登陆成功")