# -*- coding: utf-8 -*-
# @File    :appraisalResultElement
# @Date    :2023/3/28 17:09
# @Name    :LYP
""" 房屋智能估价（单套） - 估价结果页 """

from Common.Log import log
from selenium.webdriver.common.by import By

def AppraisalObject(number):
    # 估价对象 **  1：估价结果页； 2：下载估价pdf弹框
    return By.XPATH, "(//div[@class='top']/div[@class='title'])[" + str(number) + "]"

def CommunityDistrict(number):
    # 小区名称&行政区 **  1：估价结果页； 2：下载估价pdf弹框
    return By.XPATH, "(//div[@class='address'])[" + str(number) + "]"

def ValuationTime(number):
    # 估价时间 **  1：估价结果页； 2：下载估价pdf弹框
    return By.XPATH, "(//div[@class='time'])[" + str(number) + "]"

def AppraisalResult(choose, number=None):
    # 估价结果 1：估价结果页； 2：下载估价pdf弹框
    if choose == 0:
        return By.XPATH, "(//div[text()='总价(万元）'])[" + str(number) + "]"
    elif choose == 1:
        return  By.XPATH, "(//div[text()='参考总价(万元）'])[" + str(number) + "]"
    elif choose == 2:
        return By.XPATH, "//div[text()=' 正估价中']"
    elif choose == 3:
        return By.XPATH, "//div[text()='暂无法估价']"
    else:
        log.warning("||请选择正确的元素")

def HouseProperties(number):
    # 房屋属性
    return By.XPATH, "((//div[@class='detail'])[1]/div/div/span)[" + str(number) +"]"