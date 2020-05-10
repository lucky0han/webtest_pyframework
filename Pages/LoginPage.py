from Base.BasePage import BasePage


class LoginPage(BasePage):

    class Elements(BasePage.Elements):

        @property
        def name_box(self):
            """用户名输入框"""
            xpath = '//input[@id="kw"]'
            return self.page.find_element_by_xpath(xpath)

        @property
        def search_btn(self):
            """用户名输入框"""
            xpath = '//input[@id="su"]'
            return self.page.find_element_by_xpath(xpath)

    class Actions(BasePage.Actions):
        def name(self, name):
            """输入用户名"""
            self.page.elements.name_box.clear()
            self.page.elements.name_box.send_keys(name)
            return self

        def search(self):
            """点击登录按钮"""
            self.page.elements.search_btn.click()
            return self