# -*- coding:utf-8 -*-
import configparser
import os
from selenium import webdriver


class BrowserManager(object):
    config_file_path = ".." + os.sep + "pytest.ini"

    def __init__(self):
        self.Browser_List = []

    def create_browser(self):
        conf = configparser.ConfigParser()
        if os.path.exists(self.config_file_path):
            conf.read(self.config_file_path)
        else:
            raise FileNotFoundError("Can't find the 'config.ini', please check the file")
        driver_type = conf.get('driver', 'type')
        if driver_type in ['Chrome', 'Firefox', 'Ie']:
            browser = eval("webdriver." + driver_type)()
            self.Browser_List.append(browser)
        else:
            raise KeyError("Driver type just can be Chrome, Firefox, Ie")

    def get_current_browser(self):
        if len(self.Browser_List) > 0:
            return self.Browser_List[-1]
        else:
            self.create_browser()
            self.get_current_browser()

    def switch_browser(self, index):
        tmp = self.Browser_List.pop(index)
        self.Browser_List.append(tmp)
        return self.get_current_browser()

    def close_browser(self, index):
        self.Browser_List.pop(index).quit()

    def close_all_browser(self):
        while len(self.Browser_List) > 0:
            self.Browser_List.pop().quit()


