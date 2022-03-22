#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:22 上午
# @File    : test_wiki.py
from random import randint

import pytest
import allure
from selenium.webdriver import Keys

from page_object.loginpage import LoginPage
from utils.logger import log
from common.readconfig import ini
from page_object.wikipage import WikiPage
from common.readconfig import ReadConfig
from utils.times import sleep


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

    @allure.feature("wiki新建页面")
    def test_create_new_page(self,drivers):
        """新建页面"""
        wiki = WikiPage(drivers)
        wiki.click_first_wiki_space()
        wiki.click_page_list()
        sleep(3)
        wiki.click_new_page()
        title = "ui自动化测试"
        wiki.add_page_title(title)
        content = "ui自动化测试123"
        wiki.add_page_content(content)
        wiki.input_font_bold()
        wiki.add_to_page_content(content)
        wiki.click_enter()
        wiki.input_font_itali()
        wiki.add_to_page_content(content)
        wiki.click_enter()
        wiki.input_del_font()
        wiki.add_to_page_content(content)
        wiki.click_enter()
        wiki.input_highlight_font()
        wiki.add_to_page_content(content)
        wiki.click_enter()
        wiki.input_incode()
        wiki.add_to_page_content(content)
        sleep(1)
        wiki.click_enter()
        wiki.click_input_link()
        link = "https://baiudu/com"
        sleep(1)
        # wiki.input_link(link)
        wiki.click_enter()
        wiki.click_publish_button()
        assert wiki.check_title() == title

    @allure.feature('收藏按钮')
    def test_star_button(self,drivers):
        """收藏按钮测试"""
        wiki = WikiPage(drivers)
        wiki.click_star_button()
        sleep()
        star_status = wiki.get_star_button_text()
        assert star_status == '取消收藏'

    @allure.feature('关注按钮')
    def test_focus_button(self,drivers):
        """关注按钮测试"""
        wiki = WikiPage(drivers)
        wiki.click_focus_button()
        focus_status = wiki.get_focus_button_text()
        assert focus_status == "取消关注"

    @allure.feature('收藏页面')
    def test_star_page(self,drivers):
        """收藏页面测试"""
        wiki = WikiPage(drivers)
        wiki.click_to_star_page()
        star_page_title = wiki.get_star_title()
        assert star_page_title == "ui自动化测试"


if __name__ == '__main__':
    pytest.main(['TestCase/test_wiki.py'])
