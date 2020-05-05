# -*- coding:utf-8 -*-
from Base import BasePage


class BaseCase(object):
    BROWSER_MANAGER = BasePage.BasePage.driver_manager
    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.BROWSER_MANAGER.close_all_browser()