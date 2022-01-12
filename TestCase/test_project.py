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

    # @pytest.fixture(scope='class', autouse=True)
    # def is_login(self, drivers):
    #     """点击登录"""
    #     login = LoginPage(drivers)
    #     login.get_url(ini.url)
    #     login = LoginPage(drivers)
    #     login.click_login()
    #     login.input_acount(ini.account)
    #     login.input_passwd(ini.password)
    #     login.submit_login()
    #     login.click_enter_workspace()

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






if __name__ == '__main__':
    pytest.main(['TestCase/test_project.py'])
