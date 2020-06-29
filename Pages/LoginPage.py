# -*- coding:utf-8 -*-

from base.basepage import BasePage
from pages.LoginPageXpathElement import *


class LoginPage(BasePage):

    class Elements(BasePage.Elements):

        @property
        def name_box(self):
            """搜索输入框"""
            return self.page.find_element_by_xpath(search_content)

        @property
        def search_btn(self):
            """搜索按钮"""
            return self.page.find_element_by_xpath(search_btn)

    class Actions(BasePage.Actions):
        def name(self, name):
            """输入内容"""
            self.page.elements.name_box.clear()
            self.page.elements.name_box.send_keys(name)
            return self

        def search(self):
            """点击搜索按钮"""
            self.page.elements.search_btn.click()
            return self