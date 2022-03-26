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

    def add_coderepository_content(self, dirname, name, ):
        """填写目录名和代码库名"""
        self.input_text(code['目录名'], dirname)
        self.input_text(code['代码库名'], name)

    def click_confirm(self):
        """点击确认"""
        self.is_click(code['确定'])

    def check_coderepository_name(self):
        """创建成功后检查代码库姓名"""
        return self.element_text(code['代码库名检查'])

    def click_new_profile(self):
        """新建文件"""
        self.is_click(code['新建文件'])

    def input_file_name(self, file_name):
        """输入新文件名"""
        self.input_text(code['新文件名'], file_name)

    def input_file_content(self, file_content):
        """输入文件内容"""
        self.input_text(code['文件内容'], file_content)

    def click_save(self):
        """点击保存按钮"""
        self.is_click(code['保存'])

    def click_confirm_save(self):
        """点击确定保存按钮"""
        self.is_click(code['确定保存'])

    def check_save_success(self):
        """检查保存成功alert"""
        return self.is_exists(code['操作成功'])

    def check_file_name(self):
        """检查新建文件名称"""
        return self.element_text(code['查询文件名称'])

    def click_history(self):
        """点击历史"""
        self.is_click(code['历史'])

    def click_pushes(self):
        """点击pushes"""
        self.is_click(code['历史_pushes_标签'])

    def check_pushes_crumbs(self):
        """检查pushes面包屑"""
        return self.element_text(code['历史_pushes_面包屑'])

    def click_commits(self):
        """点击commits"""
        self.is_click(code['历史_commits_标签'])

    def check_commits_crumbs(self):
        """检查commits面包屑"""
        return self.element_text(code['历史_commits_面包屑'])

    def click_graph(self):
        """点击graph"""
        self.is_click(code['历史_graph_标签'])

    def check_graph_crumbs(self):
        """检查graph面包屑"""
        return self.element_text(code['历史_graph_面包屑'])

    def click_branch(self):
        """点击分支"""
        self.is_click(code['分支'])

    def click_create_branch(self):
        """点击新建分支"""
        self.is_click(code['新建分支'])

    def input_branch_name(self, branch_name):
        """输入新分支名称"""
        self.input_text(code['分支名'], branch_name)

    def click_confirm_branch(self):
        """确认创建分支"""
        self.is_click(code['确定新分支'])

    def check_new_branch_name(self):
        """检查新分支名称"""
        return self.element_text(code['检查新分支名称'])

    def click_version(self):
        """点击版本"""
        self.is_click(code['版本'])

    def click_create_new_version(self):
        """点击新建版本"""
        self.is_click(code['新建版本'])

    def input_version_name(self,version_name):
        """输入版本名称"""
        self.input_text(code['版本名称'],version_name)

    def click_confirm_create_new_version(self):
        """确认创建新版本"""
        self.is_click(code['确定创建新版本'])

    def check_new_create_version_name(self):
        """检查新创建版本名称"""
        return self.element_text(code['新版本名称'])

    def click_branch_filter(self):
        """点击分支筛选器"""
        self.is_click(code['文件分支下拉'])

    def choose_first_branch(self):
        """选择首个分支"""
        self.is_click(code['第一个分支'])

    def click_create_new_file(self):
        """点击新增文件"""
        self.is_click(code['新增文件'])

    def click_review(self):
        """点击评审"""
        self.is_click(code['评审'])

    def click_create_view(self):
        """点击新建评审"""
        self.is_click(code['新建评审'])

    def click_confirm_create_view(self):
        """点击确定新建评审"""
        self.is_click(code['确定新建评审'])

    def check_create_view(self):
        """检查评审详情"""
        return self.element_text(code['评审详情'])

    def click_view_pass(self):
        """点击评审通过"""
        self.is_click(code['评审通过'])

    def click_publish_comment(self):
        """发布评审"""
        self.is_click(code['评审发表'])

    def click_merge(self):
        """点击合入"""
        self.is_click(code['合入'])

    def click_delete_origin_branch(self):
        """选择删除源分支"""
        self.is_click(code['合入后删除源分支'])

    def confirm_merge(self):
        """确认合入"""
        self.is_click(code['确定合入'])

    def get_view_status(self):
        """获得评审状态"""
        return self.element_text(code['评审状态'])

    def click_file(self):
        """点击文件"""
        self.is_click(code['文件'])

    def click_settings(self):
        """点击设置"""
        self.is_click(code['设置'])

    def click_ops_operation(self):
        """点击运维操作"""
        self.is_click(code['运维操作'])

    def click_delete_repo(self):
        """点击删除代码库"""
        self.is_click(code['删除代码库'])

    def get_repo_name(self):
        """获得代码库名称"""
        return self.element_text(code['获得代码库名称'])

    def input_repo_name(self,repo_name):
        """输入代码库名称"""
        self.input_text(code['输入代码库名称'],repo_name)

    def confirm_delete_repo(self):
        """确认删除代码库"""
        self.is_click(code['确认删除'])

    def check_file_crumbs(self):
        """检查文件面包屑"""
        return self.element_text(code['检查文件面包屑'])

    def check_history_crumbs(self):
        """检查历史面包屑"""
        return self.element_text(code['检查历史面包屑'])

    def click_compare(self):
        """点击对比"""
        self.is_click(code['对比'])

    def check_compare_crumbs(self):
        """检查对比面包屑"""
        return self.element_text(code['检查对比面包屑'])

    def check_branch_crumbs(self):
        """检查分支面包屑"""
        return self.element_text(code['检查分支面包屑'])

    def check_version_crumbs(self):
        """检查版本面包屑"""
        return self.element_text(code['检查版本面包屑'])

    def check_review_crumbs(self):
        """检查评审面包屑"""
        return self.element_text(code['检查评审面包屑'])

    def click_scan(self):
        """点击扫描"""
        self.is_click(code['扫描'])

    def check_scan_crumbs(self):
        """检查扫描面包屑"""
        return self.element_text(code['检查扫描面包屑'])

    def click_statistics(self):
        """点击统计"""
        self.is_click(code['统计'])

    def check_statistics_crumbs(self):
        """检查统计面包屑"""
        return self.element_text(code['检查统计面包屑'])

    def check_settings_crumbs(self):
        """检查设置面包屑"""
        return self.element_text(code['检查设置面包屑'])
