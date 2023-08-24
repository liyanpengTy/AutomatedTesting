# -*- coding: utf-8 -*-
# @File    :flipOverElement
# @Date    :2023/3/31 11:12
# @Name    :LYP
""" 分页控件元素 """

from selenium.webdriver.common.by import By

def ashSetting():
    # 向前/先后按钮置灰
    return By.XPATH, "//button[@disabled='disabled']"

def pageForwarrdOff():
    # 向前翻页按钮置灰
    return By.XPATH, "//button[@disabled='disabled'][@class='btn-prev']"

def backpageOff():
    # 向后翻页按钮置灰
    return By.XPATH, "//button[@disabled='disabled'][@class='btn-next']"

def pageForwarrdOn():
    # 向前翻页按钮
    return By.XPATH, "//button[@class='btn-prev']"

def backpage():
    # 向后翻页按钮
    return By.XPATH, "//button[@class='btn-next']"

def currentPage():
    # 当前的页码
    return By.CLASS_NAME, "//li[@class='number active']"

def pageHopping():
    # 跳页输入框
    return By.CLASS_NAME, "//input[@class='el-input__inner']"

def numberPages():
    # 总页数的页码列表
    return By.XPATH, "//ul[@class='el-pager']/li"

def selectPageNumber(number):
    # 选中第number个页码
    return By.XPATH, "//ul[@class='el-pager']/li[" + str(number) + "]"