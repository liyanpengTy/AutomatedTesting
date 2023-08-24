# -*- coding: utf-8 -*-
# @File    :test_login
# @Date    :2023/3/28 16:26
# @Name    :LYP

from Common.Log import log
from Common.config import conf
from Common.getExcel import GetExcel
from Common.getTime import countdown
from Common.screenshot import screenshot
from Common.operation_redis import OperationRedis
from Common.initPath import testData_systemOne_login_dir
from Web.SystemOne.LoginModule.Page.loginElement import LoginElement


url = conf.get_value("sys", "base_DP_url")
getExcel = GetExcel(filePath=testData_systemOne_login_dir, sectioName="case", key="testData_systemOne_login")
phone = getExcel.get_sheet()[0]["user"]
# 获取redis中手机号对应value的值
red = OperationRedis("redis")
red.set_redis(phone)  # 若不使用固定“1234”的验证码，则不执行此步骤
code = red.get_value(phone)


def login(driver, newDriver):
    driver.get(url)
    log.info("||打开网址： 【{0}】".format(url))
    newDriver.input(LoginElement.phone_element, phone)
    log.info("||输入手机号：【{0}】".format(phone))
    newDriver.input(LoginElement.code_element, code)
    log.info("||输入验证码：【{0}】".format(code))
    newDriver.click(LoginElement.login_button_element)
    log.info("||点击登录按钮")
    countdown(3)
    screenshot("登录结果", "数据平台登录")
