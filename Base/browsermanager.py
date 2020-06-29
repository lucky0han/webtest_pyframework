# -*- coding:utf-8 -*-
import configparser
import os
import settings
from selenium import webdriver

from expection import NoOpenBrowser


class BrowserManager(object):
    __CONFIG_FILE_PATH__ = os.path.join(settings.PROJECT_DIR, "pytest.ini")
    __BROWSER_LIST__ = []

    def create_browser(self):
        # print(self.__CONFIG_FILE_PATH__)
        conf = configparser.ConfigParser()
        if os.path.exists(self.__CONFIG_FILE_PATH__):
            conf.read(self.__CONFIG_FILE_PATH__)
        else:
            raise FileNotFoundError("Can't find the 'pytest.ini', please check the file")
        driver_type = conf.get('driver', 'type')
        if driver_type in ['Chrome', 'Firefox', 'Ie']:
            browser = eval("webdriver." + driver_type)(executable_path=settings.CHROME_DRIVER_PATH)
            self.__BROWSER_LIST__.append(browser)
        else:
            raise KeyError("driver type just can be Chrome, Firefox, Ie")

    def get_current_browser(self):
        # print("get current browser")
        if len(self.__BROWSER_LIST__) > 0:
            return self.__BROWSER_LIST__[-1]
        else:
            raise NoOpenBrowser("No browser opened")

    def switch_browser(self, index):
        tmp = self.__BROWSER_LIST__.pop(index)
        self.__BROWSER_LIST__.append(tmp)
        return self.get_current_browser()

    def close_browser(self, index):
        self.__BROWSER_LIST__.pop(index).quit()

    def close_all_browser(self):
        while len(self.__BROWSER_LIST__) > 0:
            self.__BROWSER_LIST__.pop().quit()


