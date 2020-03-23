# -*- coding:utf-8 -*-
import configparser
import os


class DriverManager(object):
    config_file_path = ".." + os.sep + "config.ini"

    def __init__(self):
        self.Browser_List = []
        self.create_browser()

    def create_browser(self):
        conf = configparser.ConfigParser()
        if os.path.exists(self.config_file_path):
            conf.read(self.config_file_path)
        else:
            raise FileNotFoundError("Can't find the 'config.ini', please check the file")
        driver_type = conf.get('driver', 'type')
        default_ip = conf.get('driver', 'ip')
        if driver_type in ['Chrome', 'Firefox', 'Ie']:
            browser = eval("webdriver." + driver_type)()
            browser.get(default_ip)
            self.Browser_List.append(browser)
        else:
            raise KeyError("Driver type just can be Chrome, Firefox, Ie")

    def get_current_browser(self):
        if len(self.Browser_List) > 0:
            return self.Browser_List.pop()
        else:
            self.create_browser()
            self.get_current_browser()

    def switch_browser(self, index):
        return self.Browser_List[index]

    def close_browser(self, index):
        self.Browser_List.pop(index).quit()

    def close_all_browser(self):
        while len(self.Browser_List) > 0:
            self.Browser_List.pop().quit()


