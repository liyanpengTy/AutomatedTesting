# -*- coding: utf-8 -*-
# @File    :rapidValuationPublic
# @Date    :2023/3/28 19:14
# @Name    :LYP

from Web.SystemOne.ModuleOne.ModuleSubdivisionOne.Page.rapidValuationElement import *

"""
"小区估价": {"area": "1", "orientation": "1", "room": "1", "hall": "1", "floor": "2", "MainFloor": "3", "buildAge": "1", "elevator": "4"},
"地址估价": {"area": "2", "orientation": "5", "room": "2", "hall": "2", "floor": "6", "MainFloor": "7", "buildAge": "2", "elevator": "8"},
"手动提交估价": {"area": "3", "orientation": "13", "room": "3", "hall": "3", "floor": "14", "MainFloor": "15", "buildAge": "3", "elevator": "16"}
"""

def GetHouseProperties(newDriver, areaNumber, orientationNumber, roomNumber, hallNumber, floorNumber, mainFloorNumner, buildAgeNumber, elevatorNumber):
    """
    获取房屋属性：面积、朝向、户型、楼层、总楼层、建成年代、有无电梯
    :return:
    """
    HousePropertiesKeyList = ["面积", "朝向", "户型", "楼层", "总楼层", "建成年代", "有无电梯"]
    HousePropertiesValueList = []
    area = newDriver.getText(element=inputBox("请输入面积", areaNumber), choose="value")
    HousePropertiesValueList.append(area + "㎡")
    orientation = newDriver.getText(element=inputBox("请选择", orientationNumber), choose="value")
    HousePropertiesValueList.append(orientation)
    room = newDriver.getText(element=inputBox("房", roomNumber), choose="value")
    hall = newDriver.getText(element=inputBox("厅", hallNumber), choose="value")
    # kitchen = newDriver.getText(element=inputBox(text="厨"), choose="value")
    # who = newDriver.getText(element=inputBox(text="卫"), choose="value")
    HousePropertiesValueList.append(room + hall)
    floor = newDriver.getText(element=inputBox("请选择", floorNumber), choose="value")
    HousePropertiesValueList.append(floor + "层")
    MainFloor = newDriver.getText(element=inputBox("请选择", mainFloorNumner), choose="value")
    HousePropertiesValueList.append(MainFloor + "层")
    buildAge = newDriver.getText(element=inputBox("选择年份", buildAgeNumber), choose="value")
    HousePropertiesValueList.append(buildAge)
    elevator = newDriver.getText(element=inputBox("请选择", elevatorNumber), choose="value")
    HousePropertiesValueList.append(elevator)
    HousePropertiesDict = {}
    for i in range(len(HousePropertiesKeyList)):
        if HousePropertiesValueList[i] == '':
          HousePropertiesDict[HousePropertiesKeyList[i]] = "--"
        else:
          HousePropertiesDict[HousePropertiesKeyList[i]] = HousePropertiesValueList[i]
    return HousePropertiesDict