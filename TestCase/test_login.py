#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 4:30 下午
# @File    : test_login.py
import re
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage
from common.readconfig import ReadConfig
from utils.times import sleep


@allure.feature("测试简单云登录模块")
class TestLogin:

    @pytest.mark.main
    @pytest.mark.login
    @pytest.mark.project
    @pytest.fixture(scope='function', autouse=True)
    def open_ezone(self, drivers):
        '''打开ezone网页'''
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @pytest.mark.main
    @pytest.mark.login
    @pytest.mark.project
    @allure.story("点击登录用例")
    def test_login(self, drivers):
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
            assert res is not None
        elif login.login_success():
            assert login.login_success() is True


if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
