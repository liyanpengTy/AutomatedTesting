# -*- coding: utf-8 -*-
# @File    :getExcel
# @Date    :2023/3/27 15:32
# @Name    :LYP

import os
import openpyxl
import pandas as pd
from Common.initPath import *
from Common.config import conf

class GetExcel(object):
    """ 解析，获取Excel数据 """

    def __init__(self, filePath, sectioName, key, sheet_name=None):
        self.note = conf.get_value("identifier", "note")
        self.caseFile = os.path.join(filePath, conf.get_value(sectioName, key))
        self.sheetName = sheet_name
        self.wb = None

    def open_excel(self):
        """
        打开Excel文件，如果sheet不为空，定位到对应的sheet工作表
        :return:
        """
        self.wb = openpyxl.open(self.caseFile)
        if self.sheetName is not None:
            self.sh = self.wb[self.sheetName]

    def read_excels(self):
        """
        格式化用例集；
        用例格式划成JSON格式；
        过滤掉带#（注释）的用例
        :return:
        """
        if self.wb is None:
            self.open_excels()
        datas = list(self.sh.rows)
        title = [i.value for i in datas[0]]
        cases = []
        for i in datas[1:]:
            data = [k.value for k in i]
            # 将数据格式化中JSON串
            case = dict(zip(title, data))
            try:
                # 过滤掉note符号开头的用例，注释掉不收集，不执行
                if str(case["case_id"])[0] is not self.note:
                    case["sheet"] = self.sh.title
                    cases.append(case)
            except KeyError:
                cases.append(case)
        return cases

    def read_all_excel(self):
        """
        遍历所有的sheet工作表
        取得所有的用例集，再格式一下
        过滤掉带#（注释）的用例
        :return:
        """
        self.open_excel()
        cases = []
        for sheet in self.wb:
            # 过滤掉note符号开头的sheet页，注释掉不收集，不执行
            if sheet.title[0] is not self.note:
                self.sh = sheet
                cases += self.read_excels()
        return cases

    def write_excel(self, rows, column, value):
        """
        回写用例字段。
        调用此方法时，sheet_name必须传值，且不能使用其他程序打开对应的文件
        :param rows:
        :param colum:
        :param value:
        :return:
        """
        self.open_excel()
        self.sh.cell(row=rows, column=column, value=value)
        self.wb.save(self.caseFile)

    def get_sheet(self, **kwargs):
        """
        读取Excel
        :param kwargs:
        :return: key 为Excel文件中工作表的第一行;value为其它行的数据;存在多行时，每一行为一个字典， 组合成列表嵌套字典的数据
        """
        data_dict = []
        try:
            data = pd.read_excel(self.caseFile, **kwargs)
            data_dict = data.to_dict('records')
        finally:
            return data_dict


# getExcel = GetExcel(filePath=testData_systemOne_login_dir, sectioName="case", key="testData_systemOne_login")
# getExcel = GetExcel(filePath=data_ModuleOne, sectioName="case", key="data_ModuleOne_api", sheet_name="Sheet1")
# print(getExcel.read_all_excel())
# getExcel.write_excel(rows=2, column=12, value=1010)
# print(getExcel.get_sheet())
# print(getExcel.get_sheet(sheet_name="Sheet1"))
# print(len(getExcel.get_sheet(sheet_name="Sheet1")))