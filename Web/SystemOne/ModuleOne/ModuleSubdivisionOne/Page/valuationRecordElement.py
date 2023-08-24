# -*- coding: utf-8 -*-
# @File    :valuationRecordElement
# @Date    :2023/3/31 11:04
# @Name    :LYP

from selenium.webdriver.common.by import By

def screeningConditionName():
    # 所有的筛选条件名称列表
    return By.XPATH, "//form[@class='ivu-form ivu-form-label-left ivu-form-inline']/div/label"

def screeningCondition(number):
    # 第number个筛选条件
    return By.XPATH, "//form[@class='ivu-form ivu-form-label-left ivu-form-inline']/div[" + str(number) + "]/div/div[1]"

def cityValuesList():
    # 城市筛选条件下拉列表
    return By.XPATH, "//li[text()='全部 ']/../li"

def numberValuesList(number):
    # 城市下拉列表第number个值
    return By.XPATH, "//li[text()='全部 ']/../li[" + str(number) + "]"

def queryButton():
    # 查询按钮
    return By.XPATH, "//button[@class='ivu-btn ivu-btn-primary ']"