#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 2:20 下午
# @File    : managetestpage.py
from page.webpage import WebPage, sleep
from common.readelement import Element

testmanage = Element('managetest')


class ManageTest(WebPage):
    """测试管理类"""

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

    def select_charge_man(self):
        """选择负责人"""
        self.is_click(testmanage['选择负责人'])

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
