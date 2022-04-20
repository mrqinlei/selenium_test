#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 3:02 下午
# @File    : test_package.py
from random import randint

import pytest
import allure

from common.readconfig import ini
from page_object.loginpage import LoginPage
from page_object.package import PackagePage
from utils.times import sleep


@allure.feature("测试制品库模块")
class TestPackage:

    @classmethod
    @pytest.fixture(scope='class', autouse=True)
    def _is_login(cls, drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()


    @pytest.mark.package
    @pytest.mark.main
    def test_create_package(self,drivers):
        """新建制品库"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_create_new_package()
        package.input_package_name('uitest_create')
        package.input_package_describe('这是ui自动化创建的')
        package.click_confirm()
        package_name = package.get_new_package_name()
        assert package_name == 'uitest_create'

    @pytest.mark.package
    @pytest.mark.main
    def test_relation_project(self,drivers):
        """关联项目功能"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_new_create_package()
        package.click_relation_project_tab()
        package.click_relation_project()
        package.click_choose_project()
        project_name = package.get_project_name()
        package.choose_project()
        relation_project_name = package.get_relation_project_name()
        package.click_cancel_relation()
        package.click_confirm()
        assert project_name == relation_project_name


    @pytest.mark.package
    @pytest.mark.main
    def test_create_package_packet(self,drivers):
        """snapshot package 新建包"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_new_create_package()
        package.click_package_list()
        package.click_create_new_snapshot_package()
        package.input_snapshot_package_name("apple.com")
        package.click_confirm()
        package_name = package.get_snapshot_package_name()
        package.click_delete_snapshot_package()
        package.click_confirm_delete_snapshot_package()
        assert package_name == 'apple.com'

    @pytest.mark.package
    @pytest.mark.main
    def test_delete_package(self,drivers):
        """删除制品库"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_new_create_package()
        package.click_delete_package_tab()
        package.click_delete_package_button()
        package.input_delete_package_name('uitest_create')
        package.confirm_delete_package()

    @pytest.mark.package
    @pytest.mark.main
    def test_favourite_package(self,drivers):
        """收藏制品库功能"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        before_star_package_name = package.get_package_name()
        package.click_star_package()
        package.click_my_favourite_tab()
        after_star_package_name = package.get_package_name()
        package.click_star_package()
        print(before_star_package_name,after_star_package_name)
        assert before_star_package_name == after_star_package_name

    @pytest.mark.package
    @pytest.mark.main
    def test_crumbs(self,drivers):
        """面包屑"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        snapshot_crumbs = package.get_crumbs()
        package.click_release()
        release_crumbs = package.get_crumbs()
        package.click_mirror()
        mirror_crumbs = package.get_crumbs()
        assert snapshot_crumbs == '半成品库' and release_crumbs == '成品库' and mirror_crumbs == '镜像库'

if __name__ == '__main__':
    pytest.mark['TestCase/test_package.py']
