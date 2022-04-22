#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 4:58 下午
# @File    : test_project.py
import re
from random import randint

import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.projectpage import ProjectPage
from page_object.loginpage import LoginPage
from common.readconfig import ReadConfig
from utils.times import sleep


@allure.feature("测试项目模块")
class TestProject:

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

    @pytest.mark.main
    @pytest.mark.project
    @allure.feature("新建项目用例")
    def test_create_project(self, drivers):
        """新建项目测试"""
        project = ProjectPage(drivers)
        project.click_project()
        project.add_project()
        name, code = 'ui_test', 'ut'
        project.add_project_content(name, code)
        project.click_project_template()
        project.select_project_template()
        project.confirm_create_project()
        res = project.personal_settings_name()
        log.info(res)
        print(res)
        assert res == name

    @pytest.mark.main
    @pytest.mark.project
    @allure.feature("新建卡片用例")
    def test_create_card(self, drivers):
        """新建卡片用例"""
        project = ProjectPage(drivers)
        project.click_plan_and_board()
        project.click_create_card()
        project.add_card_title(title='ui自动化测试', content='ui自动化测试')
        project.click_confirm_create_card()
        assert project.check_card_create_success() is not None
        # assert res == 'ui自动化测试'

    @pytest.mark.main
    @pytest.mark.project
    def test_change_card_status(self, drivers):
        """改变卡片状态"""
        project = ProjectPage(drivers)
        # project.click_first_project()
        project.click_first_card()
        project.click_card_status()
        project.click_status_doing()
        card_status = project.check_card_status()
        print(card_status)
        sleep(2)
        assert card_status == '进行中'

    @pytest.mark.main
    @pytest.mark.project
    def test_card_block(self, drivers):
        """设置阻塞"""
        project = ProjectPage(drivers)
        # project.click_first_project()
        # project.click_first_card()
        project.click_card_detail_more_function()
        project.click_block_button()
        project.click_block_switch()
        sleep(2)
        project.input_block_content("接口阻塞，导致无法联调")
        project.confirm_block()
        project.click_block_success()
        res = project.check_block()
        project.confirm_block()
        assert res == '接口阻塞，导致无法联调'

    @pytest.mark.main
    @pytest.mark.project
    def test_delete_card(self,drivers):
        """删除卡片"""
        project = ProjectPage(drivers)
        project.click_card_detail_more_function()
        project.click_delete_card()
        project.confirm_delete_card()
        res = project.check_delete_card()
        print(res)



    @pytest.mark.main
    @pytest.mark.project
    @allure.feature("新建规划用例")
    def test_create_plan(self, drivers):
        """新建规划"""
        project = ProjectPage(drivers)
        project.click_project_plan()
        project.click_new_plan()
        project.add_plan_name(planname='uitestplan')
        project.click_confirm_create_plan()
        assert project.check_create_plan_success is not None

    @pytest.mark.skip(reason="选择日期控件定位问题，暂不执行")
    @pytest.mark.main
    @pytest.mark.project
    def test_create_plan(self, drivers):
        """新建计划"""
        project = ProjectPage(drivers)
        # project.click_first_project()
        project.click_plan_and_board()
        project.click_create_plan()
        project.input_plan_name("自动化新建计划")
        project.click_date()
        project.choose_begin_date("2022-03-20")
        project.choose_end_date("2022-03-30")  # 元素查找待确定 当前查找失败
        sleep(5)
        project.click_confirm_plan()
        sleep(5)

    @pytest.mark.main
    @pytest.mark.project
    @allure.feature("项目收藏用例")
    def test_project_star(self, drivers):
        """收藏功能"""
        project = ProjectPage(drivers)
        project.click_project()
        before_star_name = project.get_first_project_name()
        project.click_star_button()
        project.click_my_star()
        after_star_name = project.get_first_project_name()
        print(before_star_name, after_star_name)
        project.click_project()
        project.click_star_button()
        assert before_star_name == after_star_name

    @pytest.mark.skip(reason="项目列表关联icon定位不到")
    @pytest.mark.main
    @pytest.mark.project
    def test_project_relation_wiki(self, drivers):
        """项目管理列表关联wiki功能"""
        project = ProjectPage(drivers)
        project.click_project()
        project.get_relation_wiki()
        project.click_relation_wiki_icon()
        project.click_relation_wiki_button()
        project.click_wiki_space()
        before_relation_wiki_name = project.get_select_wiki_space_name()
        project.click_first_wiki_item()
        after_relation_wiki_name = project.get_relation_wiki_space_name()
        print(before_relation_wiki_name, after_relation_wiki_name)
        sleep(2)
        project.click_close_relate_windows()

    @pytest.mark.main
    @pytest.mark.project
    def test_secondary_page_check(self,drivers):
        """二级页面切换检查面包屑"""
        project = ProjectPage(drivers)
        project.click_first_project()
        project.click_project_view()
        project_view = project.check_project_view()
        project.click_project_plan()
        project_plan = project.check_plan()
        project.click_plan_and_board()
        project_plan_and_board = project.check_plan_and_board()
        project.click_gantt_chart()
        project_gantt_chart = project.check_gantt_chart()
        project.click_card_manage()
        project_card_manage = project.check_card_manage()
        project.click_diy_report()
        project_diy_report = project.check_diy_report()
        project.click_recycle()
        project_recycle = project.check_recycle()
        project.click_settings()
        project_setting = project.check_settings()
        assert project_view == '项目概览' and project_plan == '产品规划' and project_plan_and_board == '计划与看板'\
        and project_gantt_chart == '甘特图' and project_card_manage == '卡片管理' and project_diy_report == '自定义报表'\
        and project_recycle == '回收站'  and project_setting == '基本设置'

    @pytest.mark.main
    @pytest.mark.project
    def test_project_delete(self, drivers):
        """删除项目"""
        project = ProjectPage(drivers)
        project.click_first_project()
        project.click_settings()
        project.click_ops_operation()
        project.click_delete_project()
        project.input_password(ini.password)
        project.click_confirm_delete()




if __name__ == '__main__':
    pytest.main(['TestCase/test_project.py'])

