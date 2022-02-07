#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 4:58 下午
# @File    : test_project.py
import re
from random import randint

import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.projectpage import ProjectPage
from page_object.loginpage import LoginPage
from common.readconfig import ReadConfig
from utils.times import sleep



@allure.feature("测试项目模块")
class TestProject:

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

    @allure.feature("新建项目用例")
    def test_create_project(self, drivers):
        """新建项目测试"""
        project = ProjectPage(drivers)
        project.click_project()
        project.add_project()
        name, code = 'ui_test'+ str(randint(100,999)), 'ut'+ str(randint(100,999))
        project.add_project_content(name, code)
        project.click_project_template()
        project.select_project_template()
        project.confirm_create_project()
        res = project.personal_settings_name()
        log.info(res)
        print(res)
        assert res == name

    @allure.feature("新建卡片用例")
    def test_create_card(self,drivers):
        """新建卡片用例"""
        project = ProjectPage(drivers)
        project.click_plan_and_board()
        project.click_create_card()
        project.add_card_title(title='ui自动化测试',content='ui自动化测试')
        project.click_confirm_create_card()
        assert project.check_card_create_success() is not None
        # assert res == 'ui自动化测试'

    @allure.feature("新建规划用例")
    def test_create_plan(self,drivers):
        """新建规划"""
        project = ProjectPage(drivers)
        project.click_project_plan()
        project.click_new_plan()
        project.add_plan_name(planname='uitestplan')
        project.click_confirm_create_plan()
        assert project.check_create_plan_success is not None

    @allure.feature("项目收藏用例")
    def test_project_star(self,drivers):
        """收藏功能"""
        project = ProjectPage(drivers)
        project.click_project()
        before_star_name = project.get_first_project_name()
        project.click_star_button()
        project.click_my_star()
        after_star_name = project.get_first_project_name()
        print(before_star_name,after_star_name)
        assert before_star_name == after_star_name

    def test_project_relation_wiki(self,drivers):
        """项目管理列表关联wiki功能"""
        project = ProjectPage(drivers)
        project.click_project()
        project.get_relation_wiki()
        project.click_relation_wiki_icon()
        project.click_relation_wiki_button()
        project.click_wiki_space()
        before_relation_wiki_name = project.get_select_wiki_space_name()
        project.click_first_wiki_item()
        after_relation_wiki_name = project.get_relation_wiki_space_name()
        print(before_relation_wiki_name,after_relation_wiki_name)




if __name__ == '__main__':
    pytest.main(['TestCase/test_project.py'])
