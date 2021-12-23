#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 4:30 下午
# @File    : test_login.py
import re
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.homepage import HomePage
from common.readconfig import ReadConfig
import time


@allure.feature("测试简单云登录模块")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_ezone(self, drivers):
        '''打开ezone网页'''
        login = HomePage(drivers)
        login.get_url(ini.url)

    @allure.story("点击登录用例")
    def test_001(self, drivers):
        """点击登录"""
        login = HomePage(drivers)
        login.click_login()
        login.input_acount('qinlei')
        login.input_passwd('jiandanyidian123456')
        login.submit_login()
        time.sleep(7)


if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
