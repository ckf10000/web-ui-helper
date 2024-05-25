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
import time
from pandas import DataFrame, set_option
from web_ui_helper.terminal.device import Phone
from web_ui_helper.selenium.ui.frame import ListFrame
from web_ui_helper.selenium.frame.browser import SeleniumProxy
from web_ui_helper.selenium.parse.ctrip_flight import DesktopFlight, AirlineListUiLocator as Air

"""
display.max_rows:     设置要显示的最大行数
display.max_columns:  设置要显示的最大列数
display.width:        设置显示的宽度，以字符数为单位
display.precision:    设置浮点数的精度
display.max_colwidth: 设置要显示的列的最大宽度，以字符数为单位
"""

# 设置要显示的最大行数和列数
set_option('display.width', 65535)
set_option('display.max_rows', 5000)
set_option('display.max_columns', 1024)
set_option('display.max_colwidth', 1000)
# 设置打印格式，使列头和行内容对齐
set_option('display.unicode.east_asian_width', True)


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
    sel = SeleniumProxy(browser_name="Chrome", is_headless=True, proxy_address="", is_single_instance=False)
    url = "https://flights.ctrip.com/online/list/oneway-SZX-TSN?_=1&depdate=2024-05-31&sortByPrice=true"
    elements_data = ListFrame.get_all_elements_with_scroll_tile(
        driver=sel.browser, url=url, locator="xpath", list_key="index", regx="//div[@index]", timeout=3,
        start_element_locator="xpath", start_element_regx='//*[@class="sortbar-v2"]'
    )
    df = DesktopFlight.parse_airlines(elements_data=elements_data)
    # 打印DataFrame
    print(df.to_string(justify='left', index=False))
    # print(df.to_html(escape=False, index=False, justify="left"))


def test_selenium_get_expand_list():
    sel = SeleniumProxy(
        browser_name="Chrome", is_headless=False, is_enable_proxy=False, is_single_instance=False, proxy_scheme="https"
    )
    url = "https://flights.ctrip.com/online/list/oneway-SZX-TSN?_=1&depdate=2024-05-31&sortByPrice=true"
    parse_data = ListFrame.get_all_elements_with_scroll_expand(
        driver=sel.browser, url=url, index_locator=Air.var_index.value.get("locator"), list_key="index",
        index_regx=Air.var_index.value.get("regx"), indexes_locator=Air.all_index.value.get("locator"),
        indexes_regx=Air.all_index.value.get("regx"), timeout=1, start_element_regx=Air.list_hearder.value.get("regx"),
        start_element_locator=Air.list_hearder.value.get("locator"), list_parse_func=DesktopFlight.parse_airline,
        expand_locator=Air.booking_expand.value.get("locator"), expand_regx=Air.booking_expand.value.get("regx"),
        more_all_locator=Air.more_product.value.get("locator"), more_all_regx=Air.more_product.value.get("regx"),
        area_parse_func=DesktopFlight.parse_expand_area
    )
    if parse_data.get("rows_data"):
        df = DataFrame.from_records(data=parse_data.get("rows_data"))
        df.to_excel('SZX-TSN航线.xlsx', index=False)
        # 打印DataFrame
        # print(df.to_string(justify='left', index=False))
    if parse_data.get("expand_data"):
        df = DataFrame.from_records(data=parse_data.get("expand_data"))
        df.to_excel('SZX-TSN航线的所有产品.xlsx', index=False)
        # 打印DataFrame
        # print(df.to_string(justify='left', index=False))


def test_selenium_get_cookie():
    sel = SeleniumProxy(browser_name="Chrome", is_headless=True, proxy_address="")
    url = " https://www.ctrip.com"
    sel.get(url=url)
    time.sleep(5)
    from pprint import pprint
    pprint(sel.get_cookies())
    pprint(sel.get_session())
    pprint(sel.get_cookie(name="cticket"))


if __name__ == '__main__':
    # test_adb()
    # test_selenium_get_list()
    # test_selenium_get_cookie()
    test_selenium_get_expand_list()
