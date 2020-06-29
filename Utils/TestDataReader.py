# -*- coding:utf-8 -*-
import xlrd

class TestDataReader(object):
    TEST_NAME = ('Test Name', '测试用例名称')
    TEST_DATA_TITLE = ('Test Data Title', '测试数据标题，以测试用例函数名开头')
    TEST_DATA = ('Test Data', '测试数据')

    def __init__(self, file_path):
        self.book = xlrd.open_workbook(file_path)
        self.sheet = self.book.sheets()[0]

    def get_rows(self):
        """获取excel行数"""
        rows = self.sheet.nrows
        if rows:
            return rows
        else:
            return None

    def check_data(self,  param_list, data_list):
        """数据校验"""
        params_length = len(param_list)
        data_list_length = len(data_list)

        if params_length == 0:
            raise ValueError("No Param Name Given")

        if data_list_length == 0:
            raise ValueError("No Param Given")
        else:
            for data in data_list:
                if len(data) == params_length:
                    continue
                else:
                    raise ValueError("Params List Length Not Match")

    def list_to_dict(self, param_list, data_list):
        """获取有效数据，去除参数名为空的项"""
        testdatas = []
        while True:
            if param_list[-1] == '':
                param_list.pop()
            else:
                break
        params_valid_length = len(param_list)
        data_valid_list = []
        for data in data_list:
            testData = {}
            while True:
                if len(data) > params_valid_length:
                    data.pop()
                elif len(data) == params_valid_length:
                    # data_valid_list.append(testdata)
                    break
                else:
                    raise ValueError("Param length is different from value length")
            for index, param in enumerate(param_list):
                testData.update({param: data[index]})
            testdatas.append(testData)
        # return params, data_valid_list
        return testdatas

    def get_data(self, case_function_name):
        """根据给定的测试用例名称获取数据"""
        data_list = []
        params_list = []
        row_sum = self.get_rows()
        if row_sum:
            for index in range(row_sum):
                if self.sheet.cell_value(index, 0) == self.TEST_NAME[0] and \
                        self.sheet.cell_value(index, 1) == case_function_name:
                    param_row_value = self.sheet.row_values(index + 1)
                    if param_row_value[0] == self.TEST_DATA_TITLE[0]:
                        params_list = param_row_value[1:]
                    else:
                        raise ValueError("Excel format error")

                    for i in range(row_sum - index - 1):
                        row_num = index + i + 2
                        # print("index:{}".format(index))
                        # print("row_num:{}".format(row_num))
                        if row_num < row_sum:
                            row_value = self.sheet.row_values(row_num)
                            if row_value[0] == self.TEST_DATA[0]:
                                # print(row_value)
                                data = row_value[1:]
                                data_list.append(data)
                            else:
                                break
                        else:
                            break
                else:
                    continue
            self.check_data(params_list, data_list)
            # params, data_list = self.data_deal(params, data_list)
            testDatas = self.list_to_dict(params_list, data_list)
            # print("params:", params)
            # print("testDatas:", testDatas)
            return testDatas
        else:
            raise AssertionError("Please check testdata file path")