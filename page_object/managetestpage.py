#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 2:20 下午
# @File    : managetestpage.py
from selenium.webdriver import Keys

from page.webpage import WebPage, sleep
from common.readelement import Element

testmanage = Element('managetest')


class ManageTest(WebPage):
    """测试管理类"""

    def __init__(self, driver):
        super().__init__(driver)
        self.switch_to = None

    def click_test_manage(self):
        """点击测试管理"""
        self.is_click(testmanage['测试管理'])

    def click_create_button(self):
        """点击新建"""
        self.is_click(testmanage['新建'])

    def add_testmanage_content(self, name, code):
        """填写测试管理空间信息"""
        self.input_text(testmanage['空间名称'], name)
        self.input_text(testmanage['英文标识'], code)

    def click_confirm(self):
        """点击确定"""
        self.is_click(testmanage['确定'])

    def check_create_success(self):
        """检查创建成功"""
        return self.is_exists(testmanage['全部'])

    def click_first_test_space(self):
        """点击第一个测试空间"""
        self.is_click(testmanage['第一个空间'])

    def click_new_case(self):
        """点击创建用例"""
        self.is_click(testmanage['新建用例'])

    def input_case_name(self, case_name):
        """输入用例名称"""
        self.input_text(testmanage['用例名称'], case_name)

    def click_charge_man(self):
        """点击负责人"""
        self.is_click(testmanage['负责人'])

    def input_charge_man(self, charge_man):
        """输入负责人"""
        self.input_text(testmanage['输入负责人'], charge_man)

    def select_charge_man(self):
        """选择负责人"""
        self.is_click(testmanage['选择负责人'])

    def move_to_steps(self):
        """"""
        self.move_and_stay(testmanage['新增步骤'])

    def click_create_new_step(self):
        """点击新增步骤"""
        self.is_click(testmanage['新增步骤'])

    def input_step(self, step):
        """输入步骤"""
        self.input_text(testmanage['步骤1'], step)

    def input_except(self, except_result):
        """输入预期结果"""
        self.input_text(testmanage['预期1'], except_result)

    def click_create_case_confirm(self):
        """点击确定创建"""
        self.is_click(testmanage['确定创建用例'])

    def click_first_case(self):
        """点击空间第一条用例"""
        self.is_click(testmanage['第一条用例'])

    def get_case_name(self):
        """获得第一条用例名称"""
        return self.get_attribute(testmanage['用例名称'])

    def click_interface_manage(self):
        """点击接口管理"""
        self.is_click(testmanage['接口管理'])

    def click_create_interface(self):
        """点击新建接口"""
        self.is_click(testmanage['新建接口按钮'])

    def input_interface_name(self, interface_name):
        """输入接口名称"""
        self.input_text(testmanage['接口名称'], interface_name)

    def input_url(self, url):
        """输入接口uri"""
        self.input_text(testmanage['URL'], url)

    def confirm_create_interface(self):
        """确定创建接口"""
        self.is_click(testmanage['确定创建接口'])

    def click_member(self):
        """点击选择成员"""
        self.is_click(testmanage['添加成员'])

    def select_member(self):
        """选择成员"""
        self.is_click(testmanage['选择成员'])

    def abc(self):
        """"""
        self.move_to_location()

    def click_settings(self):
        """点击设置"""
        self.is_click(testmanage['设置'])

    def click_ops_operation(self):
        """点击运维操作"""
        self.is_click(testmanage['运维操作'])

    def click_delete_space(self):
        """点击删除空间"""
        self.is_click(testmanage['删除空间'])

    def confirm_delete(self):
        """确认删除"""
        self.is_click(testmanage['确认删除'])

    def click_star_space(self):
        """点击收藏按钮"""
        self.is_click(testmanage['收藏'])

    def get_star_space(self):
        """获得收藏空间英文标识"""
        return self.element_text(testmanage['空间英文标识'])

    def click_my_star_space(self):
        """点击我的收藏空间"""
        self.is_click(testmanage['我的收藏'])

    def click_test_suits(self):
        """点击测试套件"""
        self.is_click(testmanage['测试套件'])

    def click_create_new_test_suits(self):
        """点击创建测试套件"""
        self.is_click(testmanage['新建套件'])

    def input_suit_name(self,suit_name):
        """输入套件名称"""
        self.input_text(testmanage['名称'],suit_name)

    def input_suit_describe(self,suit_describe):
        """输入套件说明"""
        self.input_text(testmanage['说明'],suit_describe)

    def click_suit_case_list(self):
        """编辑套件用例列表"""
        self.is_click(testmanage['编辑用例列表'])

    def choose_case(self):
        """选择用例"""
        self.is_click(testmanage['勾选'])

    def confirm_suit_case(self):
        """确认套件用例"""
        self.is_click(testmanage['确定用例'])

    def confirm_create_test_suit(self):
        """确认创建用例套件"""
        self.is_click(testmanage['确定创建套件'])

    def get_suit_name(self):
        """获得套件名称"""
        return self.element_text(testmanage['套件名称'])

    def execute_suit(self):
        """快速执行"""
        self.is_click(testmanage['测试套件快速执行'])

    def delete_suit(self):
        """删除套件"""
        self.is_click(testmanage['删除套件'])

    def check_interface_crumbs(self):
        """接口管理面包屑"""
        return self.element_text(testmanage['接口管理面包屑'])

    def check_case_manage_crumbs(self):
        """用例管理面包屑"""
        return self.element_text(testmanage['用例管理面包屑'])

    def check_test_suit_crumbs(self):
        """测试套件面包屑"""
        return self.element_text(testmanage['测试套件面包屑'])

    def check_test_plan_crumbs(self):
        """测试计划面包屑"""
        return self.element_text(testmanage['测试计划面包屑'])

    def check_test_execute_crumbs(self):
        """测试执行面包屑"""
        return self.element_text(testmanage['测试执行面包屑'])

    def check_environment_manage_crumbs(self):
        """环境管理面包屑"""
        return self.element_text(testmanage['环境管理面包屑'])

    def check_statistics_crumbs(self):
        """统计面包屑"""
        return self.element_text(testmanage['统计面包屑'])

    def check_settings_crumbs(self):
        """设置面包屑"""
        return self.element_text(testmanage['设置面包屑'])

    def click_case_manage(self):
        """点击用例管理"""
        self.is_click(testmanage['用例管理'])

    def click_test_plan(self):
        """点击测试计划"""
        self.is_click(testmanage['测试计划'])

    def click_test_execute(self):
        """点击测试执行"""
        self.is_click(testmanage['测试执行'])

    def click_environment(self):
        """点击环境管理"""
        self.is_click(testmanage['环境管理'])

    def click_statistics(self):
        """点击统计"""
        self.is_click(testmanage['统计'])


    def click_create_test_execute(self):
        """点击新建测试执行"""
        self.is_click(testmanage['新建测试执行'])

    def input_execute_name(self,execute_name):
        """测试执行名称"""
        self.input_text(testmanage['测试执行名称'],execute_name)

    def click_execute_suit(self):
        """点击测试执行的测试套件"""
        self.is_click(testmanage['测试套件选择'])

    def choose_execute_suit(self):
        """选择执行的套件"""
        self.is_click(testmanage['套件选择'])

    def input_execute_describe(self,execute_describe):
        """输入执行的说明"""
        self.input_text(testmanage['测试执行说明'],execute_describe)

    def input_test_version(self,test_version):
        """输入测试版本"""
        self.input_text(testmanage['测试版本'],test_version)

    def confirm_create_test_execute(self):
        """确定创建测试执行"""
        self.is_click(testmanage['确定创建执行'])

    def click_my_all_space(self):
        """点击我的全部"""
        self.is_click(testmanage['我的全部'])
