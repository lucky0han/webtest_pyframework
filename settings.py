# -*- coding: utf-8 -*-

"""
配置文件
"""
import logging
import os


#settings.py 所在目录路径
BASE_DIR                                = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR                             = os.getcwd()

#日志目录
LOGS_DIR                                = os.path.join(PROJECT_DIR, "logs")

DATE_FORMAT                             = "%m/%d/%Y %H:%M:%S %p"
LOG_FORMAT                              = "%(asctime)s - %(levelname)s - %(thread_name)s - %(message)s"
logging.basicConfig(
                        filename=LOGS_DIR + os.sep + "record.log",
                        filemode="w",
                        format=LOG_FORMAT,
                        level=logging.INFO,
                        datefmt=DATE_FORMAT
                    )

#浏览器驱动目录
DRIVERS_DIR                             = os.path.join(PROJECT_DIR, "driver")

#谷歌浏览器驱动完整路径
CHROME_DRIVER_PATH                      = os.path.join(DRIVERS_DIR, "chromedriver.exe")

#测试报告存放目录
REPORT_DIR                              = os.path.join(PROJECT_DIR, "report")

#测试用例数据目录
TEST_DATA_EXCEL_DIR                     = os.path.join(PROJECT_DIR, "testdata")

#截图目录
SCREENSHOTS_DIR                         = os.path.join(PROJECT_DIR, "screenshot")

#HTML测试报告文件名
HTML_REPORT_NAME                        = "uitest_report.html"

TESTCASES_DIR                           = os.path.join(BASE_DIR, "testcases")

#测试用例文件名
TESTCASES_FILENAME                      = "*Test.py"

#测试用例标记
TESTCASE_MARKER_NAME                    = "testcase"

# 测试用例所在类名
TESTCASES_CLASS                         = "*Test"

# 测试用例函数名
TESTCASES_FUNCTIONS                         = "test_*"

#HTML 测试报告完整路径
HTML_REPORT_FILE_PATH                   = os.path.join(REPORT_DIR, HTML_REPORT_NAME)

#是否把截图添加到HTML报告上
ATTACH_SCREENSHOT_TO_HTML_REPORT        = True

#执行测试的pytest命令
PYTEST_COMMANDS                         = ["-s",'--html=%s' % HTML_REPORT_FILE_PATH, '--self-contained-html']