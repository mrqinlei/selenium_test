#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 5:17 下午
# @File    : test_coderepository.py
from random import randint

import pytest
import allure

from page_object.loginpage import LoginPage
from page_object.projectpage import project
from utils.logger import log
from common.readconfig import ini
from page_object.coderepository import CodeRepositoryPage
from common.readconfig import ReadConfig
from utils.times import sleep


@allure.feature("测试code模块")
class TestCodeRepository:

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
    @pytest.mark.repo
    @allure.feature("新建代码库用例")
    def test_create_repo_space(self, drivers):
        """新建代码库测试"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_coderepository()
        coderepository.click_create_coderepository()
        dirname, name = 'ui_test' + str(randint(100, 999)), 'ut' + str(randint(100, 999))
        coderepository.add_coderepository_content(dirname, name)
        coderepository.click_confirm()
        assert coderepository.check_coderepository_name() == name

    @pytest.mark.main
    @pytest.mark.repo
    def test_create_new_file(self, drivers):
        """新建文件"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_new_profile()
        file_name = "ui自动化" + str(randint(100, 999)) + '.py'
        coderepository.input_file_name(file_name)
        # coderepository.input_file_content("Hello World")   #monaco编辑器定位不到
        coderepository.click_save()
        coderepository.click_confirm_save()
        res = coderepository.check_file_name()
        assert res == file_name

    @pytest.mark.main
    @pytest.mark.repo
    def test_history(self, drivers):
        """历史页面push，commit，graph"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_history()
        coderepository.click_pushes()
        pushes = coderepository.check_pushes_crumbs()
        coderepository.click_commits()
        commits = coderepository.check_commits_crumbs()
        coderepository.click_graph()
        graph = coderepository.check_graph_crumbs()
        assert pushes == 'Pushes' and commits == '提交' and graph == '网格'

    def test_secondary_page_check(self):
        #TODO
        """二级页面检查"""
        pass

    @pytest.mark.main
    @pytest.mark.repo
    def test_create_branch(self, drivers):
        """创建新分支"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_branch()
        coderepository.click_create_branch()
        branch_name = "branch" + str(randint(100, 999))
        coderepository.input_branch_name(branch_name)
        coderepository.click_confirm_branch()
        branch_name_check = coderepository.check_new_branch_name()
        assert branch_name_check == branch_name

    @pytest.mark.main
    @pytest.mark.repo
    def test_create_version(self, drivers):
        """创建新版本"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_version()
        coderepository.click_create_new_version()
        new_version_name = str(randint(1, 9)) + '.' + str(randint(1, 9)) + '.' + str(randint(1, 9))
        coderepository.input_version_name(new_version_name)
        coderepository.click_confirm_create_new_version()
        assert coderepository.check_new_create_version_name() == new_version_name

    @pytest.mark.main
    @pytest.mark.repo
    def test_code_view(self, drivers):
        """新建代码评审"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_file()
        coderepository.click_branch_filter()
        coderepository.choose_first_branch()
        coderepository.click_create_new_file()
        new_file = "ui自动化" + str(randint(1, 999)) + '.py'
        coderepository.input_file_name(new_file)
        coderepository.click_save()
        coderepository.click_confirm_save()
        coderepository.click_review()
        coderepository.click_create_view()
        coderepository.click_confirm_create_view()
        viewing_status = coderepository.get_view_status()
        coderepository.click_view_pass()
        coderepository.click_publish_comment()
        coderepository.click_merge()
        coderepository.click_delete_origin_branch()
        coderepository.confirm_merge()
        view_end_status = coderepository.get_view_status()
        assert viewing_status == '评审中' and view_end_status == '已入库'

    @pytest.mark.main
    @pytest.mark.repo
    def test_delete_repo(self,drivers):
        """删除代码库"""
        coderepository = CodeRepositoryPage(drivers)
        coderepository.click_settings()
        coderepository.click_ops_operation()
        coderepository.click_delete_repo()
        repo_name = coderepository.get_repo_name()
        coderepository.input_repo_name(repo_name)
        coderepository.confirm_delete_repo()




if __name__ == '__main__':
    pytest.main(['TestCase/test_coderepository.py'])
