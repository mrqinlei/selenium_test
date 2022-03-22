#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 5:17 下午
# @File    : test_coderepository.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage
from page_object.projectpage import project
from utils.logger import log
from common.readconfig import ini
from page_object.coderepository import CodeRepositoryPage
from common.readconfig import ReadConfig
from utils.times import sleep

@allure.feature("测试code模块")
class TestcodeRepository:

    @pytest.fixture(scope='class', autouse=True)
    def is_login(self, drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()

    @allure.feature("新建代码库用例")
    def test_create_wiki_space(self, drivers):
        """新建代码库测试"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_coderepository()
        coderepository.click_create_coderepository()
        dirname, name = 'ui_test','ut'
        coderepository.add_coderepository_content(dirname,name)
        coderepository.click_confirm()
        assert coderepository.check_coderepository_name() == name


if __name__ == '__main__':
    pytest.main(['TestCase/test_coderepository.py'])
