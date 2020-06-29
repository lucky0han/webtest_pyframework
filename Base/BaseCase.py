# -*- coding:utf-8 -*-
from base import basepage


class BaseCase(object):
    BROWSER_MANAGER = basepage.BasePage.__BROWSER_MANAGER__
    __test__ = True

    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.BROWSER_MANAGER.close_all_browser()