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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from web_ui_helper.decorators.selenium_exception import element_find_exception


class ListFrame(object):

    @classmethod
    @element_find_exception
    def __get_current_indexes(cls, driver: webdriver, timeout: int, root_locator: str, root_regx: str,
                              index_locator: str, index_regx: str) -> int:
        """
        获取当前页面上已加载的索引数量
        """
        root_element = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((root_locator, root_regx))
        )
        current_indexes = root_element.find_elements(index_locator, index_regx)
        return len(current_indexes)

    @classmethod
    @element_find_exception
    def __scroll_to_bottom(cls, driver):
        """
        模拟页面滚动到底部
        """
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @classmethod
    @element_find_exception
    def parse_page(cls, driver: webdriver, url: str, root_locator: str, root_regx: str, index_locator: str,
                   index_regx: str, timeout: int = 1, max_index_count: int = 20) -> None:
        """
        爬取页面的主函数
        """
        # 打开网页
        driver.get(url)
        # 获取初始的索引数量
        current_index_count = cls.__get_current_indexes(
            driver=driver, timeout=timeout, root_locator=root_locator,
            root_regx=root_regx, index_locator=index_locator, index_regx=index_regx
        )
        while True:
            # 模拟滚动到页面底部
            cls.__scroll_to_bottom(driver=driver)
            # 等待新索引加载
            WebDriverWait(driver, timeout).until(
                lambda d: cls.__get_current_indexes(
                    driver=driver, timeout=timeout, root_locator=root_locator, root_regx=root_regx,
                    index_locator=index_locator, index_regx=index_regx
                ) > current_index_count
            )
            # 更新当前索引数量
            current_index_count = cls.__get_current_indexes(
                driver=driver, timeout=timeout, root_locator=root_locator,
                root_regx=root_regx, index_locator=index_locator, index_regx=index_regx
            )
            print(f"当前索引数量：{current_index_count}")

            # 如果想要限制爬取的最大索引数量，可以添加判断条件并在此跳出循环
            if current_index_count >= max_index_count:
                break
