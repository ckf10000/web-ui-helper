# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  web-ui-helper
# FileName:     ctrip_flight.py
# Description:  解析携程航班
# Author:       mfkifhss2023
# CreateDate:   2024/05/05
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from pandas import DataFrame
from selenium import webdriver


class DesktopFlight:

    @classmethod
    def parse_data(cls, driver: webdriver, data: dict) -> DataFrame:
        pass
