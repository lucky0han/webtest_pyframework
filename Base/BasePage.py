# -*- coding:utf-8 -*-
from selenium import webdriver


class BasePage(object):
    driver_saver = None

    def __init__(self):
        if(self.driver_saver == None):
            driver = webdriver.Chrome()
            driver.get(web_ip)
            driver.maximize_window()