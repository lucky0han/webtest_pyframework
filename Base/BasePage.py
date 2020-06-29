# -*- coding:utf-8 -*-
import logging

from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from base.browsermanager import BrowserManager
from utils import Screenshot
import time
import settings
import configparser

from utils.logtools import logger


class BasePage(object):
    __SCREENSHOT_FOLDER_PATH__ = settings.SCREENSHOTS_DIR
    __BROWSER_MANAGER__ = BrowserManager()
    __SCREENSHOT__ = Screenshot()
    __TIMEOUT__ = 0

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(BrowserManager.__CONFIG_FILE_PATH__)
        self._wait = WebDriverWait(self.__browser, float(self.conf.get('driver', 'wait_time')))
        self.elements = self.Elements(self)
        self.actions = self.Actions(self)

    def create_browser(self):
        self.__BROWSER_MANAGER__.create_browser()
        self.__browser = self.__BROWSER_MANAGER__.get_current_browser()
        return self

    def current_browser(self):
        self.__browser = self.__BROWSER_MANAGER__.get_current_browser()
        return self

    def switch_browser(self, index):
        self.__browser = self.__BROWSER_MANAGER__.switch_browser(index)
        return self

    def close_browser(self, index=None):
        if index is None:
            self.__browser.quit()
        else:
            self.__BROWSER_MANAGER__.close_browser(index)

    def close_all_browser(self):
        self.__BROWSER_MANAGER__.close_all_browser()

    def _is_webelement(self, element):
        return isinstance(element, WebElement)

    def _validate_timeout(self, timeout):
        return isinstance(timeout, (int, float))

    def open_url(self, url):
        """打开指定的url"""
        self.__browser.get(url)
        return self

    def execute_javascript(self, script_cmd, *args):
        """执行javascript脚本"""
        self.__browser.execute_script(script_cmd, *args)

    def click_xpath_by_javascript(self, xpath):
        """通过JavaScript向input元素输入文本"""
        js = "Elements = document.evaluate('{}', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);" \
             "item = Elements.snapshotItem(0);" \
             "item.click()".format(xpath)
        self.__browser.execute_script(js)

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
            timeout = self.__TIMEOUT__

        if parent and self._is_webelement(parent):
            driver = parent.parent
        else:
            driver = self.__browser
        message = "{} with locator '{}' not found.".format(by, locator)
        try:
            elements = WebDriverWait(driver, timeout).until(lambda x: x.find_elements(by, locator))
        except Exception as e:
            logger(message, level=logging.ERROR)
            raise e
        else:
            return elements

    def find_element(self, by=By.ID, locator=None, timeout=None, parent=None):
        """
        查找所有匹配的元素

        @param by - 查找方式
        @param locator - 元素定位器
        @param timeout - 查找元素超时时间
        @param parent - 父元素,提供则从父元素下查找
        @return  list of WebElement - a list with elements if any was found. An empty list if not
        """

        if not (timeout and self._validate_timeout(timeout)):
            timeout = self.__TIMEOUT__

        if parent and self._is_webelement(parent):
            driver = parent.parent
        else:
            driver = self.__browser
        message = "{} with locator '{}' not found.".format(by, locator)
        try:
            element = WebDriverWait(driver, timeout).until(lambda x: x.find_element(by, locator))
        except Exception as e:
            logger(message, level=logging.ERROR)
            raise e
        else:
            return element

    def screenshot(self, img_name):
        img_path = self.__SCREENSHOT_FOLDER_PATH__ + img_name
        self.__SCREENSHOT__(self.__browser, img_path)

    def sleep(self, seconds):
        time.sleep(seconds)

    def maximize_window(self):

        self.__browser.maximize_window()
        return self

    def minimize_window(self):

        self.__browser.minimize_window()
        return self

    def find_elements_by_xpath(self, xpath, timeout=None, parent=None):
        """
        Finds an element by xpath.

        @param xpath - The xpath locator of the element to find.

        @return WebElement - the element if it was found

        @raise NoSuchElementException - if the element wasn't found

        @usage  element = driver.find_element_by_xpath('//div/td[1]')
        """

        return self.find_elements(by=By.XPATH, locator=xpath, timeout=timeout, parent=parent)

    def find_element_by_xpath(self, xpath, timeout=None, parent=None):
        """
        Finds an element by xpath.

        @param xpath - The xpath locator of the element to find.

        @return WebElement - the element if it was found

        @raise NoSuchElementException - if the element wasn't found

        @usage  element = driver.find_element_by_xpath('//div/td[1]')
        """

        return self.find_element(by=By.XPATH, locator=xpath, timeout=timeout, parent=parent)

    def scroll_to(self, xpos, ypos):
        """scroll to any position of an opened window of browser"""

        js_code = "window.scrollTo(%s, %s);" % (xpos, ypos)
        self.execute_script(js_code)

    def execute_script(self, script, *args):

        return self.__browser.execute_script(script, *args)

    def scroll_to_bottom(self):
        bottom = self.execute_script("return document.body.scrollHeight;")
        self.scroll_to(0, bottom)

    def scroll_to_top(self):
        self.scroll_to(0, 0)

    def drag_and_drop(self, source, target):

        ac = ActionChains(self.__browser)
        ac.drag_and_drop(source, target).perform()

    def move_by_offset(self, xoffset, yoffset):

        ac = ActionChains(self.__browser)
        ac.move_by_offset(xoffset, yoffset).perform()

    def move_to_element(self, to_element):

        ac = ActionChains(self.__browser)
        ac.move_to_element(to_element).perform()

    def click_and_hold(self, on_element=None):
        ac = ActionChains(self.__browser)
        ac.click_and_hold(on_element).perform()

    @property
    def action_chains(self):
        ac = ActionChains(self.__browser)
        return ac

    def switch_window(self, window_name_or_handle):
        """切换浏览器窗口

        @param window_name_or_handle 窗口句柄或窗口名
        """
        self.__browser.switch_to.window(window_name_or_handle)

    def select_frame(self, reference):
        """切换frame

        @param reference frame id name index 或 webelement 对象
        @see selenium.webdriver.remote.switch_to.SwitchTo.frame()
        @usage page.select_frame()
        """
        self.__browser.switch_to.frame(reference)

    def default_frame(self):
        """ Switch focus to the default frame.

        @see selenium.webdriver.remote.switch_to.SwitchTo.default_content()
        @usage page.default_frame()
        """
        self.__browser.switch_to.default_content()

    def parent_frame(self):
        """嵌套frame时，可以从子frame切回父frame

        @see selenium.webdriver.remote.switch_to.SwitchTo.parent_frame()
        @usage page.parent_frame()
        """

        self.__browser.switch_to.parent_frame()

    class Elements(object):

        def __init__(self, page):
            self.page = page

    class Actions(object):

        def __init__(self, page):
            self.page = page

        def sleep(self, seconds):
            time.sleep(seconds)
            return self
