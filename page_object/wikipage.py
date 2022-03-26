#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:09 上午
# @File    : wikipage.py
from selenium.webdriver import Keys

from page.webpage import WebPage, sleep
from common.readelement import Element

wiki = Element('wiki')


class WikiPage(WebPage):
    """wiki类"""

    def click_wiki(self):
        """点击左侧wiki按钮"""
        self.is_click(wiki['wiki'])

    def click_create_wiki_space(self):
        """新建wiki空间"""
        self.is_click(wiki['新建'])

    def add_wiki_content(self, name, code):
        """填写wiki空间信息"""
        self.input_text(wiki['空间名称'], name)
        self.input_text(wiki['英文标识'], code)

    def click_confirm(self):
        """点击确定"""
        self.is_click(wiki['确定'])

    def check_wiki_name(self):
        """"""
        return self.element_text(wiki['wikiname'])

    def all_button_exists(self):
        """通过全部按钮判断创建wiki空间是否成功"""
        return self.is_exists(wiki['全部'])

    def click_first_wiki_space(self):
        """"点击第一个wiki space"""
        self.is_click(wiki['第一个页面'])

    def click_page_list(self):
        """点击页面列表"""
        self.is_click(wiki['页面列表'])

    def click_new_page(self):
        """点击新建页面"""
        self.is_click(wiki['新建页面'])

    def add_page_title(self, title):
        """输入标题"""
        self.input_text(wiki['输入标题'], title)

    def add_page_content(self, content):
        """输入内容"""
        self.input_text(wiki['输入内容'], content)

    def add_to_page_content(self, content):
        """追加输入"""
        self.input_text_withoutclear(wiki['输入内容'], content)

    def input_font_bold(self):
        """输入加粗文字"""
        self.is_click(wiki['加粗'])

    def input_font_itali(self):
        """输入斜体文字"""
        self.is_click(wiki['斜体'])

    def input_del_font(self):
        """输入删除线文字"""
        self.is_click(wiki['删除线'])

    def input_highlight_font(self):
        """输入高亮字体"""
        self.is_click(wiki['高亮'])

    def input_incode(self):
        """输入行内代码"""
        self.is_click(wiki['行内代码'])

    def click_input_link(self):
        """点击链接icon"""
        self.is_click(wiki['链接'])

    def input_link(self, link):
        """输入链接"""
        self.input_text(wiki['输入链接'], link)

    def click_enter(self):
        """点击回车"""
        self.press_enter()

    def click_publish_button(self):
        """点击发布按钮"""
        self.is_click(wiki['发布'])

    def check_title(self):
        """"检查发布后的title"""
        return self.element_text(wiki['检查title'])

    def click_star_button(self):
        """点击收藏页面按钮"""
        self.is_click(wiki['收藏按钮'])

    def get_star_button_text(self):
        """获取收藏按钮文案判断已收藏未收藏"""
        return self.element_text(wiki['收藏按钮'])

    def click_focus_button(self):
        """点击关注按钮"""
        self.is_click(wiki['关注按钮'])

    def get_focus_button_text(self):
        """获取关注按钮文案判断已关注或未关注"""
        return self.element_text(wiki['关注按钮'])

    def click_to_star_page(self):
        """点击跳转收藏页面"""
        self.is_click(wiki['我的收藏'])

    def get_star_title(self):
        """获取收藏标题"""
        return self.element_text(wiki['收藏名称'])

    def click_more_function(self):
        """点击wiki页面更多功能"""
        self.is_click(wiki['更多功能'])

    def click_create_son_page(self):
        """点击创建子页面"""
        self.is_click(wiki['创建子页面'])

    def click_son_page_publish(self):
        """发布子卡片"""
        self.is_click(wiki['子卡片发布'])

    def click_delete_page(self):
        """点击删除页面"""
        self.is_click(wiki['删除页面'])

    def confirm_delete(self):
        """点击确认删除页面"""
        self.is_click(wiki['删除确定'])

    def check_delete_success(self):
        """检查删除成功"""
        return self.is_exists(wiki['删除成功'])

    def click_move_to_new_space(self):
        """点击移到新空间"""
        self.is_click(wiki['移动到新空间'])

    def click_move_new_space_select(self):
        """点击选择空间框"""
        self.is_click(wiki['新空间选择框'])

    def choose_new_space(self):
        """选择新空间"""
        self.is_click(wiki['新空间'])

    def new_space_confirm(self):
        """点击确定移动到新空间"""
        self.is_click(wiki['新空间确定'])

    def check_page_list(self):
        """检查页面列表面包屑"""
        return self.element_text(wiki['页面列表面包屑'])

    def click_recent_visit(self):
        """点击最近访问"""
        self.is_click(wiki['最近访问'])

    def check_recent_visit(self):
        """检查最近访问面包屑"""
        return self.element_text(wiki['最近访问面包屑'])

    def check_my_star(self):
        """检查我的收藏面包屑"""
        return self.element_text(wiki['我的收藏面包屑'])

    def click_my_draft(self):
        """点击我的草稿"""
        self.is_click(wiki['我的草稿'])

    def check_my_draft(self):
        """检查我的草稿面包屑"""
        return self.element_text(wiki['我的草稿面包屑'])

    def click_recycle(self):
        """点击我的回收站"""
        self.is_click(wiki['回收站'])

    def check_recycle(self):
        """检查回收站面包屑"""
        return self.element_text(wiki['回收站面包屑'])

    def click_settings(self):
        """点击设置"""
        self.is_click(wiki['设置'])

    def check_settings(self):
        """检查设置面包屑"""
        return self.element_text(wiki['设置面包屑'])

    def click_ops_operation(self):
        """点击运维操作"""
        self.is_click(wiki['运维操作'])

    def click_delete_space(self):
        """点击删除空间"""
        self.is_click(wiki['删除空间'])

    def confirm_delete_space(self):
        """点击确认删除空间"""
        self.is_click(wiki['确认删除'])

    def click_list_first_page(self):
        """点击列表首个页面"""
        self.is_click(wiki['列表首个页面'])
