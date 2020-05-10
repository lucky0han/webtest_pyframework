# -*- coding:utf-8 -*-
import configparser
import os
import settings
from selenium import webdriver


class BrowserManager(object):
    config_file_path = os.path.join(settings.PROJECT_DIR, "pytest.ini")
    Browser_List = []

    def create_browser(self):
        print(self.config_file_path)
        conf = configparser.ConfigParser()
        if os.path.exists(self.config_file_path):
            conf.read(self.config_file_path)
        else:
            raise FileNotFoundError("Can't find the 'pytest.ini', please check the file")
        driver_type = conf.get('driver', 'type')
        if driver_type in ['Chrome', 'Firefox', 'Ie']:
            browser = eval("webdriver." + driver_type)(executable_path=settings.CHROME_DRIVER_PATH)
            self.Browser_List.append(browser)
            print("BrowserManager id", id(self.Browser_List))
        else:
            raise KeyError("Driver type just can be Chrome, Firefox, Ie")

    def get_current_browser(self):
        # print("get current browser")
        if len(self.Browser_List) > 0:
            return self.Browser_List[-1]
        else:
            self.create_browser()
            return self.get_current_browser()

    def switch_browser(self, index):
        tmp = self.Browser_List.pop(index)
        self.Browser_List.append(tmp)
        return self.get_current_browser()

    def close_browser(self, index):
        self.Browser_List.pop(index).quit()

    def close_all_browser(self):
        while len(self.Browser_List) > 0:
            self.Browser_List.pop().quit()


