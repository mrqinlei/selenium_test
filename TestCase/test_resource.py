#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 4:18 下午
# @File    : test_resource.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage

from common.readconfig import ini
from page_object.resource import ResourcePage
from utils.times import sleep


@allure.feature("计算资源模块")
class TestResource:

    @pytest.fixture(scope='class', autouse=True)
    def __is_login(self, drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()

    @pytest.mark.resource
    @pytest.mark.main
    def test_create_host_cluster(self, drivers):
        """新建主机组"""
        resource = ResourcePage(drivers)
        resource.click_resource()
        resource.click_host_cluster()
        resource.click_new_host_cluster()
        resource.input_host_cluster_name("ui自动化")
        resource.confirm_create_host_cluster()
        resource_name = resource.check_host_cluster_name()
        assert resource_name == 'ui自动化'

    @pytest.mark.resource
    @pytest.mark.main
    def test_view_host_cluster(self, drivers):
        """查看新建主机组"""
        resource = ResourcePage(drivers)
        resource.click_view_host_cluster()
        resource.edit_host_cluster()
        # resource.click_admin()
        # resource.choose_user()
        resource.input_tips("我是备注")
        resource.confirm_edit()
        tip = resource.get_tips()
        assert tip == '我是备注'

    @pytest.mark.skip(reason='需要切换iframe')
    @pytest.mark.resource
    @pytest.mark.main
    def test_add_host_cluster_node(self, drivers):
        """接入主机集群节点"""
        resource = ResourcePage(drivers)
        resource.click_host_cluster_admin()
        resource.click_view_cluster_node()
        resource.click_add_node()
        # resource.click_linux()
        # linux_command = resource.get_command()
        # resource.click_macos()
        # macos_command = resource.get_command()
        # resource.click_windows()
        # windows_command = resource.get_command()
        resource.close_node_window()
        resource.close_view_node()
        # assert linux_command == '## 适合64位x86芯片普通linux操作系统' and \
        #        macos_command == '## 适合64位x86芯片macOS系统' and windows_command == '## 适合64位x86芯片windows操作系统'


    @pytest.mark.skip
    @pytest.mark.resource
    @pytest.mark.main
    def test_delete_node(self,drivers):
        """删除节点"""
        resource = ResourcePage(drivers)
        resource.click_host_cluster_admin()
        resource.click_view_cluster_node()
        resource.delete_node()
        resource.click_confirm_delete_node()

    @pytest.mark.resource
    @pytest.mark.main
    def test_star_cluster(self,drivers):
        """收藏主机集群"""
        resource = ResourcePage(drivers)
        resource.click_resource()
        resource.click_host_cluster_all()
        resource.click_star_button()
        host_name = resource.check_host_cluster_name()
        resource.click_my_star()
        star_host_name = resource.check_host_cluster_name()
        resource.click_star_button()
        assert host_name == star_host_name

    @pytest.mark.resource
    @pytest.mark.main
    def test_delete_host_cluster(self,drivers):
        """删除主机节点"""
        resource = ResourcePage(drivers)
        resource.click_host_cluster_admin()
        resource.delete_host_cluster()
        resource.click_confirm_delete_node()

    @pytest.mark.resource
    @pytest.mark.main
    def test_create_k8s_cluster(self,drivers):
        """新建k8s集群"""
        resource = ResourcePage(drivers)
        resource.click_k8s_cluster()
        resource.create_new_k8s_cluster()
        resource.input_k8s_cluster_name("ui自动化k8s集群")
        resource.confirm_create_k8s_cluster()
        k8s_cluster_name = resource.get_k8s_cluster_name()
        assert k8s_cluster_name == 'ui自动化k8s集群'

    @pytest.mark.resource
    @pytest.mark.main
    def test_view_k8s_cluster(self,drivers):
        """查看k8s主机组"""
        resource = ResourcePage(drivers)
        resource.click_k8s_cluster()
        resource.view_k8s_cluster()
        resource.edit_k8s_cluster()
        # resource.click_admin()
        # resource.choose_user()
        resource.input_tips("我是k8s备注")
        resource.confirm_edit()
        tip = resource.get_tips()
        assert tip == '我是k8s备注'

    @pytest.mark.resource
    @pytest.mark.main
    def test_star_k8s_cluster(self,drivers):
        """收藏k8s集群"""
        resource = ResourcePage(drivers)
        resource.click_k8s_cluster()
        resource.click_host_cluster_all()
        k8s_name = resource.get_k8s_cluster_name()
        resource.click_star_button()
        resource.click_my_star()
        k8s_star = resource.get_k8s_cluster_name()
        resource.click_star_button()
        assert k8s_star == k8s_name



    @pytest.mark.resource
    @pytest.mark.main
    def test_delete_k8s_cluster(self,drivers):
        """删除k8s集群"""
        resource = ResourcePage(drivers)
        resource.click_k8s_cluster()
        resource.click_host_cluster_admin()
        resource.delete_k8s_cluster()
        resource.click_confirm_delete_node()


    @pytest.mark.resource
    @pytest.mark.main
    def test_secondary_page(self,drivers):
        """二级页面面包屑"""
        resource = ResourcePage(drivers)
        resource.click_host_cluster()
        host_crumbs = resource.check_host_cluster_crumbs()
        resource.click_k8s_cluster()
        k8s_crumbs = resource.check_k8s_cluster_crumbs()
        assert host_crumbs == '主机集群' and k8s_crumbs == 'K8S集群'



if __name__ == '__main__':
    pytest.main(['TestCase/test_resource.py'])
