# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  web-ui-helper
# FileName:     frame.py
# Description:  页面数据框架
# Author:       GIGABYTE
# CreateDate:   2024/04/28
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from selenium import webdriver
from web_ui_helper.common.webdriver import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from web_ui_helper.selenium.frame.browser import SeleniumProxy
from web_ui_helper.decorators.selenium_exception import element_find_exception, loop_find_element


class ListFrame(object):

    @classmethod
    @loop_find_element
    def get_current_elements(
            cls, driver: webdriver, locator: str, regx: str, timeout: int = 3, **kwargs
    ) -> list[WebElement]:
        kwargs.clear()
        return WebDriverWait(driver, timeout).until(
            ec.presence_of_all_elements_located((Locator.get(locator), regx))
        )

    @classmethod
    @element_find_exception
    def get_all_elements(
            cls, driver: webdriver, url: str, locator: str, regx: str, list_key: str, timeout: int = 1
    ) -> dict:
        """
        爬取页面的主函数
        """
        # 打开网页
        driver.get(url)
        flag = True
        parsed_data = dict()
        while flag:
            SeleniumProxy.scroll_to_bottom(driver=driver)
            elements = cls.get_current_elements(driver=driver, locator=locator, regx=regx, timeout=timeout, loop=60)
            new_elements = {element.get_attribute(list_key): element for element in elements if
                            element.get_attribute(list_key) not in list(parsed_data.keys())}
            if new_elements:
                parsed_data.update(new_elements)
            else:
                flag = False
        return parsed_data
