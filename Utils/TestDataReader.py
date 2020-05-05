# -*- coding:utf-8 -*-
import xlrd

class TestDataReader(object):

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

    def check_data(self,  params, data_list):
        """数据校验"""
        params_length = len(params)
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

    def data_deal(self, params, data_list):
        """获取有效数据，去除参数名为空的项"""
        while True:
            if params[-1] == '':
                params.pop()
            else:
                break
        params_valid_length = len(params)
        data_valid_list = []
        for data in data_list:
            while True:
                if len(data) > params_valid_length:
                    data.pop()
                elif len(data) == params_valid_length:
                    data_valid_list.append(data)
                    break
                else:
                    raise ValueError("Param length is different from value length")
        return params, data_valid_list

    def get_data(self, target_name):
        """根据给定的测试用例名称获取数据"""
        data_list = []
        params = []
        row_sum = self.get_rows()
        if row_sum:
            for index in range(row_sum):
                if self.sheet.cell_value(index, 1) == target_name:
                    param_row_value = self.sheet.row_values(index + 1)
                    if param_row_value[0] == 'Test Data Title':
                        params = param_row_value[1:]
                    else:
                        raise ValueError("Excel format error")

                    for i in range(row_sum - index - 1):
                        row_num = index + i + 2
                        # print("index:{}".format(index))
                        # print("row_num:{}".format(row_num))
                        if row_num < row_sum:
                            row_value = self.sheet.row_values(row_num)
                            if row_value[0] == 'Test Data':
                                # print(row_value)
                                data = row_value[1:]
                                data_list.append(data)
                            else:
                                break
                        else:
                            break
                else:
                    continue
            self.check_data(params, data_list)
            params, data_list = self.data_deal(params, data_list)
            return params, data_list
        else:
            raise AssertionError("Please check data file path")