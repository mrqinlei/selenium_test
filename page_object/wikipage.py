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

