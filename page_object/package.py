#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 2:04 下午
# @File    : package.py
from page.webpage import WebPage, sleep
from common.readelement import Element

package = Element('package')


class PackagePage(WebPage):
    """制品库类"""

    def click_package(self):
        """点击制品库"""
        self.is_click(package['制品库'])

    def click_snapshot(self):
        """点击半成品库"""
        self.is_click(package['半成品库'])

    def click_release(self):
        """点击成品库"""
        self.is_click(package['成品库'])

    def click_mirror(self):
        """点击镜像库"""
        self.is_click(package['镜像库'])

    def get_crumbs(self):
        """获的面包屑名称"""
        return self.element_text(package['制品库面包屑'])

    def click_star_package(self):
        """点击收藏"""
        self.is_click(package['收藏按钮'])

    def get_package_name(self):
        """获取制品库名称"""
        return self.element_text(package['获取制品库名称'])

    def click_my_favourite_tab(self):
        """点击我的收藏"""
        self.is_click(package['我的收藏'])

    def click_create_new_package(self):
        """点击创建新半成品库"""
        self.is_click(package['新建半成品库'])

    def input_package_name(self, package_name):
        """输入package name"""
        self.input_text(package['输入仓库名称'], package_name)

    def input_package_describe(self, describe_content):
        """输入仓库描述"""
        self.input_text(package['输入仓库描述'], describe_content)

    def click_confirm(self):
        """点击确定"""
        self.is_click(package['确定'])

    def get_new_package_name(self):
        """获取新创建制品库名称"""
        return self.element_text(package['仓库名称'])

    def click_new_create_package(self):
        """点击新创建的制品库"""
        self.is_click(package['点击新创建的半成品'])

    def click_relation_project_tab(self):
        """点击关联项目tab"""
        self.is_click(package['关联项目tab'])

    def click_relation_project(self):
        """点击关联项目按钮"""
        self.is_click(package['关联项目'])

    def click_choose_project(self):
        """点击请选择项目"""
        self.is_click(package['点击选择项目'])

    def get_project_name(self):
        """获取项目名称"""
        return self.element_text(package['选择项目'])

    def choose_project(self):
        """选择项目"""
        self.is_click(package['选择项目'])

    def get_relation_project_name(self):
        """获取关联后项目名称"""
        return self.element_text(package['获取关联项目名称'])

    def click_cancel_relation(self):
        """取消关联"""
        self.is_click(package['取消关联'])

    def click_delete_package_tab(self):
        """点击删除制品库tab"""
        self.is_click(package['删除制品库tab'])

    def click_delete_package_button(self):
        """点击删除制品库按钮"""
        self.is_click(package['删除制品库按钮'])

    def input_delete_package_name(self, delete_package_name):
        """输入被删除制品库名称"""
        self.input_text(package['输入制品库名称删除'], delete_package_name)

    def confirm_delete_package(self):
        """确认删除制品库"""
        self.is_click(package['确认删除'])

    def click_package_list(self):
        """点击包列表tab"""
        self.is_click(package['包列表'])

    def click_create_new_snapshot_package(self):
        """制品库呢已新建包"""
        self.is_click(package['新建包'])

    def input_snapshot_package_name(self,snapshot_package_name):
        """输入包名"""
        self.input_text(package['输入包名'],snapshot_package_name)

    def get_snapshot_package_name(self):
        """获取新创建的包名"""
        return self.element_text(package['获取包名'])

    def click_delete_snapshot_package(self):
        """点击删除包按钮"""
        self.is_click(package['删除包按钮'])

    def click_confirm_delete_snapshot_package(self):
        """确认删除包"""
        self.is_click(package['确认删除包'])
