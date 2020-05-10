# -*- coding: utf-8 -*-

"""
配置文件
"""

import os

PROJECT_DIR                             = os.getcwd()

#浏览器驱动目录
DRIVERS_DIR                             = os.path.join(PROJECT_DIR, "Driver")

#谷歌浏览器驱动完整路径
CHROME_DRIVER_PATH                      = os.path.join(DRIVERS_DIR, "chromedriver.exe")

#测试报告存放目录
REPORT_DIR                              = os.path.join(PROJECT_DIR, "Report")

#测试用例数据目录
TEST_DATA_EXCEL_DIR                     = os.path.join(PROJECT_DIR, "Data")

#截图目录
SCREENSHOTS_DIR                         = os.path.join(PROJECT_DIR, "Screenshot")

#HTML测试报告文件名
HTML_REPORT_NAME                        = "uitest_report.html"

#测试用例标记
TESTCASE_MARKER_NAME                    = "testcase"

#HTML 测试报告完整路径
HTML_REPORT_FILE_PATH                   = os.path.join(REPORT_DIR, HTML_REPORT_NAME)

#python __init__.py file name
PY_INIT_FILE_NAME                       = "__init__.py"

#是否把截图添加到HTML报告上
ATTACH_SCREENSHOT_TO_HTML_REPORT        = True

#执行测试的pytest命令
PYTEST_COMMANDS                         = ["-s",'--html=%s' % HTML_REPORT_FILE_PATH, '--self-contained-html']