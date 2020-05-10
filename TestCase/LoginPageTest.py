# -*- coding:utf-8 -*-

"""
登录页面测试示例
@author hanfeng
"""
import pytest

from Base.BaseCase import BaseCase
from Pages.LoginPage import LoginPage

class LoginPageTest(BaseCase):
    
    def setup_class(self):
        
        pass
        
    def setup_method(self):
        
        pass    
    
    @pytest.mark.testcase("success search", author="hanfeng", editor="")
    def test_successfully_login(self, testdata):
        name    = testdata.get("搜索内容")
        url     = testdata.get("登录页面URL")

        page = LoginPage()
        page.open_url(url).actions.name(name).sleep(2).search().sleep(3)
        page.sleep(3)
        
    def teardown_method(self):
        
        pass
        
    def teardown_class(self):
        self.BROWSER_MANAGER.close_all_browser()
        
if __name__=="__main__":
    pass