# -*- coding:utf-8 -*-
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.DriverManager import BrowserManager
from Utils import Screenshot
import time
import setting


class BasePage(object):
    screenshot_folder_path = setting.SCREENSHOTS_DIR
    driver_manager = BrowserManager()
    _screenshot = Screenshot()
    timeout = 0

    def __init__(self):
        self._driver = self.driver_manager.get_current_browser()
        self._wait = WebDriverWait(self._driver, self.conf.get('driver', 'wait_time'))
        self.elements = self.Elements(self)
        self.actions = self.Actions(self)

    def _is_webelement(self, element):

        return isinstance(element, WebElement)

    def _validate_timeout(self, timeout):

        return isinstance(timeout, (int, float))

    def switch_browser(self, index):
        self._driver = self.driver_manager.switch_browser(index)

    def find_element_by_xpath(self, locator):
        self._wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return self._driver.find_element_by_xpath(locator)

    def execute_javascript(self, script_cmd, *args):
        """执行javascript脚本"""
        self._driver.execute_script(script_cmd, *args)

    def click_xpath_by_javascript(self, xpath):
        """通过JavaScript向input元素输入文本"""
        js = "Elements = document.evaluate('{}', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);" \
             "item = Elements.snapshotItem(0);" \
             "item.click()".format(xpath)
        self._driver.execute_script(js)

    def is_element_enabled(self, element):
        """判断元素是否可用"""
        return (element.is_enabled() and element.get_attribute("readonly") is None)

    def find_elements(self, by=By.ID, locator=None, timeout=None, parent=None):
        """
        查找所有匹配的元素

        @param by - 查找方式
        @param locator - 元素定位器
        @param timeout - 查找元素超时时间
        @param parent - 父元素,提供则从父元素下查找
        @return  list of WebElement - a list with elements if any was found. An empty list if not
        """

        if not (timeout and self._validate_timeout(timeout)):
            timeout = self.timeout

        if parent and self._is_webelement(parent):
            driver = parent.parent
        else:
            driver = self._driver
        message = "{} with locator '{}' not found.".format(by, locator)
        try:
            elements = WebDriverWait(driver, timeout).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            message = message + "in {timeout}".format(timeout=timeout)
            screen = getattr(t, 'screen', None)
            stacktrace = getattr(t, 'stacktrace', None)
            raise TimeoutException(message, screen, stacktrace)
        except NoSuchWindowException as e:
            screen = getattr(e, 'screen', None)
            stacktrace = getattr(e, 'stacktrace', None)
            raise NoSuchWindowException(message, screen, stacktrace)
        except Exception as e:
            print(message)
            raise e
        else:
            return elements

    def screenshot(self):
        self._screenshot(self._driver, self.screenshot_folder_path)

    class Elements(object):

        def __init__(self, page):
            self.page = page

    class Actions(object):

        def __init__(self, page):
            self.page = page

        def sleep(self, seconds):
            time.sleep(seconds)
            return self
