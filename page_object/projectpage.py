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
        self.move_and_stay(project['项目列表首个项目'])

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

    def click_close_relate_windows(self):
        """关闭关联浮窗"""
        self.is_click(project['关闭关联浮窗'])

    def click_settings(self):
        """点击设置"""
        self.is_click(project['设置'])

    def click_ops_operation(self):
        """点击运维"""
        self.is_click(project['运维操作'])

    def click_delete_project(self):
        """点击删除项目"""
        self.is_click(project['删除项目'])

    def input_password(self,password):
        """输入登录密码"""
        self.input_text(project['输入登录密码'],password)

    def click_confirm_delete(self):
        """点击确认删除"""
        self.is_click(project['确认删除'])

    def click_first_project(self):
        """点击列表首个项目"""
        self.is_click(project['项目列表首个项目'])

    def click_first_card(self):
        """点击首张卡片"""
        self.is_click(project['首张卡片'])

    def click_card_status(self):
        """点击卡片状态"""
        self.is_click(project['卡片状态'])

    def click_status_doing(self):
        """选择进行中"""
        self.is_click(project['进行中'])

    def check_card_status(self):
        """检查卡片状态"""
        return self.element_text(project['卡片状态检查'])

    def click_card_detail_more_function(self):
        """点击卡片详情更多功能"""
        self.is_click(project['卡片详情更多功能'])

    def click_block_button(self):
        """点击阻塞"""
        self.is_click(project['阻塞'])

    def click_block_switch(self):
        """打开阻塞开关"""
        self.is_click(project['阻塞开关'])

    def input_block_content(self,block_content):
        """输入阻塞内容"""
        self.input_text(project['阻塞内容'],block_content)

    def confirm_block(self):
        """点击确定阻塞"""
        self.is_click(project['确定阻塞'])

    def click_block_success(self):
        """检查阻塞设置成功"""
        self.is_click(project['检查阻塞'])

    def check_block(self):
        """检查阻塞打开成功"""
        return self.element_text(project['阻塞内容'])

    def click_create_plan(self):
        """新建计划"""
        self.is_click(project['新建计划'])

    def input_plan_name(self,plan_name):
        """输入计划名称"""
        self.input_text(project['计划名称'],plan_name)

    def click_date(self):
        """点击日期"""
        self.is_click(project['起止时间'])

    def choose_begin_date(self,date):
        """选择开始日期"""
        self.input_text(project['开始日期'],date)

    def choose_end_date(self,date):
        """选择结束日期"""
        self.input_text(project['结束日期'],date)

    def click_confirm_plan(self):
        """确定创建计划"""
        self.is_click(project['确定计划'])

    def click_project_view(self):
        """点击项目概览"""
        self.is_click(project['项目概览'])

    def check_project_view(self):
        """检查项目概览切换后面包屑"""
        return self.element_text(project['项目概览面包屑检查'])

    def click_gantt_chart(self):
        """点击甘特图"""
        self.is_click(project['甘特图'])

    def check_gantt_chart(self):
        """检查甘特图页面面包屑"""
        return self.element_text(project['甘特图面包屑检查'])

    def click_card_manage(self):
        """点击卡片管理"""
        self.is_click(project['卡片管理'])

    def check_card_manage(self):
        """检查卡片管理面包屑"""
        return self.element_text(project['卡片管理面包屑检查'])

    def click_diy_report(self):
        """点击自定义报表"""
        self.is_click(project['自定义报表'])

    def check_diy_report(self):
        """检查自定义报表面包屑"""
        return self.element_text(project['自定义报表面包屑检查'])

    def click_recycle(self):
        """点击回收站"""
        self.is_click(project['回收站'])

    def check_recycle(self):
        """检查回收站面包屑"""
        return self.element_text(project['回收站面包屑检查'])

    def check_settings(self):
        """检查设置面包屑"""
        return self.element_text(project['设置面包屑检查'])

    def check_plan(self):
        """检查产品规划面包屑"""
        return self.element_text(project['产品规划面包屑检查'])

    def check_plan_and_board(self):
        """检查计划与看板面包屑切换"""
        return self.element_text(project['计划与看板面包屑检查'])

    def click_delete_card(self):
        """点击删除卡片"""
        self.is_click(project['删除卡片'])

    def confirm_delete_card(self):
        """确定删除卡片"""
        self.is_click(project['确定删除卡片'])

    def check_delete_card(self):
        """检查删除卡片成功alert"""
        return self.is_exists(project['删除成功'])
