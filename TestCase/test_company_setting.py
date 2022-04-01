#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 7:16 下午
# @File    : test_company_setting.py
import pytest
import allure
from page_object.loginpage import LoginPage
from common.readconfig import ini
from page_object.companysettingpage import CompanySetting


@allure.feature("企业设置模块")
class TestCompanySetting:

    @pytest.fixture(scope='class', autouse=True)
    def _is_login(self, drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login = LoginPage(drivers)
        login.click_login()
        login.input_acount(ini.account)
        login.input_passwd(ini.password)
        login.submit_login()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_company_info(self,drivers):
        """编辑企业信息"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_company_info()
        companysetting.click_edit_company_base_info()
        companysetting.click_company_name()
        companysetting.input_company_name("ui自动化")
        companysetting.click_save()
        companysetting.click_edit_ticket_info()
        companysetting.input_company_full_name('ui自动化大公司')
        companysetting.input_ITIN('11223344')
        companysetting.click_save()
        companysetting.click_edit_bill_info()
        companysetting.input_bank_name('招商银行')
        companysetting.input_ban_account('621483011234')
        companysetting.input_company_address("北京昌平区")
        companysetting.input_company_contact_information("621221212")
        companysetting.click_save()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_user_interface(self,drivers):
        """界面设置"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_user_interface()
        companysetting.click_watermark_switch_off()
        companysetting.click_watermark_switch_on()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_profile_setting(self,drivers):
        """项目设置"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_project_setting()
        companysetting.click_create_project_template()
        companysetting.input_name('ui自动化创建')
        companysetting.click_other_template()
        companysetting.choose_template()
        companysetting.confirm_create_template()
        template_name = companysetting.get_template_name()
        companysetting.delete_template()
        companysetting.confirm_delete()
        assert template_name == 'ui自动化创建'

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_wiki_setting(self,drivers):
        """wiki设置"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_wiki_setting()
        companysetting.edit_wiki_version_keep()
        companysetting.input_wiki_version_keep("1")
        companysetting.click_save()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_push_rule(self,drivers):
        """提交规范"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_push_rule()
        companysetting.input_push_file_size_limit('1024')
        companysetting.confirm_create_template()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_scan_record(self,drivers):
        """扫描记录"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_code_scan()
        companysetting.input_review_scan_keep("1")
        companysetting.input_whole_scan_keep("1")
        companysetting.input_external_scan_keep("1")
        companysetting.click_scan_save()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_flow_record(self,drivers):
        """流水线记录"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_flow_setting()
        companysetting.click_edit_flow_report_keep_days()
        companysetting.input_flow_report_keep_days("1")
        companysetting.click_save()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_manage_test(self,drivers):
        """测试设置"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_test_setting()
        companysetting.input_test_execute_keep_days('1')
        companysetting.input_test_performance_data_keep_days('1')
        companysetting.click_scan_save()

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_resource(self,drivers):
        """资源用量"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_resource_use()
        resource_title = companysetting.get_resource_title()
        assert resource_title == '资源用量'

    @pytest.mark.main
    @pytest.mark.companysetting
    def test_pay_order(self,drivers):
        """账单"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()
        companysetting.click_bill()
        companysetting.click_bill_detail()
        companysetting.click_pay_record()

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.companysetting
    def test_create_member(self,drivers):
        """TODO 邀请成员"""
        companysetting = CompanySetting(drivers)
        companysetting.click_company_setting()






if __name__ == '__main__':
    pytest.main('[TestCase/test_company_setting.py]')
