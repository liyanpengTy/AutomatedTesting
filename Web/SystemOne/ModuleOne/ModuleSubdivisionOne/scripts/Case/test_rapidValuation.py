# -*- coding: utf-8 -*-
# @File    :test_rapidValuation
# @Date    :2023/3/28 17:19
# @Name    :LYP


import os
import re
import math
import unittest
import pytest
from Common.Log import log
from Common.sendMsg import sendText
from Common.getExcel import GetExcel
from Common.screenshot import screenshot
from Common.getTime import getTime, Time, countdown, getDay
from Common.initPath import testData_systemOne_moduleOne_subdivisionOne_dir
from Web.Utils.driverUtils import DriverUtils
from Web.Public.assertion import Pass, failure
from Web.Public.operationMethod import OperationMethod, getAttributes
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待模块
from selenium.webdriver.support import expected_conditions  # 显示等待条件
from Web.SystemOne.menuElement import menu
from Web.SystemOne.LoginModule.scripts.Case.login import login
from Web.SystemOne.ModuleOne.ModuleSubdivisionOne.Page.rapidValuationElement import *
from Web.SystemOne.ModuleOne.ModuleSubdivisionOne.Page.appraisalResultElement import *
from Web.SystemOne.ModuleOne.ModuleOnePublic.rapidValuationPublic import GetHouseProperties


class TestRapidValuation(unittest.TestCase):
    """ 房屋智能估价（单套） - 快速估价 """
    fileName = os.path.basename(__file__)
    startTime = getTime()
    recordStartTime = Time("DataFormat")
    getExcel = GetExcel(filePath=testData_systemOne_moduleOne_subdivisionOne_dir, sectioName="case", key="testData_systemOne_moduleOne_subdivisionOne")
    print("\n")
    log.info("||======================================测试数据======================================")
    rapidValuationData = getExcel.get_sheet()
    log.info("||{0}".format(rapidValuationData))
    log.info("||======================================测试数据======================================")
    log.info("||======================================验证数据======================================")
    rapidValuationMsgData = getExcel.get_sheet(sheet_name="Sheet2")
    log.info("||{0}".format(rapidValuationMsgData))
    log.info("||======================================验证数据======================================")

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
        log.info("||进入【房屋智能估价（单套）- 快速估价】页面")

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
        log.info("||===================结束执行【房屋智能估价（单套）- 快速估价】页面测试用例===================")
        # sendText.send_text("《房屋智能估价（单套）- 快速估价》页面测试结束，请查看！！！")

    # @pytest.mark.run(order=9)
    # @pytest.mark.flaky(2)
    def test_001(self):
        """ 测试已上线城市是否正确 """
        print("\n")
        log.info("||==========================开始执行【测试已上线城市是否正确】用例==========================")
        self.newDriver.click(cityBox(1))
        log.info("||点击城市选择框")
        cityLists = self.newDriver.find_els(cityList(attribute="page"))
        if not cityLists:
            log.error("||快速估价页面，城市下拉框列表没有值。执行时间：【{0}】".format(Time("DataFormat")))
            screenshot("城市下拉框", self.fileName + "-001")
        else:
            for i in range(len(cityLists)):
                cityName = getAttributes(List=cityLists, number=i)
                log.info("||第【{0}】个上线的城市：【{1}】".format(i + 1, cityName))
                cityNameMsg = self.rapidValuationMsgData[i]["cityMsg"]
                log.info("||第【{0}】个上线城市对比对象：【{1}】".format(i + 1, cityNameMsg))
                assert cityName == cityNameMsg, failure(self.fileName + "-001")
            Pass(self.fileName + "001")
            screenshot("城市下拉框", self.fileName + "-001")
        log.info("||==========================结束执行【测试已上线城市是否正确】用例==========================")

    # @pytest.mark.run(order=10)
    # @pytest.mark.flaky(2)
    def test_002(self):
        """ 小区估价 """
        print("\n")
        log.info("||===============================开始执行【小区估价】用例================================")
        # 循环测试执行的次数
        for i in range(len(self.rapidValuationData)):
            city = self.rapidValuationData[i]["city"]
            self.newDriver.click(cityBox(number=1))
            log.info("||点击城市选择框")
            if city == "广州市":
                self.newDriver.click(cityList(attribute="page", choose=1, number=1))
            elif city == "佛山市":
                self.newDriver.click(cityList(attribute="page", choose=1, number=2))
            elif city == "东莞市":
                self.newDriver.click(cityList(attribute="page", choose=1, number=3))
            else:
                log.warning("||【{0}】未开放".format(city))
            cityName = self.newDriver.getText(cityBox(number=1))
            log.info("||获取城市名：【{0}】".format(cityName))
            self.newDriver.input(inputBox("请输入小区名称"), self.rapidValuationData[i]["xqName"])
            log.info("||在小区名称输入框中输入：【{0}】".format(self.rapidValuationData[i]["xqName"]))
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(expected_conditions.presence_of_element_located(communityDropList(choose=1, number=1)))
            countdown(3)
            screenshot(self.rapidValuationData[i]["city"] + "_小区名称下拉列表", self.fileName + "-002")
            self.newDriver.click(communityDropList(choose=1, number=1))
            community = self.newDriver.getText(inputBox("请输入小区名称"), choose="value")
            log.info("||点击小区下拉列表第一个搜索结果：【{0}】".format(community))
            self.newDriver.click(inputBox("请输入小区名称"))
            countdown(1)
            district = self.newDriver.find_el(communityDropList()).get_attribute("textContent").split("-")[-1]
            log.info("||获取行政区：【{0}】".format(district))
            self.newDriver.click(communityDropList(choose=1, number=1))
            communityDistrict_A = community + " " + district
            log.info("||小区估价页的小区名称和行政区：【{0}】".format(communityDistrict_A))
            countdown(1)
            self.newDriver.click(inputBox("请选择或输入楼栋号"))
            log.info("||点击楼栋号输入下拉框")
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located(BuildingNumberDropList(choose=1, number=1)))
            countdown(1)
            self.newDriver.click(BuildingNumberDropList(choose=1, number=1))
            building = self.newDriver.getText(inputBox("请选择或输入楼栋号"), choose="value")
            log.info("||点击楼栋下拉列表第一个搜索结果：【{0}】".format(building))
            countdown(1)
            self.newDriver.click(inputBox("请选择或输入房号"))
            log.info("||点击房号输入下拉框")
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(expected_conditions.presence_of_element_located(BuildingNumberDropList(choose=1, number=1)))
            countdown(1)
            self.newDriver.click(BuildingNumberDropList(choose=1, number=1))
            roomNumber = self.newDriver.getText(inputBox("请选择或输入房号"), choose="value")
            log.info("||点击房号下拉列表第一个搜索结果：【{0}】".format(roomNumber))
            # 根据输入框判断：选择的房号对应的面积在系统内是否有值
            state = self.newDriver.isElementExist(whetherDisabled("请输入面积"))
            if not state:
                self.newDriver.input(inputBox("请输入面积"), 100)
            area = self.newDriver.getText(element=inputBox(text="请输入面积"), choose="value")
            self.newDriver.click(more(1))
            log.info("||点击【更多>>】")
            screenshot(community + "_小区估价页", self.fileName + "-002")
            appraisalObject_A = ""
            # 只有广州市的估价对象需要拼接城市+行政区+小区名称+楼栋号+房号
            if city == "广州市":
                appraisalObject_A = cityName + district + community + building + roomNumber
                log.info("||估价对象：【{0}】".format(appraisalObject_A))
            getHouseProperties_A = GetHouseProperties(self.newDriver, areaNumber=1, orientationNumber=1, roomNumber=1, hallNumber=1, floorNumber=2, mainFloorNumner=3, buildAgeNumber=1, elevatorNumber=4)
            log.info("||将房屋属性写入列表：【{0}】".format(getHouseProperties_A))
            self.newDriver.click(protocol(1))
            log.info("||勾选用户协议")
            self.newDriver.click(PresentValuationButton(1))
            log.info("||点击现在估价按钮")
            countdown(5)
            if city == "广州市":
                appraisalObject_B = self.newDriver.getText(AppraisalObject(number=1))
                log.info("||估价结果页的估价对象：【{0}】".format(appraisalObject_B))
                assert appraisalObject_A == appraisalObject_B, failure(self.fileName + "-002")
            communityDistrict_B = self.newDriver.getText(CommunityDistrict(number=1))
            log.info("||估价结果页的小区名称和行政区：【{0}】".format(communityDistrict_B))
            assert communityDistrict_A == communityDistrict_B, failure(self.fileName + "-002")
            valuationTime_A = "估价时间：" + Time("LongDataFormat")
            log.info("||当前时间的年月日：【{0}】".format(valuationTime_A))
            valuationTime_B = self.newDriver.getText(ValuationTime(number=1))
            log.info("||估价结果页的年月日：【{0}】".format(valuationTime_B))
            assert valuationTime_A == valuationTime_B, failure(self.fileName + "-002")
            # 判断出值结果
            for k in range(4):
                State = self.newDriver.isElementExist(AppraisalResult(choose=k, number=1))
                if State:
                    if k == 0:
                        log.info("||城市：【{0}】，小区名称：【{1}】，楼栋：【{2}】，房号：【{3}】， 面积：【{4}】的估价结果为【直接出值】".format(cityName, community, building, roomNumber, area))
                        break
                    elif k == 1:
                        log.info("||城市：【{0}】，小区名称：【{1}】，楼栋：【{2}】，房号：【{3}】， 面积：【{4}】的估价结果为【参考价】".format(cityName, community, building, roomNumber, area))
                        break
                    elif k == 2:
                        log.info("||城市：【{0}】，小区名称：【{1}】，楼栋：【{2}】，房号：【{3}】， 面积：【{4}】的估价结果为【正估价中】".format(cityName, community, building, roomNumber, area))
                        break
                    elif k == 3:
                        log.info("||城市：【{0}】，小区名称：【{1}】，楼栋：【{2}】，房号：【{3}】， 面积：【{4}】的估价结果为【暂无法估价】".format(cityName, community, building, roomNumber, area))
                        break
            housePropertiesKeyList = ["面积", "建成年代", "物业类型", "楼层", "总楼层", "户型", "有无电梯", "朝向"]
            getHouseProperties_B = {}
            for k in range(len(housePropertiesKeyList)):
                if k == 2:
                    # 物业类型固定为住宅，排除其他的值。
                    getHouseProperties_B[housePropertiesKeyList[k]] = "住宅"
                    continue
                else:
                    getHouseProperties_B[housePropertiesKeyList[k]] = self.newDriver.getText(HouseProperties(k + 1))
            log.info("||估价结果页的房屋属性：【{0}】".format(getHouseProperties_B))
            # 对比两个字典
            contrastList = [(G, getHouseProperties_A[G], getHouseProperties_B[G]) for G in getHouseProperties_A if getHouseProperties_A[G] != getHouseProperties_B[G]]
            if len(contrastList) != 0:
                assert False, failure(self.fileName + "-002")
            screenshot(community + "_估价结果页", self.fileName + "-002")
            self.newDriver.click(menu(level=3, choose=2, value="快速估价"))
        Pass(self.fileName + "-002")
        log.info("||===============================结束执行【小区估价】用例================================")

    # @pytest.mark.run(order=11)
    # @pytest.mark.flaky(2)
    def test_003(self):
        """ 手动提交估价 """
        print("\n")
        log.info("||==============================开始执行【手动提交估价】用例===============================")
        self.newDriver.click(cityBox(1))
        cityLists = self.newDriver.find_els(cityList(attribute="page"))
        self.newDriver.click(cityBox(1))
        for i in range(len(cityLists)):
            self.newDriver.click(cityBox(1))
            self.newDriver.click(cityList(attribute="page", choose=1, number=i + 1))
            cityName = self.newDriver.getText(cityBox(number=1))
            log.info("||点击选中：【{0}】".format(cityName))
            self.newDriver.input(inputBox("请输入小区名称"), "cs")
            self.newDriver.click(communityDropList(choose=2, number=1))
            countdown(1)
            screenshot(self.rapidValuationData[i]["city"] + "_打开手动提交弹框", self.fileName + "_003")
            cityNames = self.newDriver.getText(cityBox(number=2))
            log.info("||弹框选中的城市：【{0}】".format(cityNames))
            assert cityName == cityNames, failure(self.fileName + "_003")
            self.newDriver.input(inputBox("请输入", 1), self.rapidValuationData[i]["address"])
            log.info("||在小区名称输入框中输入：【{0}】".format(self.rapidValuationData[i]["address"]))
            self.newDriver.input(inputBox("输入详细证载/房屋地址（包括楼栋、房号）"), self.rapidValuationData[i]["address"])
            log.info("||在地址输入框中输入：【{0}】".format(self.rapidValuationData[i]["address"]))
            self.newDriver.click(more(3))
            log.info("||点击【更多>>】")
            countdown(3)
            state = self.newDriver.isElementExist(whetherDisabled("请输入面积"))
            if not state:
                self.newDriver.input(inputBox("请输入面积", number=3), context="100")
            countdown(1)
            orientation = self.newDriver.getText(inputBox("请选择", 13), "value")
            if orientation == "":
                self.newDriver.click(inputBox("请选择", number=13))
                log.info("||点击【朝向】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            room = self.newDriver.getText(inputBox("房", 3), "value")
            if room == "":
                self.newDriver.click(inputBox("房", number=3))
                log.info("||点击【房屋户型-房】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            hall = self.newDriver.getText(inputBox("厅", 3), "value")
            if hall == "":
                self.newDriver.click(inputBox("厅", number=3))
                log.info("||点击【房屋户型-厅】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            kitchen = self.newDriver.getText(inputBox("厨", 3), "value")
            if kitchen == "":
                self.newDriver.click(inputBox("厨", number=3))
                log.info("||点击【房屋户型-厨】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            who = self.newDriver.getText(inputBox("卫", 3), "value")
            if who == "":
                self.newDriver.click(inputBox("卫", number=3))
                log.info("||点击【房屋户型-卫】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            floor = self.newDriver.getText(inputBox("请选择", 14), "value")
            if floor == "":
                self.newDriver.click(inputBox("请选择", number=14))
                log.info("||点击【楼层】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            mainFloor = self.newDriver.getText(inputBox("请选择", 15), "value")
            if mainFloor == "":
                self.newDriver.click(inputBox("请选择", number=15))
                log.info("||点击【总楼层】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            buildAge = self.newDriver.getText(inputBox("选择年份", 3), "value")
            if buildAge == "":
                self.newDriver.click(inputBox("选择年份", number=3))
                log.info("||点击【建成年代】选择框")
                number = int(self.rapidValuationData[i]["days"])
                if number <= int(getDay()):
                    days = self.newDriver.find_el(selectionDays("年份区间")).get_attribute("textContent")
                    dayList = re.findall("\\d+", days)
                    if int(dayList[1]) >= number >= int(dayList[0]):
                        countdown(1)
                        self.newDriver.click(selectionDays("选择年份", number=number))
                    elif number <= int(dayList[0]):
                        frequency = math.ceil((int(dayList[0]) - number) / 10)
                        for fq in range(frequency):
                            self.newDriver.click(selectionDays("前一年"))
                        countdown(1)
                        self.newDriver.click(selectionDays("选择年份", number=number))
                else:
                    log.error("||要选择的建成年代大于当前的年份")
            elevator = self.newDriver.getText(inputBox("请选择", 16), "value")
            if elevator == "":
                self.newDriver.click(inputBox("请选择", number=16))
                log.info("||点击【有无电梯】选择框")
                self.newDriver.click(dropDownList(1))
                countdown(1)
            screenshot(self.rapidValuationData[i]["city"] + "_手动提交估价", self.fileName + "_003")
            getHouseProperties_A = GetHouseProperties(self.newDriver, areaNumber=3, orientationNumber=13, roomNumber=3, hallNumber=3, floorNumber=14, mainFloorNumner=15,  buildAgeNumber=3, elevatorNumber=16)
            log.info("||将房屋属性写入列表：【{0}】".format(getHouseProperties_A))
            self.newDriver.click(PresentValuationButton(3))
            log.info("||点击【现在估价】按钮")
            countdown(5)
            screenshot(self.rapidValuationData[i]["city"] + "_估价结果页", self.fileName + "_003")
            appraisalObject = self.newDriver.getText(AppraisalObject(number=1))
            log.info("||估价对象：【{0}】".format(appraisalObject))
            assert appraisalObject == self.rapidValuationData[i]["address"], failure(self.fileName + "_003")
            communityDistrict = self.newDriver.getText(CommunityDistrict(number=1))
            log.info("||小区名称：【{0}】".format(communityDistrict))
            assert communityDistrict == self.rapidValuationData[i]["address"], failure(self.fileName + "_003")
            valuationTime_A = "估价时间：" + Time("LongDataFormat")
            log.info("||当前时间的年月日：【{0}】".format(valuationTime_A))
            valuationTime_B = self.newDriver.getText(ValuationTime(number=1))
            log.info("||估价结果页的年月日：【{0}】".format(valuationTime_B))
            assert valuationTime_A == valuationTime_B, failure(self.fileName + "_003")
            housePropertiesKeyList = ["面积", "建成年代", "物业类型", "楼层", "总楼层", "户型", "有无电梯", "朝向"]
            getHouseProperties_B = {}
            for k in range(len(housePropertiesKeyList)):
                if k == 2:
                    # 物业类型固定为住宅，排除其他的值。
                    getHouseProperties_B[housePropertiesKeyList[k]] = "--"
                    continue
                else:
                    getHouseProperties_B[housePropertiesKeyList[k]] = self.newDriver.getText(HouseProperties(k + 1))
            log.info("||估价结果页的房屋属性：【{0}】".format(getHouseProperties_B))
            # 对比两个字典
            contrastList = [(G, getHouseProperties_A[G], getHouseProperties_B[G]) for G in getHouseProperties_A if getHouseProperties_A[G] != getHouseProperties_B[G]]
            if len(contrastList) != 0:
                assert False, failure(self.fileName + "_003")
            self.newDriver.click(menu(level=3, choose=2, value="快速估价"))
        Pass(self.fileName + "-003")
        log.info("||==============================结束执行【手动提交估价】用例===============================")


if __name__ == '__main__':
    unittest.main()