#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 3:23 下午
# @File    : resource.py
from page.webpage import WebPage, sleep
from common.readelement import Element

resource = Element('resource')


class ResourcePage(WebPage):
    """计算资源类"""

    def click_resource(self):
        """点击计算资源"""
        self.is_click(resource['计算资源'])

    def click_host_cluster(self):
        """点击主机集群"""
        self.is_click(resource['主机集群'])

    def click_k8s_cluster(self):
        """点击k8s集群"""
        self.is_click(resource['k8s集群'])

    def click_host_cluster_all(self):
        """点击主机集群全部"""
        self.is_click(resource['全部'])

    def click_host_cluster_admin(self):
        """点击主机集群我是管理员"""
        self.is_click(resource['我是管理员'])

    def click_host_cluster_star(self):
        """点击主机集群我的收藏"""
        self.is_click(resource['我的收藏'])

    def click_new_host_cluster(self):
        """点击新建主机集群"""
        self.is_click(resource['新建'])

    def input_host_cluster_name(self, host_cluster_name):
        """输入主机组名称"""
        self.input_text(resource['输入主机名称'], host_cluster_name)

    def confirm_create_host_cluster(self):
        """确认创建主机组"""
        self.is_click(resource['确定创建主机'])

    def check_host_cluster_name(self):
        """检查创建成功主机名称"""
        return self.element_text(resource['主机组名称'])

    def click_view_host_cluster(self):
        """查看主机"""
        self.is_click(resource['查看'])

    def edit_host_cluster(self):
        """编辑主机组"""
        self.is_click(resource['编辑主机组'])

    def click_admin(self):
        """点击管理员"""
        self.is_click(resource['输入用户名'])

    def choose_user(self):
        """选择用户"""
        self.is_click(resource['选择第一个用户'])

    def input_tips(self, tips):
        """输入备注"""
        self.input_text(resource['输入备注'], tips)

    def input_k8s_tip(self,k8s_tips):
        """输入k8s备注"""
        self.input_text(resource['k8s_备注'],k8s_tips)
    def confirm_edit(self):
        """确认编辑"""
        self.is_click(resource['确定编辑'])

    def get_tips(self):
        """查看备注"""
        return self.element_text(resource['查看备注'])

    def click_star_button(self):
        """点击收藏按钮"""
        self.is_click(resource['收藏'])

    def click_my_star(self):
        """点击我的收藏"""
        self.is_click(resource['我的收藏'])

    def check_star_host_cluster_name(self):
        """获得收的收藏主机名称"""
        return self.element_text(resource['获取收藏主机名称'])

    def click_view_cluster_node(self):
        """点击查看主机组节点"""
        self.is_click(resource['查看集群节点'])

    def click_add_node(self):
        """点击新增节点"""
        self.is_click(resource['接入节点'])

    def check_node_window_title(self):
        """检查节点窗口标题"""
        return self.element_text(resource['接入节点浮窗标题'])

    def click_linux(self):
        """点击节点linux接入"""
        self.is_click(resource['linux'])

    def get_command(self):
        """获得命令注释内容"""
        return self.element_text(resource['命令'])

    def click_macos(self):
        """点击节点接入macos"""
        self.is_click(resource['macos'])

    def click_windows(self):
        """点击windows"""
        self.is_click(resource['windows'])

    def close_node_window(self):
        """关闭节点窗口"""
        self.is_click(resource['关闭节点浮窗'])

    def delete_node(self):
        """删除节点"""
        self.is_click(resource['删除节点'])

    def click_confirm_delete_node(self):
        """确认删除节点"""
        self.is_click(resource['确认删除节点'])

    def close_view_node(self):
        """关闭查看节点窗口"""
        self.is_click(resource['关闭'])

    def check_host_cluster_crumbs(self):
        """检查主机集群面包屑"""
        return self.element_text(resource['主机集群面包屑'])

    def check_k8s_cluster_crumbs(self):
        """检查k8s面包屑"""
        return self.element_text(resource['K8S集群面包屑'])

    def create_new_k8s_cluster(self):
        """新建k8s集群"""
        self.is_click(resource['新建k8s集群'])

    def input_k8s_cluster_name(self, k8s_name):
        """输入k8s集群名称"""
        self.input_text(resource['输入k8s集群名称'], k8s_name)

    def confirm_create_k8s_cluster(self):
        """确定新建k8s集群"""
        self.is_click(resource['确定创建k8s集群'])

    def get_k8s_cluster_name(self):
        """获得k8s集群名称"""
        return self.element_text(resource['查看k8s集群标题'])

    def delete_k8s_cluster(self):
        """删除k8s集群按钮"""
        self.is_click(resource['删除k8s集群'])

    def view_k8s_cluster(self):
        """查看k8s集群"""
        self.is_click(resource['k8s查看'])

    def edit_k8s_cluster(self):
        """编辑k8s"""
        self.is_click(resource['编辑k8s集群'])

    def delete_host_cluster(self):
        """删除主机组"""
        self.is_click(resource['删除主机集群'])

