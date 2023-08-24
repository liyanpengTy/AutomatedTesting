# -*- coding: utf-8 -*-
# @File    :rapidValuationElement
# @Date    :2023/3/28 17:08
# @Name    :LYP
""" 房屋智能估价（单套） - 快速估价页"""

from Common.Log import log
from selenium.webdriver.common.by import By


def cityBox(number):
    # 1:估价页-城市选择框；2:手动提交估价弹框-城市选择框
    return By.XPATH, "(//span[@class='ivu-select-selected-value'])[" + str(number) + "]"


def cityList(attribute, choose=0, number=None):
    if attribute == "page":
        # 快速估价页面
        if choose == 0:
            # 城市列表
            return By.XPATH, "//li[@data-v-d9801f5e='']"
        else:
            # 城市列表第number个值
            return By.XPATH, "(//li[@data-v-d9801f5e=''])[" + str(number) + "]"
    elif attribute == "Popout":
        # 手动提交弹框
        if choose == 0:
            return By.XPATH, "//li[@data-v-1f01b264='']"
        else:
            return By.XPATH, "(//li[@data-v-1f01b264=''])[" + str(number) + "]"
    else:
        log.error("||attribute选择错误，请输入【page】/【Popout】")


def inputBox(text, number=1):
    # 快速估价输入或选择框
    return By.XPATH, "(//input[@placeholder='" + str(text) + "'])[" + str(number) + "]"


def whetherDisabled(text, number=1):
    # text=请选择，number控制输入框的位置
    return By.XPATH, "(//input[@disabled='disabled'][@placeholder='" + str(text) + "'])[" + str(number) + "]"


def communityDropList(choose=0, number=None):
    if choose == 0:
        # 小区下拉列表
        return By.XPATH, "//li[@class='slice']"
    elif choose == 1:
        # 小区下拉列表第number个值
        return By.XPATH, "(//li[@class='slice'])[" + str(number) + "]"
    elif choose == 2:
        # 找不到你想要的小区  1：小区估价 4：地址估价
        return By.XPATH, "(//div[text()=' 手动提交估价 '])[" + str(number) + "]"
    else:
        # 获取除输入条件外的字符
        return By.XPATH, "//li[@class='slice']/span/span/text()"


def BuildingNumberDropList(choose=0, number=None):
    if choose == 0:
        # 楼栋/房号下拉列表
        return By.XPATH, "//li[@role='option']"
    elif choose == 1:
        # 楼栋/房号下拉列表第number个值
        return By.XPATH, "(//li[@role='option'])[" + str(number) + "]"
    else:
        log.error("||请选择正确的元素")


def protocol(number):
    # 用户协议。1：小区估价； 2：地址估价
    return By.XPATH, "(//span[@class='ivu-checkbox'])[" + str(number) + "]"


def PresentValuationButton(number):
    # 现在估价按钮。1：小区估价； 2：地址估价； 3：手动提交估价
    return By.XPATH, "(//span[text()='现在估价'])[" + str(number) + "]"


def more(number):
    # 更多展开控件。1：小区估价； 2：地址估价； 3：手动提交估价
    return By.XPATH, "(//div[text()='更多 '])[" + str(number) + "]"


def dropDownList(number=None):
    # 选中的下拉框列表; number为下拉列表第N个
    if number == None:
        return By.XPATH, "//div[@x-placement='bottom-start']/div/div/ul/li"
    else:
        return By.XPATH, "(//div[@x-placement='bottom-start']/div/div/ul/li)[" + str(number) + "]"


def selectionDays(function, number=None):
    if function == "年份区间":
        return By.XPATH, "(//span[@class='el-date-picker__header-label'])[1]"
    elif function == "前一年":
        return By.XPATH, "//button[@aria-label='前一年']"
    elif function == "后一年":
        return By.XPATH, "//button[@aria-label='后一年']"
    elif function == "选择年份":
        return By.XPATH, "//a[text()='" + str(number) + "']"
    else:
        log.error("||function选择错误，请输入【年份区间】/【前一年】/【后一年】/【选择年份】")
