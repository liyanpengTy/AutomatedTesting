# -*- coding: utf-8 -*-
# @File    :statementElement
# @Date    :2023/3/31 15:24
# @Name    :LYP
""" 报表元素 """

from selenium.webdriver.common.by import By

def header(number=1):
    # 获取报表表头，默认第一行。使用时，检查此元素是否可选中目标
    return By.XPATH, "(//tr)[" + str(number) + "]/th"

def rowData(lineNumber):
    # 获取报表中第lineNumber行的数据
    return By.XPATH, "//tbody[@class='ivu-table-tbody']/tr[" + str(lineNumber) + "]/td"

def columnData(columnNumber):
    # 获取报表中第columnNumber列的数据
    return By.XPATH, "//tbody[@class='ivu-table-tbody']/tr/td[" + str(columnNumber) + "]"

def preciseData(lineNumber, columnNumber):
    # 获取报表中第lineNumber行、第columnNumber列的数据
    return By.XPATH, "//tbody[@class='ivu-table-tbody']/tr[" + str(lineNumber) + "]/td[" + str(columnNumber) + "]"