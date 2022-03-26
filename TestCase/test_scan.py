#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 2:46 下午
# @File    : test_scan.py
from random import randint

import pytest
import allure

from common.readconfig import ini
from page_object.loginpage import LoginPage
from page_object.scan import ScanPage


@allure.feature("测试scan模块")
class TestCodeScan:

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

    @pytest.mark.main
    @pytest.mark.scan
    def test_scan_secondary_page(self, drivers):
        """检查扫描二级页面"""
        scan = ScanPage(drivers)
        scan.click_scan()
        scan.click_scan_rules()
        scan_rule_crumbs = scan.check_scan_rule_crumbs()
        scan.click_rule_gather()
        rule_gather_crumbs = scan.check_rule_gather_crumbs()
        assert scan_rule_crumbs == '扫描规则' and rule_gather_crumbs == '规则集'

    @pytest.mark.main
    @pytest.mark.scan
    def test_scan_rule_page(self, drivers):
        """扫描规则页面过滤设置"""
        scan = ScanPage(drivers)
        scan.click_scan()
        scan.click_language_filter()
        scan.choose_python()
        # scan.click_level_filter()
        # scan.choose_block_level()
        scan.click_type_filter()
        scan.choose_bug_type()
        language = scan.check_language()
        # level = scan.check_level()
        rule_type = scan.check_type()
        assert language == 'Python' and  rule_type == '缺陷'

    @pytest.mark.main
    @pytest.mark.scan
    def test_rule_check_detail(self,drivers):
        """规则检查详情"""
        scan = ScanPage(drivers)
        scan.click_first_rule()
        window_title = scan.check_window_title()
        scan.click_edit()
        scan.edit_rule_level()
        # scan.set_block_level()
        scan.edit_type()
        # scan.set_bug_type()
        scan.confirm_edit()
        # level = scan.check_level()
        rule_type = scan.check_type()
        assert rule_type == '缺陷' and '规则检查详情' in window_title

    @pytest.mark.main
    @pytest.mark.scan
    def test_rule_detail(self,drivers):
        """规则详情"""
        scan = ScanPage(drivers)
        scan.click_first_line_number()
        rule_detail_crumbs = scan.check_rule_detail()
        assert rule_detail_crumbs == '规则详情'

    @pytest.mark.main
    @pytest.mark.scan
    def test_rule_gather(self,drivers):
        """新建规则集"""
        scan = ScanPage(drivers)
        scan.click_rule_gather()
        scan.click_create_rule()
        scan.click_direct_create()
        scan.input_rule_gather_name("ui自动化"+str(randint(1, 999)))
        scan.confirm_create_rule_gather()
        scan.check_default_rule_gather()
        default_rule_gather = scan.check_window_rule_gather_name()
        scan.close_default_rule_window()
        assert default_rule_gather == '查看规则集'




if __name__ == '__main__':
    pytest.main(['TestCase/test_scan.py'])
