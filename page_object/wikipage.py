#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:09 上午
# @File    : wikipage.py

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