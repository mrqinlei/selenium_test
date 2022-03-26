#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 2:06 下午
# @File    : scan.py.py
from page.webpage import WebPage, sleep
from common.readelement import Element

scan = Element('scan')


class ScanPage(WebPage):
    """扫描页面类"""

    def click_scan(self):
        """点击代码扫描"""
        self.is_click(scan['代码扫描'])

    def click_scan_rules(self):
        """点击扫描规则"""
        self.is_click(scan['扫描规则'])

    def click_rule_gather(self):
        """点击规则集"""
        self.is_click(scan['规则集'])

    def click_language_filter(self):
        """点击语言筛选"""
        self.is_click(scan['筛选语言'])

    def choose_python(self):
        """选择python语言"""
        self.is_click(scan['python'])

    def click_level_filter(self):
        """点击级别过滤"""
        self.is_click(scan['级别筛选'])

    def choose_block_level(self):
        """选择阻塞级别"""
        self.is_click(scan['阻塞级别'])

    def click_type_filter(self):
        """类型选择"""
        self.is_click(scan['类型筛选'])

    def choose_bug_type(self):
        """选择缺陷类型"""
        self.is_click(scan['缺陷'])

    def check_language(self):
        """检查选择后语言类型"""
        return self.element_text(scan['检查语言'])

    def check_level(self):
        """检查选择后级别"""
        return self.element_text(scan['检查问题级别'])

    def check_type(self):
        """检查类型"""
        return self.element_text(scan['检查类型'])

    def click_first_rule(self):
        """点击首行规则"""
        self.is_click(scan['首行规则编号item'])

    def click_first_line_number(self):
        """点击首行编号"""
        self.is_click(scan['首行编号'])

    def check_rule_detail(self):
        """检查编号跳转后面包屑"""
        return self.element_text(scan['规则详情'])

    def close_rule_window(self):
        """关闭规则右浮窗"""
        self.is_click(scan['规则浮窗关闭'])

    def check_window_title(self):
        """检查右浮窗标题"""
        return self.element_text(scan['规则检查详情'])

    def click_window_number(self):
        """点击右浮窗规则编号"""
        self.is_click(scan['浮窗编号'])

    def click_edit(self):
        """点击编辑"""
        self.is_click(scan['编辑'])

    def edit_rule_level(self):
        """编辑规则等级"""
        self.is_click(scan['编辑规则级别'])

    def set_block_level(self):
        """设置规则等级为block"""
        self.is_click(scan['设置阻塞级别'])

    def edit_type(self):
        """编辑分类"""
        self.is_click(scan['编辑分类'])

    def set_bug_type(self):
        """设置编辑分类为缺陷"""
        self.is_click(scan['设置缺陷分类'])

    def confirm_edit(self):
        """确认确定编辑"""
        self.is_click(scan['确定编辑'])

    def click_create_rule(self):
        """点击新建规则集"""
        self.is_click(scan['新建规则集'])

    def click_direct_create(self):
        """点击直接新建"""
        self.is_click(scan['直接新建'])

    def input_rule_gather_name(self,rule_gather_name):
        """输入规则集名称"""
        self.input_text(scan['新建规则集名称'],rule_gather_name)

    def confirm_create_rule_gather(self):
        """确定新建规则集"""
        self.is_click(scan['确定新建'])

    def check_default_rule_gather(self):
        """查看默认规则集"""
        self.is_click(scan['查看默认规则集'])

    def check_window_rule_gather_name(self):
        """检查右浮窗规则集title"""
        return self.element_text(scan['右浮窗规则集title'])

    def close_default_rule_window(self):
        """关闭右浮窗口"""
        self.is_click(scan['关闭规则集右浮窗'])

    def check_scan_rule_crumbs(self):
        """检查扫描规则面包屑"""
        return self.element_text(scan['扫描规则面包屑'])

    def check_rule_gather_crumbs(self):
        """检查规则集面包屑"""
        return self.element_text(scan['规则集面包屑'])

