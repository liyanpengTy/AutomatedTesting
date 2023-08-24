# -*- coding: utf-8 -*-
# @File    :test_moduleSubdivisionOne
# @Date    :2023/4/11 18:06
# @Name    :LYP

import ddt
import warnings
import unittest
import requests
from Common.Log import log
from Api.newReport import new_report
from Common.getExcel import GetExcel
from Common.sendApirequest import Request
from Common.initPath import data_ModuleOne
from Common.initPath import html_report_dir


@ddt.ddt
class TestModuleSubdivisionOne(unittest.TestCase):
    # 因要回写表格，需将sheet_name=value带上
    getExcel = GetExcel(filePath=data_ModuleOne, sectioName="case", key="data_ModuleOne_api", sheet_name="Sheet1")
    testData = getExcel.read_all_excel()
    variable = {        # 存放变量数据
        "userId": None,
        "userCustomerId": None
    }
    parameter = {}      # 存放入参数据

    def setUp(self):
        self.send = requests.session()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        pass

    def setVariable(self, data, result):
        if data["getArray"] is None:
            if data["variableOne"] is not None:
                self.variable[data["variableOne"]] = result["data"][data["variableOne"]]
                log.info("||增加variable字典键值对：【{0}:{1}】".format(data["variableOne"], result["data"][data["variableOne"]]))
            if data["variableTwo"] is not None:
                self.variable[data["variableTwo"]] = result["data"][data["variableTwo"]]
                log.info("||增加variable字典键值对：【{0}:{1}】".format(data["variableTwo"], result["data"][data["variableTwo"]]))
            if data["variableThree"] is not None:
                self.variable[data["variableThree"]] = result["data"][data["variableThree"]]
                log.info("||增加variable字典键值对：【{0}:{1}】".format(data["variableThree"], result["data"][data["variableThree"]]))
        elif data["getArray"] == "data":
            self.variable[data["variableOne"]] = result["data"]
            log.info("||向variable字典增加键值对：【{0}:{1}】".format(self.variable[data["variableOne"]], result["data"]))

    def setParameter(self, data):
        self.parameter = {}     # 初始化入参数据
        if data["parameterOne"] is not None:
            self.parameter[data["parameterOne"]] = self.variable[data["parameterOne"]]
        if data["parameterTwo"] is not None:
            self.parameter[data["parameterTwo"]] = self.variable[data["parameterTwo"]]
        if data["parameterThree"] is not None:
            self.parameter[data["parameterThree"]] = self.variable[data["parameterThree"]]
        log.info("||创建parameter入参数据：{0}".format(self.parameter))

    @ddt.data(*testData)
    def test_login_api(self, data):
        rowNum = int(data["ID"].split("_")[1])
        log.info("||执行第【{0}】条数据，数据ID：【{1}】".format(rowNum, data["ID"]))
        parameterDict = {   # 存放特殊处理的数据 key:第几条，value：入参数据
                8:  {"id": self.variable["userId"]},
                10: {"id": self.variable["userId"]},
                11: {"origin": "1"},
                12: {"id": self.variable["userCustomerId"]}
            }
        if rowNum == 1:
            # 只适用登录接口
            self.re = Request(self.send, data)
            self.result = self.re.json()
            self.setVariable(data, self.result)
            self.variable["id"] = [self.result["data"]["userId"]]
        elif rowNum in parameterDict:  # 特殊处理
            log.info("||特殊处理第【{0}】条数据".format(rowNum))
            self.re = Request(self.send, data, self.variable["accessToken"], parameterDict[rowNum])
            self.result = self.re.json()
            if rowNum == 10:    # 增加variable变量数据
                self.setVariable(data, self.result)
        else:
            if data["ParticipationWay"] == 1:       # 请求头入参
                log.info("||第【{0}】条数据需要请求头入参".format(rowNum))
                if data["getVariable"] == 0:        # 不需要获取变量
                    log.info("||第【{0}】条数据不需要获取变量".format(rowNum))
                    if data["Input"] == 0:          # 不需要入参
                        log.info("||第【{0}】条数据不需要入参".format(rowNum))
                        self.re = Request(self.send, data, self.variable["accessToken"])
                        self.result = self.re.json()
                    elif data["Input"] == 1:     # 需要入参，从variable变量中取数
                        log.info("||第【{0}】条数据需要入参".format(rowNum))
                        self.setParameter(data)
                        self.re = Request(self.send, data, self.variable["accessToken"], self.parameter)
                        self.result = self.re.json()
                    elif data["Input"] == 2:     # 需要入参，入Excel中的数据
                        log.info("||第【{0}】条数据需要使用Excel中的入参数据".format(rowNum))
                        self.re = Request(self.send, data, self.variable["accessToken"])
                        self.result = self.re.json()
                elif data["getVariable"] == 1:      # 需要获取变量
                    log.info("||第【{0}】条数据需要获取变量".format(rowNum))
                    self.setParameter(data)
                    print(self.parameter)
                    self.re = Request(self.send, data, self.variable["accessToken"], self.parameter)
                    self.result = self.re.json()
                    self.setVariable(data, self.result)
            elif data["ParticipationWay"] == 2:     # 请求体入参 # 需完善，遇到其他方式时，再进行优化
                log.info("||第【{0}】条数据需要请求体入参".format(rowNum))
                self.re = Request(self.send, data, self.variable["accessToken"])
                self.result = self.re.json()
        readData_code = int(data["status_code"])
        readData_msg = data["msg"]
        if readData_code == self.result['code'] and readData_msg in self.re.text:
            OK_data = "PASS"
            self.getExcel.write_excel(rowNum + 1, 10, OK_data)
            log.info("||第【{0}】条数据执行结果：【{1}】".format(rowNum, OK_data))
        else:
            NOT_data = "FAIL"
            self.getExcel.write_excel(rowNum + 1, 10, NOT_data)
            log.info("||第【{0}】条数据执行结果：【{1}】".format(rowNum, NOT_data))
        self.assertEqual(self.result['code'], readData_code, "返回实际结果是->:{0}".format(self.result['code']))
        self.assertIn(readData_msg, self.re.text, "返回实际结果是->:{0}".format(self.result))


if __name__ == '__main__':
    unittest.main()
    # TestModuleSubdivisionOne().test_api()
