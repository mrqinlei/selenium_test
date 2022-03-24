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
    title = ''

    @pytest.fixture(scope='class', autouse=True)
    def __is_login(self, drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()

    @pytest.mark.wiki
    @pytest.mark.main
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

    @pytest.mark.wiki
    @pytest.mark.main
    def test_secondary_page(self,drivers):
        """二级页面切换检查面包屑"""
        wiki = WikiPage(drivers)
        wiki.click_first_wiki_space()
        wiki.click_page_list()
        page_list = wiki.check_page_list()
        wiki.click_recent_visit()
        recent_visit = wiki.check_recent_visit()
        wiki.click_to_star_page()
        star_page = wiki.check_my_star()
        wiki.click_my_draft()
        my_draft = wiki.check_my_draft()
        wiki.click_recycle()
        recycle = wiki.check_recycle()
        wiki.click_settings()
        settings = wiki.check_settings()
        print(page_list,recent_visit,star_page,my_draft,recycle,settings)
        assert page_list == '页面列表' and recent_visit == '最近访问' and star_page == '我的收藏'\
        and my_draft == '我的草稿' and recycle == '回收站' and settings == '设置'

    @pytest.mark.wiki
    @pytest.mark.main
    def test_star_space(self, drivers):
        """空间收藏"""
        # TODO
        pass

    @pytest.mark.wiki
    @pytest.mark.main
    @allure.feature("wiki新建页面")
    def test_create_new_page(self, drivers):
        """新建页面"""
        wiki = WikiPage(drivers)
        wiki.click_page_list()
        sleep(3)
        wiki.click_new_page()
        global title
        title = "ui自动化测试" + str(randint(100, 999))
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

    @pytest.mark.wiki
    @pytest.mark.main
    @allure.feature('收藏按钮')
    def test_star_button(self, drivers):
        """收藏按钮测试"""
        wiki = WikiPage(drivers)
        wiki.click_star_button()
        sleep()
        star_status = wiki.get_star_button_text()
        assert star_status == '取消收藏'

    @pytest.mark.wiki
    @pytest.mark.main
    @allure.feature('关注按钮')
    def test_focus_button(self, drivers):
        """关注按钮测试"""
        wiki = WikiPage(drivers)
        wiki.click_focus_button()
        focus_status = wiki.get_focus_button_text()
        assert focus_status == "取消关注"

    @pytest.mark.wiki
    @pytest.mark.main
    @allure.feature('收藏页面')
    def test_star_page(self, drivers):
        """收藏页面测试"""
        wiki = WikiPage(drivers)
        wiki.click_to_star_page()
        star_page_title = wiki.get_star_title()
        assert 'ui自动化测试' in star_page_title

    @pytest.mark.wiki
    @pytest.mark.main
    def test_create_son_page(self, drivers):
        """增加子页面"""
        wiki = WikiPage(drivers)
        wiki.click_page_list()
        wiki.click_more_function()
        wiki.click_create_son_page()
        son_title = "ui自动化测试子页面" + str(randint(100, 999))
        wiki.add_page_title(son_title)
        content = "ui自动化测试子页面123"
        wiki.add_page_content(content)
        sleep(2)
        wiki.click_son_page_publish()
        assert wiki.check_title() == son_title

    @pytest.mark.wiki
    @pytest.mark.main
    def test_move_to_new_space(self, drivers):
        """移动到新空间"""
        wiki = WikiPage(drivers)
        wiki.click_list_first_page()
        wiki.click_more_function()
        wiki.click_move_to_new_space()
        wiki.click_move_new_space_select()
        wiki.choose_new_space()
        wiki.new_space_confirm()

    @pytest.mark.wiki
    @pytest.mark.main
    def test_delete_page(self, drivers):
        """删除页面"""
        wiki = WikiPage(drivers)
        wiki.click_list_first_page()
        wiki.click_more_function()
        wiki.click_delete_page()
        wiki.confirm_delete()
        res = wiki.check_delete_success()
        assert res is True

    @pytest.mark.wiki
    @pytest.mark.main
    def test_delete_space(self, drivers):
        """删除空间"""
        wiki = WikiPage(drivers)
        wiki.click_settings()
        wiki.click_ops_operation()
        wiki.click_delete_space()
        wiki.confirm_delete_space()








if __name__ == '__main__':
    pytest.main(['TestCase/test_wiki.py'])
