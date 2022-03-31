#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 2:37 下午
# @File    : servicepage.py
from page.webpage import WebPage
from common.readelement import Element

service = Element('service')


class ServicePage(WebPage):
    """集成服务类"""

    def click_service(self):
        """点击集成服务"""
        self.is_click(service['服务集成'])

    def click_docker_mirror(self):
        """点击docker镜像源"""
        self.is_click(service['docker镜像源'])

    def click_sonarqube(self):
        """点击sonarqube"""
        self.is_click(service['sonarqube'])

    def click_webhook(self):
        """点击webhook"""
        self.is_click(service['webhook'])

    def click_jira(self):
        """点击jira"""
        self.is_click(service['jira集成'])

    def click_jenkins(self):
        """点击jira"""
        self.is_click(service['jenkins'])

    def click_scan(self):
        """点击代码扫描"""
        self.is_click(service['代码扫描'])

    def click_add(self):
        """点击添加"""
        self.is_click(service['添加'])

    def input_name(self, service_name):
        """输入服务名称"""
        self.input_text(service['输入名称'], service_name)

    def input_service_address(self, service_address):
        """输入服务地址"""
        self.input_text(service['服务地址'], service_address)

    def get_webhook_name(self):
        """获得webhook服务名称"""
        return self.element_text(service['webhook_name'])

    def input_docker_user_name(self, user_name):
        """输入用户名"""
        self.input_text(service['docker用户名'], user_name)

    def input_docker_user_passwd(self, passwd):
        """输入密码"""
        self.input_text(service['docker密码'], passwd)

    def click_no_verify(self):
        """点击无认证"""
        self.is_click(service['无认证'])

    def delete_success(self):
        """删除成功"""
        return self.element_text(service['删除成功'])

    def delete_jenkins_success(self):
        return self.element_text(service['删除jenkins成功'])

    def click_confirm(self):
        """点击确定"""
        self.is_click(service['确定'])

    def get_service_name(self):
        """获取服务名称"""
        return self.element_text(service['获取服务名称'])

    def click_all(self):
        """点击all"""
        self.is_click(service['全部标签'])

    def click_admin(self):
        """点击我是管理员"""
        self.is_click(service['我是管理员标签'])

    def click_view_service(self):
        """点击查看服务"""
        self.is_click(service['查看服务'])

    def click_edit(self):
        """点击编辑"""
        self.is_click(service['编辑'])

    def get_service_edit_success(self):
        """获取编辑程功状态"""
        return self.element_text(service['成功状态'])

    def click_star_button(self):
        """点击收藏按钮"""
        self.is_click(service['收藏服务'])

    def click_my_star(self):
        """点击我的收藏"""
        self.is_click(service['我的收藏标签'])

    def delete_service(self):
        """点击删除服务"""
        self.is_click(service['删除服务'])

    def confirm_delete(self):
        """点击确认删除"""
        self.is_click(service['确认删除'])

    def webhook_cancel_delete(self):
        """webhook取消删除"""
        self.is_click_slow(service['取消删除'])

    def input_token(self, token):
        """输入token"""
        self.input_text(service['token'], token)

    def input_url(self, url):
        """输入url"""
        self.input_text(service['输入url'], url)

    def click_webhook_save(self):
        """点击webhook保存"""
        self.is_click(service['webhook保存'])

    def click_edit_webhook(self):
        """点击编辑webhook"""
        self.is_click(service['编辑webhook'])

    def close_webhook_window(self):
        """点击关闭webhook窗口"""
        self.is_click(service['关闭webhook浮窗'])

    def view_webhook(self):
        """查看webhook"""
        self.is_click(service['webhook查看'])

    def delete_webhook(self):
        """删除webhook"""
        self.is_click(service['删除webhook'])

    def webhook_view_history(self):
        """webhook查看历史"""
        self.is_click(service['webhook查看历史'])

    def get_webhook_history_window_title(self):
        """获取webhook历史窗口标题"""
        return self.element_text(service['webhook查看历史浮窗标题'])

    def close_webhook_history_window(self):
        """关闭webhook历史浮窗"""
        self.is_click(service['关闭浮窗'])

    def input_jira_username(self, jira_name):
        """输入jira用户名"""
        self.input_text(service['jira用户名'], jira_name)

    def input_jira_password(self, jira_password):
        """输入jira密码"""
        self.input_text(service['jira密码'], jira_password)

    def input_jenkins_tip(self, tip):
        """输入jenkins备注"""
        self.input_text(service['jenkins备注'], tip)

    def get_jenkins_tip(self):
        """获得jenkins备注"""
        return self.element_text(service['获得备注'])

    def click_jenkins_view(self):
        """jenkins查看"""
        self.is_click(service['jenkinsh查看'])

    def star_jenkins_service(self):
        """收藏jenkins服务"""
        self.is_click(service['jenkins收藏'])

    def delete_jenkins_service(self):
        """删除jenkins服务"""
        self.is_click(service['jenkins删除'])

    def get_crumbs(self):
        """获取面包屑"""
        return self.element_text(service['面包屑'])




