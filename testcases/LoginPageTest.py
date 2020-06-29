# -*- coding:utf-8 -*-

"""
登录页面测试示例
@author hanfeng
"""
import pytest
from base.basecase import BaseCase
from pages.LoginPage import LoginPage

class LoginPageTest(BaseCase):
    
    def setup_class(self):
        
        pass
        
    def setup_method(self):
        
        pass    
    
    @pytest.mark.testcase(name="success search", author="hanfeng", editor="")
    def test_successfully_login(self, testdata):
        name    = testdata.get("搜索内容")
        url     = testdata.get("登录页面URL")
        # page = LoginPage()
        # page.open_url(url).actions.name(name).sleep(2).search().sleep(3)
        # page.sleep(3)
        assert 1 == 1

    @pytest.mark.testcase(name="success search2")
    def test_successfully_login2(self, testdata):
        name = testdata.get("搜索内容")
        url = testdata.get("登录页面URL")
        assert 1 == 2

        
    def teardown_method(self):
        
        pass
        
    def teardown_class(self):
        # self.BROWSER_MANAGER.close_all_browser()
        pass

if __name__=="__main__":
    pass