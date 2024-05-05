# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  web-ui-helper
# FileName:     test.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/28
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from web_ui_helper.terminal.device import Phone
from web_ui_helper.selenium.ui.frame import ListFrame
from web_ui_helper.selenium.frame.browser import SeleniumProxy


def test_adb():
    # ph = Phone(device_id="192.168.3.244", port=5555, enable_debug=False, enabled_log=False, loglevel="error")
    # ph = Phone(device_id="S2D0219126003408", enable_debug=True, enabled_log=True, loglevel="error")
    ph = Phone(device_id="66J5T19312004724", enable_debug=True, enabled_log=True, loglevel="error")
    print(ph.shell("ls"))
    # print(ph.start_app("abc"))
    # print(ph.stop_app("abc"))
    # print(ph.wake())
    # print(ph.home())
    # ph.hide_keyword()


def test_selenium_get_list():
    sel = SeleniumProxy(browser_name="Chrome", is_headless=True, proxy_address="")
    url = "https://flights.ctrip.com/online/list/oneway-foc-can?_=1&depdate=2024-05-15&sortByPrice=true"
    results = ListFrame.get_all_elements(
        driver=sel.browser, url=url, locator="xpath", list_key="index", regx="//div[@index]", timeout=3
    )
    for index, element in results.items():
        print(index)
        print(SeleniumProxy.get_outer_html(sel.browser, element=element))


if __name__ == '__main__':
    # test_adb()
    test_selenium_get_list()
