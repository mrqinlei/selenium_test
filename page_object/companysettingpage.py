#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 2:45 下午
# @File    : companysettingpage.py
from page.webpage import WebPage
from common.readelement import Element

companysetting = Element('companysetting')

class CompanySetting(WebPage):
    """企业设置方法类"""

    def click_company_setting(self):
        """点击企业设置"""
        self.is_click(companysetting['企业设置'])

    def click_company_info(self):
        """点击企业信息"""
        self.is_click(companysetting['企业信息'])

    def click_edit_company_base_info(self):
        """点击企业基本信息"""
        self.is_click(companysetting['编辑基本信息'])

    def click_company_name(self):
        """"""
        self.double_click(companysetting['输入企业名称'])

    def input_company_name(self,company_name):
        """输入企业名称"""
        self.send(companysetting['输入企业名称'],company_name)

    def click_save(self):
        """点击保存"""
        self.is_click(companysetting['保存'])

    def click_scan_save(self):
        """点击代码扫描保存"""
        self.is_click(companysetting['代码扫描保存'])



    def click_edit_ticket_info(self):
        """编辑开票信息"""
        self.is_click(companysetting['编辑开票信息'])

    def input_company_full_name(self,company_full_name):
        """输入开票信息"""
        self.input_text(companysetting['输入企业完整名称'],company_full_name)

    def input_ITIN(self,itin):
        """输入纳税人识别号"""
        self.input_text(companysetting['输入纳税人识别号'],itin)

    def click_edit_bill_info(self):
        """编辑增值税专用发票信息"""
        self.is_click(companysetting['增值税专用发票信息'])

    def input_bank_name(self,bank_name):
        """输入开户行"""
        self.input_text(companysetting['开户行'],bank_name)

    def input_ban_account(self,bank_account):
        """输入银行账号"""
        self.input_text(companysetting['银行账号'],bank_account)

    def input_company_address(self,company_address):
        """输入公司地址"""
        self.input_text(companysetting['公司地址'],company_address)

    def input_company_contact_information(self,contact_info):
        """输入公司联系方式"""
        self.input_text(companysetting['公司联系方式'],contact_info)

    def click_user_interface(self):
        """点击界面设置"""
        self.is_click(companysetting['界面设置'])

    def click_watermark_switch_off(self):
        """点击水印关"""
        self.is_click(companysetting['界面水印关闭'])

    def click_watermark_switch_on(self):
        """点击水印开"""
        self.is_click(companysetting['界面水印开启'])

    def click_project_setting(self):
        """点击项目设置"""
        self.is_click(companysetting['项目设置'])

    def click_create_project_template(self):
        """点击新建项目模板"""
        self.is_click(companysetting['新建项目设置'])

    def input_name(self,template_name='ui自动化创建'):
        """输入名称"""
        self.input_text(companysetting['输入名称'],template_name)

    def click_other_template(self):
        """点击其他模板"""
        self.is_click(companysetting['点击选择模板'])

    def choose_template(self):
        """选择通用模板"""
        self.is_click(companysetting['通用项目'])

    def confirm_create_template(self):
        """确认创建模板"""
        self.is_click(companysetting['确定创建模板'])

    def get_template_name(self):
        """获得模板名称"""
        return self.element_text(companysetting['获得模板名称'])

    def delete_template(self):
        """删除模板"""
        self.is_click(companysetting['删除模板'])

    def confirm_delete(self):
        """确认删除"""
        self.is_click(companysetting['确定删除'])

    def click_wiki_setting(self):
        """点击wiki设置"""
        self.is_click(companysetting['wiki设置'])

    def edit_wiki_version_keep(self):
        """点击编辑wiki版本数量保留"""
        self.is_click(companysetting['编辑wiki设置'])

    def input_wiki_version_keep(self,wiki_version_num):
        """输入wiki版本保留数量"""
        self.input_text(companysetting['输入版本数量'],wiki_version_num)

    def click_push_rule(self):
        """点击提交规范"""
        self.is_click(companysetting['提交规范'])

    def input_push_file_size_limit(self,file_size_limit):
        """输入文件大小"""
        self.input_text(companysetting['提交文件限制大小'],file_size_limit)

    def click_code_scan(self):
        """点击代码扫描"""
        self.is_click(companysetting['代码扫描'])

    def input_review_scan_keep(self,review_scan_keep_days):
        """输入评审扫描记录保留时间"""
        self.input_text(companysetting['扫描评审记录保留'],review_scan_keep_days)

    def input_whole_scan_keep(self,whole_scan_keep_days):
        """输入全量扫描记录保留时间"""
        self.input_text(companysetting['全量扫描记录保留'],whole_scan_keep_days)

    def input_external_scan_keep(self,external_scan_keep_days):
        """输入外部代码扫描记录保留时间"""
        self.input_text(companysetting['外部代码扫描记录保留'],external_scan_keep_days)

    def click_flow_setting(self):
        """点击流水线设置"""
        self.is_click(companysetting['流水线设置'])

    def click_edit_flow_report_keep_days(self):
        """点击编辑流水线报告保留时间"""
        self.is_click(companysetting['编辑流水线设置'])

    def input_flow_report_keep_days(self,flow_keep_days):
        """输入流水线报告保留时间"""
        self.input_text(companysetting['流水线制品保留时长'],flow_keep_days)

    def click_test_setting(self):
        """点击测试设置"""
        self.is_click(companysetting['测试设置'])

    def input_test_execute_keep_days(self,test_execute_day):
        """输入测试执行保留时间"""
        self.input_text(companysetting['测试执行保留'],test_execute_day)

    def input_test_performance_data_keep_days(self,test_performance_keep_days):
        """输入性能测试数据保留时间"""
        self.input_text(companysetting['性能测试明细数据'],test_performance_keep_days)

    def click_resource_use(self):
        """点击资源用量"""
        self.is_click(companysetting['资源用量'])

    def get_resource_title(self):
        """获得资源用量页面标题"""
        return self.element_text(companysetting['资源用量标题'])

    def click_bill(self):
        """点击账单"""
        self.is_click(companysetting['账单'])

    def click_bill_detail(self):
        """点击账单明细"""
        self.is_click(companysetting['账单明细'])

    def click_pay_record(self):
        """点击充值记录"""
        self.is_click(companysetting['充值记录'])

    def click_member_and_role(self):
        """点击成员与角色"""
        self.is_click(companysetting['成员与角色'])

    def click_member_manage(self):
        """点击成员管理"""
        self.is_click(companysetting['成员管理标签'])


    def click_member_invite_or_add(self):
        """点击成员添加或邀请"""
        self.is_click(companysetting['成员添加或邀请'])

    def click_create_invite_link(self):
        """点击创建邀请链接"""
        self.is_click(companysetting['创建邀请链接'])

    def get_invite_link(self):
        """获取邀请链接"""
        return self.element_text(companysetting['获取邀请链接'])

    def click_fast_add(self):
        """点击快速添加"""
        self.is_click(companysetting['快速添加'])

    def input_email(self,email):
        """输入email"""
        self.input_text(companysetting['输入邮箱'],email)

    def input_login_username(self,user_name):
        """输入登录用户名"""
        self.input_text(companysetting['输入登录用户名'],user_name)

    def add_member(self):
        """点击添加成员"""
        self.is_click(companysetting['添加成员'])

    def get_account_status(self):
        """获得账号状态"""
        return self.element_text(companysetting['获取账号状态'])

    def click_register_and_invite(self):
        """点击注册与邀请"""
        self.is_click(companysetting['注册与邀请标签'])

    def click_role_manage(self):
        """点击角色管理"""
        self.is_click(companysetting['角色管理标签'])

    def click_email_invite(self):
        """点击邮件邀请"""
        self.is_click(companysetting['邮件邀请'])

    def input_member_email(self,member_email):
        """输入成员邮箱"""
        self.input_text(companysetting['输入成员邮箱'],member_email)

    def click_send_email(self):
        """点击发送邮件"""
        self.is_click(companysetting['发送邮件'])

    def get_member_name(self):
        """获取成员名字"""
        return self.element_text(companysetting['获取成员名字'])

    def delete_member(self):
        """删除成员"""
        self.is_click(companysetting['删除成员'])

    def click_invite_right(self):
        """设置邀请权限"""
        self.is_click(companysetting['邀请权限'])

    def click_invite_range(self):
        """设置被邀请人范围"""
        self.is_click(companysetting['被邀请人范围'])

    def confirm_register_and_invite_change(self):
        """确认注册与邀请修改"""
        self.is_click(companysetting['注册与邀请确认'])



