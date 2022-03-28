#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 2:04 下午
# @File    : package.py
from page.webpage import WebPage, sleep
from common.readelement import Element

package = Element('package')


class PackagePage(WebPage):

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

    def click_create_new_snapshot(self):
        """点击新建半成品库"""
        self.is_click(package['新建库'])

    def click_new_repo_type(self):
        """点击仓库类型"""
        self.is_click([package['新建仓库类型']])

    def choose_repo_type(self):
        """选择仓库类型"""
        self.is_click(package['选择仓库类型'])

    def input_repo_name(self,repo_name):
        """输入仓库名称"""
        self.input_text(package['仓库名称'],repo_name)

    def confirm_create_repo(self):
        """确认创建仓库"""
        self.is_click(package['确定新建仓库'])

    def click_apk(self):
        """点击apk"""
        self.is_click(package['apk'])

    def click_star_button(self):
        """点击收藏按钮"""
        self.is_click(package['收藏按钮'])

    def click_my_star(self):
        """点击我的收藏"""
        self.is_click(package['我的收藏'])

    def check_star_snapshot(self):
        """查看收藏的库"""
        return self.element_text(package['收藏库'])

    def click_cancel_star(self):
        """取消收藏"""
        self.is_click(package['取消收藏'])

    def click_all(self):
        """点击全部"""
        self.is_click(package['全部'])

    def click_create_package(self):
        """点击新建包"""
        self.is_click(package['新建包'])

    def input_package_name(self, package_name):
        """输入包名"""
        self.input_text(package['包名'], package_name)

    def confirm_create_package(self):
        """确定新建包"""
        self.is_click(package['确定创建新包'])

    def click_package_list(self):
        """点击包列表"""
        self.is_click(package['包列表'])

    def get_package_list_title_name(self):
        """获得包名列头"""
        return self.element_text(package['包名列头'])

    def click_use_guide(self):
        """点击使用方法"""
        self.is_click(package['使用方法'])

    def get_use_guide_title(self):
        """获得使用方法的title"""
        return self.element_text(package['使用方法title'])

    def click_relate_project(self):
        """点击关联项目标签"""
        self.is_click(package['关联项目'])

    def click_project(self):
        """点击关联按钮"""
        self.is_click(package['关联项目按钮'])

    def click_choose_project(self):
        """选择项目"""
        self.is_click(package['选择项目'])

    def choose_first_project(self):
        """选择第一个项目"""
        self.is_click(package['选择第一个项目'])

    def create_success(self):
        """创建成功alert"""
        self.is_exists(package['创建成功'])

    def delete_relation(self):
        """删除关联"""
        self.is_click(package['删除关联'])

    def confirm_delete_relation(self):
        """确认删除关联"""
        self.is_click(package['确认删除关联'])

    def delete_package(self):
        """删除包"""
        self.is_click(package['删除包'])

    def confirm_delete(self):
        """确认删除"""
        self.is_click(package['确认删除'])

    def delete_success(self):
        """删除成功"""
        self.is_exists(package['删除成功'])

    def check_snapshot_crumbs(self):
        """检查半成品库面包屑"""
        return self.element_text(package['半成品库面包屑'])

    def check_release_crumbs(self):
        """检查成品库标签"""
        return self.element_text(package['成品库面包屑'])

    def check_mirror_crumbs(self):
        """检查镜像库"""
        return self.element_text(package['镜像库面包屑'])

    def check_apk_title(self):
        """检查apk页面title"""
        return self.element_text(package['apk页面'])

    def click_composer(self):
        """点击composer"""
        self.is_click(package['composer'])

    def check_composer_title(self):
        """检查composer页面内title"""
        return self.element_text(package['composer页面'])

    def click_conan(self):
        """点击conan"""
        self.is_click(package['conan'])

    def check_conan_title(self):
        """检查conan页面title"""
        return self.element_text(package['conan页面'])

    def click_docker(self):
        """点击docker"""
        self.is_click(package['docker'])

    def check_docker_title(self):
        """检查docker页面title"""
        return self.element_text(package['docker页面'])

    def click_helm(self):
        """点击helm"""
        self.is_click(package['helm'])

    def check_helm_title(self):
        """检查helm页面title"""
        return self.element_text(package['helm页面'])

    def click_ipa(self):
        """点击ipa"""
        self.is_click(package['ipa'])

    def check_ipa_title(self):
        """检查ipa页面title"""
        return self.element_text(package['ipa页面'])

    def click_maven(self):
        """点击maven"""
        self.is_click(package['maven'])

    def check_maven_title(self):
        """检查maven页面title"""
        return self.element_text(package['maven页面'])

    def click_npm(self):
        """点击npm"""
        self.is_click(package['npm'])

    def check_npm_title(self):
        """检查npm页面title"""
        return self.element_text(package['npm页面'])

    def click_nuget(self):
        """点击nuget"""
        self.is_click(package['nuget'])

    def check_nuget_title(self):
        return self.element_text(package['nuget页面'])

    def click_pypi(self):
        """点击pypi"""
        self.is_click(package['pypi'])

    def check_pypi_title(self):
        """检查pypi页面title"""
        return self.element_text(package['pypi页面'])

    def click_file(self):
        """点击file"""
        self.is_click(package['file'])

    def check_file_title(self):
        """检查file页面title"""
        return self.element_text(package['file页面'])
