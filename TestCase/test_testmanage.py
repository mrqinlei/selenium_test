#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 2:44 下午
# @File    : test_testmanage.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage
from utils.logger import log
from utils.times import sleep
from common.readconfig import ini
from page_object.managetestpage import ManageTest
from common.readconfig import ReadConfig


@allure.feature("测试测试管理模块")
class TestTestManage:

    # @pytest.fixture(scope='class', autouse=True)
    # def __is_login(self, drivers):
    #     """点击登录"""
    #     login = LoginPage(drivers)
    #     login.get_url(ini.url)
    #     login = LoginPage(drivers)
    #     login.click_login()
    #     login.input_acount(ini.account)
    #     login.input_passwd(ini.password)
    #     login.submit_login()

    @pytest.mark.main
    def test_create_manage(self, drivers):
        """创建测试管理空间"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_create_button()
        name, code = 'ui_test' + str(randint(100, 999)), 'ut' + str(randint(100, 999))
        testmange.add_testmanage_content(name, code)
        testmange.click_confirm()
        assert testmange.check_create_success() is not None

    @pytest.mark.main
    def test_create_card(self, drivers):
        """创建用例"""
        testmange = ManageTest(drivers)
        testmange.click_first_test_space()
        testmange.click_new_case()
        case_name = "这是ui自动化测试"
        testmange.input_case_name(case_name)
        testmange.click_charge_man()
        testmange.click_charge_man()  # 选择负责人待优化
        testmange.click_create_new_step()
        testmange.input_step(step="步骤一")
        testmange.input_except(except_result="预期结果")
        testmange.click_create_case_confirm()
        testmange.click_first_case()
        test_name = testmange.get_case_name()
        assert test_name == case_name

    @pytest.mark.main
    def test_create_interface(self,drivers):
        """创建接口"""
        testmange = ManageTest(drivers)
        testmange.click_first_test_space()  #如果创建用例被注释则打开
        testmange.click_interface_manage()
        testmange.click_create_interface()
        interface_name = "ui自动化测试输入接口"
        testmange.input_interface_name(interface_name)
        url = "test/api/v1"
        testmange.input_url(url)
        testmange.click_member()
        testmange.select_member()  # 选择负责人待优化
        testmange.confirm_create_interface()



if __name__ == '__main__':
    pytest.main(['TestCase/test_manage.py'])
