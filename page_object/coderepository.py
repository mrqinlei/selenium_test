#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 5:01 下午
# @File    : coderepository.py
from page.webpage import WebPage, sleep
from common.readelement import Element

code = Element('coderepository')


class CodeRepositoryPage(WebPage):
        """代码库类"""


        def click_coderepository(self):
            """点击代码库"""
            self.is_click(code['代码库'])

        def click_create_coderepository(self):
            """点击新建代码库"""
            self.is_click(code['新建代码库'])

        def add_coderepository_content(self,dirname,name,):
            """填写目录名和代码库名"""
            self.input_text(code['目录名'], dirname)
            self.input_text(code['代码库名'], name)

        def click_confirm(self):
            """点击确认"""
            self.is_click(code['确定'])

        def check_coderepository_name(self):
            """创建成功后检查代码库姓名"""
            return self.element_text(code['代码库名检查'])


