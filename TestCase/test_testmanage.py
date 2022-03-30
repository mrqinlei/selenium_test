#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 2:44 下午
# @File    : test_testmanage.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage

from common.readconfig import ini
from page_object.managetestpage import ManageTest


@allure.feature("测试测试管理模块")
class TestTestManage:

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

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_create_manage_space(self, drivers):
        """创建测试管理空间"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_create_button()
        name, code = 'ui_test' + str(randint(100, 999)), 'ut' + str(randint(100, 999))
        testmange.add_testmanage_content(name, code)
        testmange.click_confirm()
        assert testmange.check_create_success() is not None

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_star_space(self,drivers):
        """收藏空间测试"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_star_space()
        before_star = testmange.get_star_space()
        testmange.click_my_star_space()
        after_star = testmange.get_star_space()
        testmange.click_star_space()
        assert before_star == after_star

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.testmanage
    def test_create_test_case(self, drivers):
        """创建用例"""
        testmange = ManageTest(drivers)
        testmange.click_first_test_space()
        testmange.click_new_case()
        case_name = "这是ui自动化测试"
        testmange.input_case_name(case_name)
        testmange.click_charge_man()
        # testmange.abc()
        # testmange.select_charge_man()  # 选择负责人待优化
        # testmange.move_to_steps()
        testmange.click_create_new_step()
        testmange.input_step(step="步骤一")
        testmange.input_except(except_result="预期结果")
        testmange.click_create_case_confirm()
        testmange.click_first_case()
        test_name = testmange.get_case_name()
        assert test_name == case_name

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.testmanage
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

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_suit_test(self,drivers):
        """测试套件创建"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_my_all_space()
        testmange.click_first_test_space()
        testmange.click_test_suits()
        testmange.click_create_new_test_suits()
        testmange.input_suit_name("ui自动化创建")
        testmange.input_suit_describe("uiui自动化")
        testmange.click_suit_case_list()
        # testmange.choose_case()
        testmange.confirm_suit_case()
        testmange.confirm_create_test_suit()
        suit_name = testmange.get_suit_name()
        assert suit_name == 'ui自动化创建'

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_execute(self,drivers):
        """测试执行创建"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_test_execute()
        testmange.click_create_test_execute()
        testmange.input_execute_name("ui套件")
        testmange.click_execute_suit()
        testmange.choose_execute_suit()
        testmange.input_execute_describe("测试执行说明内容")
        testmange.input_test_version("1")
        testmange.confirm_create_test_execute()

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_suit_fast_execute(self,drivers):
        """测试套件快速执行"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_test_suits()
        testmange.execute_suit()



    @pytest.mark.main
    @pytest.mark.testmanage
    def test_suit_delete(self,drivers):
        """测试套件删除"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_test_suits()
        testmange.delete_suit()

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_secondary_page_crumbs_check(self,drivers):
        """二级页面切换面包屑检查"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_interface_manage()
        interface_crumbs = testmange.check_interface_crumbs()
        testmange.click_case_manage()
        case_manage_crumbs = testmange.check_case_manage_crumbs()
        testmange.click_test_suits()
        test_suit_crumbs = testmange.check_test_suit_crumbs()
        testmange.click_test_plan()
        test_plan_crumbs = testmange.check_test_plan_crumbs()
        testmange.click_test_execute()
        test_execute_crumbs = testmange.check_test_execute_crumbs()
        testmange.click_environment()
        environment_crumbs = testmange.check_environment_manage_crumbs()
        testmange.click_statistics()
        statistics_crumbs = testmange.check_statistics_crumbs()
        testmange.click_settings()
        settings_crumbs = testmange.check_settings_crumbs()
        assert interface_crumbs == '接口管理' and case_manage_crumbs == '用例管理' and test_suit_crumbs == '测试套件'\
            and test_plan_crumbs == '测试计划' and test_execute_crumbs == '测试执行' and environment_crumbs == '环境管理'\
            and statistics_crumbs == '统计' and settings_crumbs == '设置'

    @pytest.mark.main
    @pytest.mark.testmanage
    def test_delete_test_space(self,drivers):
        """删除测试空间"""
        testmange = ManageTest(drivers)
        testmange.click_test_manage()
        testmange.click_settings()
        testmange.click_ops_operation()
        testmange.click_delete_space()
        testmange.confirm_delete()





if __name__ == '__main__':
    pytest.main(['TestCase/test_manage.py'])
