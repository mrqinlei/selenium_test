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
    def test_secondary_page(self, drivers):
        """测试二级页面"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        snapshot_crumbs = package.check_snapshot_crumbs()
        package.click_release()
        release_crumbs = package.check_release_crumbs()
        package.click_mirror()
        mirror_crumbs = package.check_mirror_crumbs()
        assert snapshot_crumbs == '半成品库' and release_crumbs == '成品库' and mirror_crumbs == '镜像库'

    @pytest.mark.package
    @pytest.mark.main
    def test_create_new_snapshot(self, drivers):
        """新建半成品库"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_create_new_snapshot()
        # package.click_new_repo_type()
        # package.choose_repo_type()
        package.input_repo_name("ui" + str(randint(1, 999)))
        package.confirm_create_package()

    @pytest.mark.package
    @pytest.mark.main
    def test_create_apk_package(self, drivers):
        """新建apk包"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_apk()
        package.click_create_package()
        package.input_package_name("ui" + str(randint(1, 999)))
        package.confirm_create_package()

    @pytest.mark.package
    @pytest.mark.main
    def test_star_package(self, drivers):
        """收藏包"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_star_button()
        package.click_my_star()
        star_package = package.check_star_snapshot()
        package.click_cancel_star()
        package.click_all()
        assert star_package == 'apk'

    @pytest.mark.package
    @pytest.mark.main
    def test_package_tab(self, drivers):
        """测试包页面tab"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_package_list()
        list_title_name = package.get_package_list_title_name()
        package.click_use_guide()
        get_use_guide_title = package.get_use_guide_title()
        package.click_relate_project()
        package.click_project()
        package.click_choose_project()
        package.choose_first_project()
        sleep(1)
        package.delete_relation()
        package.confirm_delete_relation()
        assert list_title_name == '包名' and get_use_guide_title == '通过网页上传与下载'

    @pytest.mark.package
    @pytest.mark.main
    def test_delete_package(self, drivers):
        """删除包"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_package_list()
        package.delete_package()
        package.confirm_delete()

    @pytest.mark.package
    @pytest.mark.main
    def test_check_all_type_package(self, drivers):
        """检查所有类型制品库"""
        package = PackagePage(drivers)
        package.click_package()
        package.click_snapshot()
        package.click_apk()
        apk_title = package.check_apk_title()
        package.click_composer()
        composer_title = package.check_composer_title()
        package.click_conan()
        conan_title = package.check_conan_title()
        package.click_docker()
        docker_title = package.check_docker_title()
        package.click_helm()
        helm_title = package.check_helm_title()
        package.click_ipa()
        ipa_title = package.check_ipa_title()
        package.click_maven()
        maven_title = package.check_maven_title()
        package.click_npm()
        npm_title = package.check_npm_title()
        package.click_nuget()
        nuget_title = package.check_nuget_title()
        package.click_pypi()
        pypi_title = package.check_pypi_title()
        package.click_file()
        file_title = package.check_file_title()
        assert apk_title == 'apk' and composer_title == 'composer' and conan_title == 'conan' and \
               docker_title == 'docker' and helm_title == 'helm' and ipa_title == 'ipa' and maven_title \
               == 'maven' and npm_title == 'npm' and nuget_title == 'nuget' and pypi_title == 'pypi' and \
               file_title == 'file'


if __name__ == '__main__':
    pytest.mark['TestCase/test_package.py']
