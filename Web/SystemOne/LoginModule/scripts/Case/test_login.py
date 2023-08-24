# -*- coding: utf-8 -*-
# @File    :test_login
# @Date    :2023/3/29 12:20
# @Name    :LYP

import os
import unittest
from Common.Log import log
from Common.config import Config, conf
from Common.sendMsg import sendText
from Common.getExcel import GetExcel
from Common.screenshot import screenshot
from Common.operation_db import OperationDB
from Common.operation_redis import OperationRedis
from Common.getTime import getTime, Time, countdown, getDay
from Common.initPath import testData_systemOne_login_dir, sqlConfig_systemOne_login_dir
from Web.Utils.driverUtils import DriverUtils
from Web.Public.assertion import Pass, failure
from Web.Public.operationMethod import OperationMethod
from Web.SystemOne.LoginModule.Page.loginElement import *

""" 数据平台登录页 """
class TestLogin(unittest.TestCase):
    fileName = os.path.basename(__file__)
    startTime = getTime()
    recordStartTime = Time("DataFormat")
    url = conf.get_value("sys", "base_DP_url")
    select = OperationDB("test_db")
    sqlConfig = Config(config_file=sqlConfig_systemOne_login_dir, fileName="LoginSqlConfig.ini")
    getExcel = GetExcel(filePath=testData_systemOne_login_dir, sectioName="case", key="testData_systemOne_login")
    print("\n")
    log.info("||====================================测试数据====================================")
    Data = getExcel.get_sheet(sheet_name="Sheet2")
    loginData = {}
    # 处理获取的数据，形成特定的嵌套字典
    for i in range(len(Data)):
        borrow_dict = {}
        for key, value in Data[i].items():
            if key != "msg":
                borrow_dict[key] = value
        loginData[Data[i]["msg"]] = borrow_dict
    log.info("||{0}".format(loginData))
    log.info("||====================================测试数据====================================")

    @classmethod
    def setUpClass(cls) -> None:
        print("\n")
        log.info("||==========================开始执行【登录】页面测试用例==========================")
        log.info("||开始时间：【{0}】".format(cls.recordStartTime))
        cls.driver = DriverUtils.getDriver()
        cls.newDriver = OperationMethod(cls.driver)
        cls.driver.get(cls.url)
        log.info("||打开网址：【{0}】".format(cls.url))

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        countdown(1)
        self.driver.refresh()
        print("\n")
        log.info("||==============================执行下一个测试用例==============================")

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quitDriver()
        EndTime = getTime()
        when = (EndTime - cls.startTime).total_seconds()
        print("\n")
        log.info("||==========================================================================")
        log.info("||开始时间: 【{0}】".format(cls.recordStartTime))
        log.info("||结束时间: 【{0}】".format(Time("DataFormat")))
        log.info("||共用时：【{0}】秒".format(when))
        log.info("||==========================结束执行【登录】页面测试用例==========================")
        # sendText.send_text("《登录》页面测试结束，请查看！！！")

    # @pytest.mark.run(order=1)
    # @pytest.mark.flaky(2)
    def test_001(self):
        """ 验证码错误 """
        print("\n")
        log.info("||==========================开始执行【验证码错误】用例==========================")
        user = self.loginData["验证码错误"]["user"]
        code = self.loginData["验证码错误"]["code"]
        self.newDriver.input(LoginElement.phone_element, user)
        log.info("||输入手机号：【{0}】".format(user))
        self.newDriver.input(LoginElement.code_element, code)
        log.info("||输入验证码：【{0}】".format(code))
        self.newDriver.click(LoginElement.login_button_element)
        log.info("||点击登录按钮")
        cue = self.newDriver.getText(LoginElement.cue)
        assert cue == "验证码错误", failure(self.fileName + "_001")
        Pass(self.fileName + "_001")
        log.info("||==========================结束执行【验证码错误】用例==========================")

    # @pytest.mark.run(order=2)
    # @pytest.mark.flaky(2)
    def test_002(self):
        """ 账号已过期"""
        print("\n")
        log.info("||==========================开始执行【账号已过期】用例==========================")
        currentDate = str(Time("DataFormat"))
        SQL = self.sqlConfig.get_value("SQL", "UserExpired").format(currentDate)
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "账号已过期", failure(self.fileName + "_002")
            Pass(self.fileName + "_002")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||==========================开始执行【账号已过期】用例==========================")

    # @pytest.mark.run(order=3)
    # @pytest.mark.flaky(2)
    def test_003(self):
        """ 该用户未到使用时间，如需提前请与我们联系 """
        print("\n")
        currentDate = str(Time("LongDataFormat"))
        log.info("||=======================开始执行【用户未到使用期限】用例========================")
        SQL = self.sqlConfig.get_value("SQL", "CustomerNotArriveServiceLife").format(currentDate)
        log.info("||执行SQL：【{0}】".format(SQL))
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "该用户未到使用时间，如需提前请与我们联系", failure(self.fileName + "_003")
            Pass(self.fileName + "_003")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||=======================结束执行【用户未到使用期限】用例========================")

    # @pytest.mark.run(order=4)
    # @pytest.mark.flaky(2)
    def test_004(self):
        """ 未到有效期，暂不能登录 """
        print("\n")
        log.info("||=======================开始执行【账号未到使用期限】用例========================")
        currentDate = str(Time("DataFormat"))
        SQL = self.sqlConfig.get_value("SQL", "UserNotArriveServiceLife").format(currentDate)
        log.info("||执行SQL：【{0}】".format(SQL))
        isOK, phone = self.select.excel_sql(SQL, "single")
        if isOK:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "未到有效期，暂不能登录", failure(self.fileName + "_004")
            Pass(self.fileName + "_004")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||=======================结束执行【账号未到使用期限】用例========================")

    # @pytest.mark.run(order=5)
    # @pytest.mark.flaky(2)
    def test_005(self):
        """ 该用户已到期，如需续期请与我们联系 """
        print("\n")
        log.info("||==========================开始执行【用户已过期】用例==========================")
        currentDate = str(Time("LongDataFormat"))
        SQL = self.sqlConfig.get_value("SQL", "CustomerExpired").format(currentDate)
        log.info("||执行SQL：【{0}】".format(SQL))
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "该用户已到期，如需续期请与我们联系", failure(self.fileName + "_005")
            Pass(self.fileName + "_005")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||==========================开始执行【用户已过期】用例==========================")

    # @pytest.mark.run(order=6)
    # @pytest.mark.flaky(2)
    def test_006(self):
        """ 账号不存在 """
        print("\n")
        log.info("||==========================开始执行【账号不存在】用例==========================")
        SQL = self.sqlConfig.get_value("SQL", "UserNonexistence")
        log.info("||执行SQL：【{0}】".format(SQL))
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["customer_admin_phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "账号不存在", failure(self.fileName + "_006")
            Pass(self.fileName + "_006")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||==========================结束执行【账号不存在】用例==========================")

    # @pytest.mark.run(order=7)
    # @pytest.mark.flaky(2)
    def test_007(self):
        """账号不可用，请联系贵司用户管理员或我们处理"""
        print("\n")
        log.info("||==========================开始执行【账号不可用】用例==========================")
        SQL = self.sqlConfig.get_value("SQL", "UserUnavailable")
        log.info("||执行SQL：【{0}】".format(SQL))
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "账号不可用，请联系贵司用户管理员或我们处理", failure(self.fileName + "_007")
            Pass(self.fileName + "_007")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||==========================结束执行【账号不可用】用例==========================")

    # @pytest.mark.run(order=8)
    # @pytest.mark.flaky(2)
    def test_008(self):
        """ 账号审核中 """
        print("\n")
        log.info("||==========================开始执行【账号审核中】用例==========================")
        SQL = self.sqlConfig.get_value("SQL", "UserUnderReview")
        log.info("||执行SQL：【{0}】".format(SQL))
        isOk, phone = self.select.excel_sql(SQL, "single")
        if isOk:
            log.info("||从数据库中获取到的数据：【{0}】".format(phone))
            self.newDriver.input(LoginElement.phone_element, phone["phone"])
            self.newDriver.input(LoginElement.code_element, "1234")
            self.newDriver.click(LoginElement.login_button_element)
            cue = self.newDriver.getText(LoginElement.cue)
            assert cue == "账号审核中", failure(self.fileName + "_008")
            Pass(self.fileName + "_008")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(phone, SQL))
        log.info("||==========================结束执行【账号审核中】用例==========================")


if __name__ == "__main__":
    unittest.main()