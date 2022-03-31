#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 3:07 下午
# @File    : test_service.py
import pytest
import allure
from page_object.loginpage import LoginPage
from common.readconfig import ini
from page_object.servicepage import ServicePage


@allure.feature("集成服务模块")
class TestServiceIntegration:

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
    @pytest.mark.service
    def test_create_docker_mirror(self, drivers):
        """添加docker镜像源"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_docker_mirror()
        service.click_add()
        service.input_name('ui自动化创建')
        service.input_service_address('ezone.work')
        service.input_docker_user_name('user')
        service.input_docker_user_passwd('password')
        service.click_confirm()
        service_name = service.get_service_name()
        assert service_name == 'ui自动化创建'

    @pytest.mark.main
    @pytest.mark.service
    def test_view_docker__service(self, drivers):
        """查看docker服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_docker_mirror()
        service.click_admin()
        service.click_view_service()
        service.click_edit()
        service.click_confirm()
        service_status = service.get_service_edit_success()
        assert service_status == '服务编辑成功'

    @pytest.mark.main
    @pytest.mark.service
    def test_star_docker_service(self, drivers):
        """收藏docker服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_docker_mirror()
        service.click_all()
        service.click_star_button()
        service_name = service.get_service_name()
        service.click_my_star()
        service_star_name = service.get_service_name()
        service.click_star_button()
        assert service_name == service_star_name

    @pytest.mark.main
    @pytest.mark.service
    def test_delete_docker_service(self, drivers):
        """删除docker服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_docker_mirror()
        service.click_admin()
        service.delete_service()
        service.confirm_delete()
        delete_status = service.delete_success()
        assert 'ui自动化创建删除成功' in delete_status

    @pytest.mark.main
    @pytest.mark.service
    def test_create_sonarqube_service(self, drivers):
        """创建sonarqube服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_sonarqube()
        service.click_add()
        service.input_name("ui自动化创建")
        service.input_service_address("127.0.0.1:80")
        service.input_token("1")
        service.click_confirm()
        sonarqube_name = service.get_service_name()
        assert sonarqube_name == 'ui自动化创建'

    @pytest.mark.main
    @pytest.mark.service
    def test_view_sonarqube(self, drivers):
        """查看sonarqube"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_sonarqube()
        service.click_admin()
        service.click_view_service()
        service.click_edit()
        service.click_confirm()
        sonarqube_edit_success = service.get_service_edit_success()
        assert sonarqube_edit_success == '服务编辑成功'

    @pytest.mark.main
    @pytest.mark.service
    def test_star_sonarqube_service(self, drivers):
        """收藏sonarqube服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_sonarqube()
        service.click_all()
        service.click_star_button()
        service_name = service.get_service_name()
        service.click_my_star()
        star_service_name = service.get_service_name()
        service.click_all()
        service.click_star_button()
        assert service_name == star_service_name

    @pytest.mark.main
    @pytest.mark.service
    def test_delete_sonarqube_service(self, drivers):
        """删除sonarqube服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_sonarqube()
        service.click_admin()
        service.delete_service()
        service.confirm_delete()
        delete_status = service.delete_success()
        assert 'ui自动化创建删除成功' in delete_status

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.service
    def test_create_webhook_service(self, drivers):
        """创建webhook服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_webhook()
        service.click_add()
        service.input_name("ui自动化创建")
        service.input_url('http://ezone.ezone-test.work/')
        service.input_token('123')
        service.click_webhook_save()
        service.close_webhook_window()
        service_name = service.get_webhook_name()
        assert service_name == 'ui自动化创建'

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.service
    def test_view_webhook_service(self, drivers):
        """view webhook服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_webhook()
        service.view_webhook()
        service.click_edit_webhook()
        service.input_name("编辑")
        service.click_webhook_save()
        service.close_webhook_window()
        service_name = service.get_webhook_name()
        assert service_name == 'ui自动化创建编辑'

    @pytest.mark.skip
    @pytest.mark.main
    @pytest.mark.service
    def test_delete_webhook_service(self, drivers):
        """删除webhook服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_webhook()
        service.click_admin()
        service.delete_webhook()
        service.webhook_cancel_delete()
        # delete_webhook_success = service.webhook_cancel_delete()
        # assert delete_webhook_success == 'ui自动化创建编辑删除成功'

    @pytest.mark.main
    @pytest.mark.service
    def test_jira_create_service(self,drivers):
        """新建jira服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jira()
        service.click_add()
        service.input_name('ui自动化创建')
        service.input_service_address('http://ezone.ezone-test.work/')
        service.input_jira_username('123')
        service.input_jira_password('123')
        service.click_confirm()
        jira_service_create_success = service.get_service_name()
        assert jira_service_create_success == 'ui自动化创建'


    @pytest.mark.main
    @pytest.mark.service
    def test_view_jira(self, drivers):
        """查看jira"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jira()
        service.click_admin()
        service.click_view_service()
        service.click_edit()
        service.click_confirm()
        jira_edit_success = service.get_service_edit_success()
        assert jira_edit_success == '服务编辑成功'

    @pytest.mark.main
    @pytest.mark.service
    def test_star_jira_service(self, drivers):
        """收藏jira服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jira()
        service.click_all()
        service.click_star_button()
        service_name = service.get_service_name()
        service.click_my_star()
        star_service_name = service.get_service_name()
        service.click_all()
        service.click_star_button()
        assert service_name == star_service_name


    @pytest.mark.main
    @pytest.mark.service
    def test_delete_jira_service(self, drivers):
        """删除jira服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jira()
        service.click_admin()
        service.delete_service()
        service.confirm_delete()
        delete_status = service.delete_success()
        assert 'ui自动化创建删除成功' in delete_status


    @pytest.mark.main
    @pytest.mark.service
    def test_jenkins_create_service(self,drivers):
        """新建jenkins服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jenkins()
        service.click_add()
        service.input_name('uiautomationcreate')
        service.click_confirm()
        jenkins_service_name = service.get_service_name()
        assert jenkins_service_name == 'uiautomationcreate'

    @pytest.mark.main
    @pytest.mark.service
    def test_view_jenkins(self, drivers):
        """查看jenkins"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jenkins()
        service.click_jenkins_view()
        service.click_edit()
        service.input_jenkins_tip('我是UI自动化备注')
        service.click_confirm()
        jenkins_tip = service.get_jenkins_tip()
        assert jenkins_tip == '我是UI自动化备注'


    @pytest.mark.main
    @pytest.mark.service
    def test_star_jenkins_service(self, drivers):
        """收藏jenkins服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jenkins()
        service.click_all()
        service.star_jenkins_service()
        service_name = service.get_service_name()
        service.click_my_star()
        star_service_name = service.get_service_name()
        service.click_all()
        service.star_jenkins_service()
        assert service_name == star_service_name


    @pytest.mark.main
    @pytest.mark.service
    def test_delete_jenkins_service(self, drivers):
        """删除jenkins服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_jenkins()
        service.click_admin()
        service.delete_jenkins_service()
        service.confirm_delete()
        delete_status = service.delete_jenkins_success()
        assert '删除成功' in delete_status


    @pytest.mark.main
    @pytest.mark.service
    def test_scan_create_service(self,drivers):
        """新建扫描服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_scan()
        service.click_add()
        service.input_name('ui自动化创建')
        service.input_service_address('http://ezone.ezone-test.work/')
        service.input_token('123')
        service.click_confirm()
        scan_service_name = service.get_service_name()
        assert scan_service_name == 'ui自动化创建'

    @pytest.mark.main
    @pytest.mark.service
    def test_view_scan(self, drivers):
        """查看scan"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_scan()
        service.click_admin()
        service.click_view_service()
        service.click_edit()
        service.click_confirm()
        scan_edit_success = service.get_service_edit_success()
        assert scan_edit_success == '服务编辑成功'

    @pytest.mark.main
    @pytest.mark.service
    def test_star_scan_service(self, drivers):
        """收藏scan服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_scan()
        service.click_all()
        service.click_star_button()
        service_name = service.get_service_name()
        service.click_my_star()
        star_service_name = service.get_service_name()
        service.click_all()
        service.click_star_button()
        assert service_name == star_service_name

    @pytest.mark.main
    @pytest.mark.service
    def test_delete_scan_service(self, drivers):
        """删除scan服务"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_scan()
        service.click_admin()
        service.delete_service()
        service.confirm_delete()
        delete_status = service.delete_success()
        assert 'ui自动化创建删除成功' in delete_status

    @pytest.mark.main
    @pytest.mark.service
    def test_secondary_crumbs(self,drivers):
        """二级页面面包屑"""
        service = ServicePage(drivers)
        service.click_service()
        service.click_docker_mirror()
        docker_crumbs = service.get_crumbs()
        service.click_sonarqube()
        sonarqube_crumbs = service.get_crumbs()
        service.click_webhook()
        webhook_crumbs = service.get_crumbs()
        service.click_jira()
        jira_crumbs = service.get_crumbs()
        service.click_jenkins()
        jenkins_crumbs = service.get_crumbs()
        service.click_scan()
        scan_crumbs = service.get_crumbs()
        assert docker_crumbs == 'Docker镜像源' and sonarqube_crumbs == 'SonarQube' and webhook_crumbs == 'Webhook' and \
               jira_crumbs == 'Jira集成' and jenkins_crumbs == 'Jenkins' and scan_crumbs == '代码扫描'


if __name__ == '__main__':
    pytest.main['TestCase/test_service']
