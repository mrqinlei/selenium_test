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

    # def is_login(self, request, drivers):
    #     login = LoginPage(drivers)
    #     login.username('admin')
    #     login.password('Admin123456')
    #     login.submit()
    #     sleep(3)
    @allure.feature("新建项目用例")
    def test_create_project(self, drivers):
        """新建项目测试"""
        project = ProjectPage(drivers)
        project.click_enter_workspace()
        project.click_project()
        project.add_project()
        name, code = 'ui_test'+ str(randint(100,99)), 'ut'+ str(randint(10,99))
        project.add_project_content(name, code)
        project.click_project_template()
        project.select_project_template()
        project.confirm_create_project()
        res = project.personal_settings_name()
        log.info(res)
        print(res)
        assert res == name


if __name__ == '__main__':
    pytest.main(['TestCase/test_project.py'])
