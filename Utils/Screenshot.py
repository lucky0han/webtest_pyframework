# -*- coding:utf-8 -*-
import base64
import os
import pyautogui
from selenium import webdriver
import time
import settings


class Screenshot(object):

    def __call__(self, driver, save_folder_path, image_name=None):
        self._save_folder_path = settings.SCREENSHOTS_DIR + os.sep + save_folder_path
        if image_name is None:
            self._image_name = "{}.png".format(time.strftime('%Y%m%d%H%M%S'))
        self._image_path = self._save_folder_path + os.sep + self._image_name
        self._driver = driver
        result = self.browser_screenshot()
        return result, self._image_path

    def browser_screenshot(self):
        if isinstance(self._driver, (webdriver.Chrome, webdriver.Firefox, webdriver.Ie)):
            if not os.path.isdir(self._save_folder_path):
                os.makedirs(self._save_folder_path)
            if self._driver.get_screenshot_as_file(self._image_path):
                self._driver.quit()
                return True
            else:
                Screenshot.screen_screenshot(self._image_path)

    def screen_screenshot(self):
        img = pyautogui.screenshot()
        try:
            img.save(self._image_path, "png")
        except ValueError as ve:
            return False
        except IOError as ioe:
            return False
        finally:
            del img
        return True

    @classmethod
    def screenshot_file_to_base64(cls, file_full_path):
        """转为base64 编码数据

        @filename 完整文件路径
        """
        raw_data = ""
        try:
            with open(file_full_path, "rb") as f:
                raw_data = f.read()
        except IOError as err:
            print(err)
        return base64.b64encode(raw_data).decode()
