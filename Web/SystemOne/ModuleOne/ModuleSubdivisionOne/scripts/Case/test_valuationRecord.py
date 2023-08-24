# -*- coding: utf-8 -*-
# @File    :test_valuationRecord
# @Date    :2023/3/31 10:51
# @Name    :LYP

import os
import unittest
import pytest
from Common.Log import log
from Common.sendMsg import sendText
from Common.screenshot import screenshot
from Common.operation_db import OperationDB
from Common.config import Config
from Common.getTime import Time, getTime, getDay, countdown
from Common.initPath import testData_systemOne_login_dir, sqlConfig_systemOne_moduleOne_subdivisionOne_dir
from Web.Utils.driverUtils import DriverUtils
from Web.Public.pagingElement import *
from Web.Public.statementElement import *
from Web.Public.assertion import Pass, failure
from Web.Public.operationMethod import OperationMethod, getAttributes
from Web.SystemOne.menuElement import menu
from Web.SystemOne.LoginModule.scripts.Case.login import login, phone
from Web.SystemOne.ModuleOne.ModuleSubdivisionOne.Page.valuationRecordElement import *

class TestValuationRecord(unittest.TestCase):
    """ 房屋智能估价（单套） - 估价记录 """
    fileName = os.path.basename(__file__)
    startTime = getTime()
    recordStartTime = Time("DataFormat")
    select = OperationDB("test_db")
    sqlConfig = Config(config_file=sqlConfig_systemOne_moduleOne_subdivisionOne_dir, fileName="rapidValuationSqlConfig.ini")
    getUserID_SQL = sqlConfig.get_value("SQL", "UserId").format(phone)
    log.info("||执行SQL：【{0}】".format(getUserID_SQL))
    isOk, user_id = select.excel_sql(getUserID_SQL, "single")
    log.info("||执行SQL结果：【{0}】".format(user_id))

    @classmethod
    def setUpClass(cls) -> None:
        print("\n")
        log.info("||===================开始执行《房屋智能估价（单套）- 快速估价》页面测试用例===================")
        log.info("||开始时间：【{0}】".format(cls.recordStartTime))
        cls.driver = DriverUtils.getDriver()
        cls.newDriver = OperationMethod(cls.driver)
        login(cls.driver, cls.newDriver)
        OperationMethod.HoverElement(cls.driver, menu(level=1, choose=0, number=2), cls.newDriver)
        cls.newDriver.click(menu(level=2, choose=0, number=1))
        cls.newDriver.click(menu(level=3, choose=2, value="估价记录"))
        log.info("||进入【房屋智能估价（单套）- 估价记录】页面")

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        countdown(1)
        self.driver.refresh()
        print("\n")
        log.info("||==================================执行下一个测试用例==================================")

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quitDriver()
        EndTime = getTime()
        when = (EndTime - cls.startTime).total_seconds()
        print("\n")
        log.info("||==================================================================================")
        log.info("||开始时间: 【{0}】".format(cls.recordStartTime))
        log.info("||结束时间: 【{0}】".format(Time("DataFormat")))
        log.info("||共用时：【{0}】秒".format(when))
        log.info("||===================结束执行【房屋智能估价（单套）- 估价记录】页面测试用例===================")
        # sendText.send_text("《房屋智能估价（单套）- 估价记录》页面测试结束，请查看！！！")

    # @pytest.mark.run(order=12)
    # @pytest.mark.flaky(2)
    def test_001(self):
        """ 报表数据量是否正确 """
        print("\n")
        log.info("||==========================开始执行【报表数据量是否正确】用例============================")
        if self.isOk:
            SQL = self.sqlConfig.get_value("SQL", "CountReportDataVolume").format(self.user_id["id"])
            log.info("||SQL：【{0}】".format(SQL))
            isOks, count = self.select.excel_sql(SQL, "single")
            if isOks:
                log.info("||执行SQL结果：【{0}】".format(count))
                countdown(5)
                numberPageList = self.newDriver.find_els(numberPages())
                log.info("||翻页控件页码显示的长度：【{0}】".format(len(numberPageList)))
                self.newDriver.click(selectPageNumber(len(numberPageList)))
                countdown(5)
                columnList = self.newDriver.find_els(columnData(1))
                serialNumberMax = int(self.newDriver.getText(preciseData(len(columnList), 1)))
                log.info("||列表中的最大序号：【{0}】".format(serialNumberMax))
                assert count["合计"] == serialNumberMax, failure(self.fileName + "-001")
                Pass(self.fileName + "-001")
            else:
                log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(count, SQL))
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(self.user_id, self.getUserID_SQL))
        log.info("||==========================结束执行【报表数据量是否正确】用例============================")

    # @pytest.mark.run(order=12)
    # @pytest.mark.flaky(2)
    def test_002(self):
        """ 根据城市筛选条件使用查询功能，查看结果集是否正确 """
        print("\n")
        log.info("||=============开始执行【根据城市筛选条件使用查询功能，查看结果集是否正确】用例================")
        if self.isOk:
            self.newDriver.click(screeningCondition(1))
            log.info("||点击城市筛选条件，展开下拉列表")
            cityList = self.newDriver.find_els(cityValuesList())
            self.newDriver.click(screeningCondition(1))
            log.info("||点击城市筛选条件，收起下拉列表")
            for i in range(len(cityList)):
                # 排除查询全部城市的场景
                if i != 0:
                    city = getAttributes(cityList, i)
                    self.newDriver.click(screeningCondition(1))
                    log.info("||点击城市筛选条件，展开下拉列表")
                    countdown(5)
                    self.newDriver.click(numberValuesList(i+1))
                    log.info("||点击的城市名称：【{0}】".format(city))
                    self.newDriver.click(queryButton())
                    log.info("||点击【查询】按钮")
                    countdown(5)
                    numberPageList = self.newDriver.find_els(numberPages())
                    log.info("||翻页控件页码显示的长度：【{0}】".format(len(numberPageList)))
                    self.newDriver.click(selectPageNumber(len(numberPageList)))
                    log.info("||点击翻页到最后一页")
                    countdown(5)
                    columnList = self.newDriver.find_els(columnData(1))
                    serialNumberMax = int(self.newDriver.getText(preciseData(len(columnList), 1)))
                    log.info("||列表中的最大序号：【{0}】".format(serialNumberMax))
                    getCityCodeOld_SQL = self.sqlConfig.get_value("SQL", "CityCode").format(city)
                    log.info("||执行SQL：【{0}】".format(getCityCodeOld_SQL))
                    isOk, cityCode = self.select.excel_sql(getCityCodeOld_SQL, "single")
                    log.info("||执行SQL结果：【{0}】".format(cityCode))
                    if isOk:
                        if i == 1:
                            SQL = self.sqlConfig.get_value("SQL", "ValuationHistory").format(self.user_id["id"])
                        else:
                            SQL = self.sqlConfig.get_value("SQL", "ValuationHistoryOld").format(self.user_id["id"], cityCode["city_code"])
                        log.info("||执行SQL：【{0}】".format(SQL))
                        isOks, count = self.select.excel_sql(SQL, "single")
                        log.info("||执行SQL的结果：【{0}】".format(count))
                        if isOks:
                            assert count["合计"] == serialNumberMax, failure(self.fileName + "-002")
                        else:
                            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(count, SQL))
                    else:
                        log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(cityCode, getCityCodeOld_SQL))
            Pass(self.fileName + "-002")
        else:
            log.error("||【{0}】，请检查SQL：【{1}】并确定数据库中是否有此类数据".format(self.user_id, self.getUserID_SQL))
        log.info("||=============结束执行【根据城市筛选条件使用查询功能，查看结果集是否正确】用例================")


if __name__ == '__main__':
    unittest.main()