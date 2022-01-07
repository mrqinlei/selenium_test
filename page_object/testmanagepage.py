#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 2:20 下午
# @File    : testmanagepage.py
from page.webpage import WebPage, sleep
from common.readelement import Element

testmanage = Element('testmanage')

class TestManage(WebPage):
    """测试管理类"""

    def click_test_manage(self):
        """点击测试管理"""
        self.is_click(testmanage['测试管理'])

    def click_create_button(self):
        """点击新建"""
        self.is_click(testmanage['新建'])

    def add_testmanage_content(self,name,code):
        """填写测试管理空间信息"""
        self.input_text(testmanage['空间名称'],name)
        self.input_text(testmanage['英文标识'],code)

    def click_confirm(self):
        """点击确定"""
        self.is_click(testmanage['确定'])

    def check_create_success(self):
        """检查创建成功"""
        return self.is_exists(testmanage['全部'])
