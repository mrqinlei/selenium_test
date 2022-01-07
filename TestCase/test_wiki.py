#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:22 上午
# @File    : test_wiki.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage
from utils.logger import log
from common.readconfig import ini
from page_object.wikipage import WikiPage
from common.readconfig import ReadConfig


@allure.feature("测试wiki模块")
class TestWiki:

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
        login.click_enter_workspace()

    @allure.feature("新建wiki用例")
    def test_create_wiki_space(self, drivers):
        """新建wiki空间测试"""
        wiki = WikiPage(drivers)
        wiki.click_wiki()
        wiki.click_create_wiki_space()
        name, code = 'ui_test' + str(randint(100, 999)), 'ut' + str(randint(100, 999))
        wiki.add_wiki_content(name, code)
        wiki.click_confirm()
        # fr = open('../page_element/wiki.yaml', 'a')
        # xpath = "\"xpath==//span[contains(text(),'%s')]\"" % name
        # data = {"wikibutton": xpath}
        # yaml.dump(data, fr)
        # wiki.click_wiki_name()
        # res = wiki.check_wiki_name()
        # print(res)
        assert wiki.all_button_exists() is not None



if __name__ == '__main__':
    pytest.main(['TestCase/test_wiki.py'])
