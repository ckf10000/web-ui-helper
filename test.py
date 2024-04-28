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


def test_adb():
    # ph = Phone(device_id="192.168.3.244", port=5555, enable_debug=True, enabled_log=True, loglevel="error")
    ph = Phone(device_id="S2D0219126003408", enable_debug=True, enabled_log=True, loglevel="error")
    print(ph.shell("ls"))
    # print(ph.start_app("abc"))
    # print(ph.stop_app("abc"))
    # print(ph.wake())
    # print(ph.home())
    # ph.hide_keyword()


if __name__ == '__main__':
    test_adb()
