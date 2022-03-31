#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.conf import cm
from utils.times import sleep
from utils.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.support.select import Select


log = Logger(__name__).logger


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def focus(self):
        """聚焦元素"""
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def input_text_withoutclear(self, locator, txt):
        """输入（输入前不清空）"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.send_keys(txt)
        log.info("输入文本:{}".format(txt))

    def press_enter(self):
        self.send_keys(Keys.ENTER)

    def is_click(self, locator):
        """点击"""
        ele = self.find_element(locator)
        ele.click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def is_click_slow(self, locator):
        """点击"""
        ele = self.find_element(locator)
        sleep(3)
        ele.click()
        log.info("点击元素：{}".format(locator))

    def is_exists(self, locator):
        """元素是否存在(DOM)"""
        try:
            WebPage.element_locator(lambda *args: EC.presence_of_element_located(args)(self.driver), locator)
            return True
        except NoSuchElementException:
            return False

    def alert_exists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        if alert:
            text = alert.text
            log.info("Alert弹窗提示为：%s" % text)
            alert.accept()
            return text
        else:
            log.error("没有Alert弹窗提示!")

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def get_attribute(self, locator, name):
        """获取元素属性"""
        return self.find_element(locator).get_attribute(name)

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)


    def move_and_stay(self, locator):
        """悬停"""
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


    def move_to_location(self):
        self.driver.execute_script('window.scrollBy(1000,1050)')
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def scroll(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)



if __name__ == "__main__":
    pass
