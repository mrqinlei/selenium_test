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

    def personal_settings_name(self):
        """创建成功后跳转个人设置，查看个人设置项目名称"""
        return self.element_text(project['个人设置项目名称'])

    def click_project_plan(self):
        """点击项目名称跳转"""
        self.is_click(project['产品规划'])

    def click_new_plan(self):
        """点击新增规划"""
        self.is_click(project['新建规划'])

    def add_plan_name(self, planname):
        """输入计划名称"""
        self.input_text(project['规划名称'], planname)

    def click_confirm_create_plan(self):
        """点击确定创建计划"""
        self.is_click(project['规划确定'])

    def check_create_plan_success(self):
        """检查创建计划成功"""
        self.is_exists(project['创建成功'])

    def click_plan_and_board(self):
        """点击计划与看板"""
        self.is_click(project['计划与看板'])

    def click_create_card(self):
        """点击创建卡片"""
        self.is_click(project['新建卡片'])

    def add_card_title(self, title, content):
        """输入卡片标题"""
        self.input_text(project['卡片标题'], title)
        self.input_text(project['卡片内容'], content)

    def click_confirm_create_card(self):
        """点击确定创建卡片"""
        self.is_click(project['卡片确定'])

    def check_card_create_success(self):
        """检查卡片创建成功"""
        return self.is_exists(project['卡片title'])

    def get_first_project_name(self):
        """获得第一个项目的名称"""
        return self.element_text(project['获得项目名称'])

    def click_star_button(self):
        """点击收藏按钮"""
        self.is_click(project['收藏按钮'])

    def click_my_star(self):
        """点击我的收藏"""
        self.is_click(project['我的收藏'])

    def get_relation_wiki(self):
        """悬停获得关联icon"""
        self.move_and_stay(project['获得项目名称'])

    def click_relation_wiki_icon(self):
        """点击关联wiki的icon"""
        self.is_click(project['关联wiki'])

    def click_relation_wiki_button(self):
        """点击关联wiki的button"""
        self.is_click(project['关联wiki空间'])

    def click_wiki_space(self):
        """"点击关联下拉框"""
        self.is_click(project['选择wiki空间'])


    def click_first_wiki_item(self):
        """选择第一个wiki空间"""
        self.is_click(project['确定wiki空间'])


    def get_select_wiki_space_name(self):
        """获取第一个空间的名称"""
        return self.element_text(project['确定wiki空间'])

    def get_relation_wiki_space_name(self):
        """获取关联成功后第一个wiki空间名称"""
        return self.element_text(project['关联后wiki空间名称'])
