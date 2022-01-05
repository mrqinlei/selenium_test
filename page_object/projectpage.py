#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 3:37 下午
# @File    : projectpage.py
from page.webpage import WebPage, sleep
from common.readelement import Element

project = Element('project')
login = Element('login')


class ProjectPage(WebPage):
    """project类"""
    def click_enter_workspace(self):
        """点击进入工作台"""
        self.is_click(login['进入工作台'])

    def click_project(self):
        """点击项目管理"""
        self.is_click(project['项目管理'])

    def add_project(self):
        """新建项目"""
        self.is_click(project['新建'])

    def add_project_content(self, name, code):
        """填写项目信息"""
        self.input_text(project['项目名称'], name)
        self.input_text(project['英文标识'], code)

    def click_project_template(self):
        """点击项目模板"""
        self.is_click(project['项目模板'])

    # def locate_project_template(self):
    #     """定位模板下拉框"""
    #     return self.find_element(project['项目模板'])

    def select_project_template(self):
        """选择则项目模板"""
        self.is_click(project['软件研发模板选项'])

    def confirm_create_project(self):
        """点击确定创建按钮"""
        self.is_click(project['新建项目确定'])

    def check_create_result(self):
        """查看创建项目结果"""
        return self.element_text(project['项目名称列表'])

    def personal_settings_name(self):
        """创建成功后跳转个人设置，查看个人设置项目名称"""
        return self.element_text(project['个人设置项目名称'])

