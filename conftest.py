# -*- coding: utf-8 -*-
import json
import os
from Expection import NoOpenBrowser
import pytest
from py._xmlgen import html
import settings
from datetime import datetime
from Utils import TestDataReader
from Utils import Screenshot


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('TestData'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.insert(4, html.th('Author'))
    cells.insert(5, html.th('Editor'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description if hasattr(report, "description") else ""))
    cells.insert(2, html.td(report.testdata if hasattr(report, "testdata") else ""))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.insert(4, html.td(report.author if hasattr(report, "author") else ""))
    cells.insert(5, html.td(report.editor if hasattr(report, "editor") else ""))
    # cells.insert(1,html.td(Report.nodeid))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = item.function.__doc__ if item.function.__doc__ else item.function.__name__
    extra = getattr(report, 'extra', [])

    if report.when == "call":  # 测试用例失败自动截图

        # fill testdata
        args = {}
        for argname in item._fixtureinfo.argnames:
            args[argname] = item.funcargs[argname]
        setattr(report, "testdata", json.dumps(args, ensure_ascii=False))

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                browser = item.cls.BROWSER_MANAGER.get_current_browser()
            except NoOpenBrowser:
                browser = None
            capturer = Screenshot()
            # folder_name = settings.SCREENSHOTS_DIR + os.sep + report.description
            folder_name = report.description
            ss_result, ss_path = capturer(browser, folder_name)
            print(ss_path)
            if settings.ATTACH_SCREENSHOT_TO_HTML_REPORT:
                template = """<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" onclick="window.open(this.src)" align="right"/></div>"""
                html = template % Screenshot.screenshot_file_to_base64(ss_path) if ss_result else """<div>截图失败</div>"""
                extra.append(pytest_html.extras.html(html))
    report.extra = extra


def pytest_generate_tests(metafunc):
    for marker in metafunc.definition.iter_markers():
        if marker.name == settings.TESTCASE_MARKER_NAME:
            metafunc.function.__doc__ = "".join(marker.args)
            break
    test_class_name = metafunc.cls.__name__
    test_method_name = metafunc.function.__name__
    testdata_file_path = os.path.join(settings.TEST_DATA_EXCEL_DIR, test_class_name + ".xlsx")
    # print('TEST_DATA_EXCEL_DIR', settings.TEST_DATA_EXCEL_DIR)
    # print(testdata_file_path)
    this_case_datas = TestDataReader(testdata_file_path).get_data(test_method_name)

    argnames = metafunc.definition._fixtureinfo.argnames

    if len(argnames) < 1:
        argname = ""
        this_case_datas = []
    elif len(argnames) < 2:
        argname = argnames[0]
    else:
        emf = "{funcname}() can only be at most one parameter, but multiple parameters are actually defined{args}"
        raise TypeError(emf.format(funcname=test_method_name, args=", ".join(argnames)))
    metafunc.parametrize(argname, this_case_datas)
