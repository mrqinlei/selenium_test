#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import os

import pytest
import allure
import selenium
from py.xml import html
from selenium import webdriver

from config.conf import cm
from common.readconfig import ini
from utils.times import timestamp
from utils.send_mail import send_report
from selenium.webdriver.chrome.options import Options
from utils.logger import log

driver = None
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置窗口界面大小
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--headless')

        # driver = webdriver.Remote("http://localhost:4444/wd/hub",
        #                           webdriver.DesiredCapabilities.CHROME.copy(),)
        driver = webdriver.Remote(desired_capabilities=DesiredCapabilities().CHROME,
                                  command_executor='http://localhost:4444', options=chrome_options)

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        log.info('nodeid：%s' % report.nodeid)
        log.info('运行结果: %s' % report.outcome)


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def pytest_html_report_title(report):
    report.title = "pytest示例项目测试报告"


def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = "简单云测试"
    config._metadata['测试地址'] = ini.url


def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear() # 清空summary中的内容
    prefix.extend([html.p("所属部门: XX公司测试部")])
    prefix.extend([html.p("测试执行人: xx")])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        'total times': timestamp() - terminalreporter._sessionstarttime
    }
    print(result)
    if result['failed'] or result['error']:
        # send_report()
        pass


def _capture_screenshot():
    """截图保存为base64"""
    # now_time, screen_file = cm.screen_path
    # driver.save_screenshot(screen_file)
    # allure.attach.file(screen_file,
    #                    "失败截图{}".format(now_time),
    #                    allure.attachment_type.PNG)
    # with open(screen_file, 'rb') as f:
    #     imagebase64 = base64.b64encode(f.read())
    # return imagebase64.decode()


def pytest_collection_modifyitems(session, items):
    # 期望用例顺序
    appoint_items = ["test_login", "test_project","test_wiki","test_coderepository","test_testmanage"]

    # 指定运行顺序
    run_items = []
    for i in appoint_items:
        for item in items:
            module_item = item.name.split("[")[0]
            if i == module_item:
                run_items.append(item)

    for i in run_items:
        run_index = run_items.index(i)
        items_index = items.index(i)

        if run_index != items_index:
            n_data = items[run_index]
            run_index = items.index(n_data)
            items[items_index], items[run_index] = items[run_index], items[items_index]
