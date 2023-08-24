# -*- coding: utf-8 -*-
# @File    :initPath
# @Date    :2023/3/24 18:29
# @Name    :LYP


import os

_BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
common_dir = os.path.join(_BASEDIR, "Common")
config_dir = os.path.join(_BASEDIR, "Config")
# html测试报告存放路径
html_report_dir = os.path.join(_BASEDIR, "report", "api")
_log_dir = os.path.join(_BASEDIR, "Log")
# 日志存放路径
log_dir = os.path.join(_log_dir, "Log")
# 截图位置存放路径
screen_dir = os.path.join(_log_dir, "Screen")
# API的路径
_Api_dir = os.path.join(_BASEDIR, "Api")
run_ModuleOneCase = os.path.join(_Api_dir, "ModuleOne", "Case")
data_ModuleOne = os.path.join(_Api_dir, "ModuleOne", "Data")
run_ModuleTwoCase = os.path.join(_Api_dir, "ModuleTwo", "Case")
data_ModuleTwo = os.path.join(_Api_dir, "ModuleTwo", "Data")
# Web的路径
_web_dir = os.path.join(_BASEDIR, "Web")
# 系统一的路径
_systemOne_dir = os.path.join(_web_dir, "SystemOne")
# 系统一登录模块的路径
_login_systemOne_dir = os.path.join(_systemOne_dir, "LoginModule")
testData_systemOne_login_dir = os.path.join(_login_systemOne_dir, "scripts", "TestData")
sqlConfig_systemOne_login_dir = os.path.join(_login_systemOne_dir, "config")
# 模块一的路径
_systemOne_moduleOne_dir = os.path.join(_systemOne_dir, "ModuleOne")
# 模块细分一的路径
_systemOne_moduleOne_subdivisionOne_dir = os.path.join(_systemOne_moduleOne_dir, "ModuleSubdivisionOne")
testData_systemOne_moduleOne_subdivisionOne_dir = os.path.join(_systemOne_moduleOne_subdivisionOne_dir, "scripts", "TestData")
sqlConfig_systemOne_moduleOne_subdivisionOne_dir = os.path.join(_systemOne_moduleOne_subdivisionOne_dir, "config")
# 模块细分二的路径
_systemOne_moduleOne_subdivisionTwo_dir = os.path.join(_systemOne_moduleOne_dir, "ModuleSubdivisionTwo")
testData_systemOne_moduleOne_subdivisionTwo_dir = os.path.join(_systemOne_moduleOne_subdivisionTwo_dir, "scripts", "TestData")
# 模块二的路径
_systemOne_moduleTwo_dir = os.path.join(_systemOne_dir, "ModuleTwo")
# 模块细分一的路径
_systemOne_moduleTwo_subdivisionOne_dir = os.path.join(_systemOne_moduleTwo_dir, "ModuleSubdivisionOne")
testData_systemOne_moduleTwo_subdivisionOne_dir = os.path.join(_systemOne_moduleTwo_subdivisionOne_dir, "scripts", "TestData")
# 模块细分二的路径
_systemOne_moduleTwo_subdivisionTwo_dir = os.path.join(_systemOne_moduleTwo_dir, "ModuleSubdivisionTwo")
testData_systemOne_moduleTwo_subdivisionTwo_dir = os.path.join(_systemOne_moduleTwo_subdivisionTwo_dir, "scripts", "TestData")
# 系统二的路径
_systemTwo_dir = os.path.join(_web_dir, "SystemTwo")
# 系统二登录模块的路径
_login_systemTwo_dir = os.path.join(_systemTwo_dir, "LoginModule")
testData_systemTwo_login_dir = os.path.join(_login_systemTwo_dir, "scripts", "TestData")
# 模块一的路径
_systemTwo_moduleOne_dir = os.path.join(_systemTwo_dir, "ModuleOne")
# 模块细分一的路径
_systemTwo_moduleOne_subdivisionOne_dir = os.path.join(_systemTwo_moduleOne_dir, "ModuleSubdivisionOne")
testData_systemTwo_moduleOne_subdivisionOne_dir = os.path.join(_systemTwo_moduleOne_subdivisionOne_dir, "scripts", "TestData")
# 模块细分二的路径
_systemTwo_moduleOne_subdivisionTwo_dir = os.path.join(_systemTwo_moduleOne_dir, "ModuleSubdivisionTwo")
testData_systemTwo_moduleOne_subdivisionTwo_dir = os.path.join(_systemTwo_moduleOne_subdivisionTwo_dir, "scripts", "TestData")
# 模块二的路径
_systemTwo_moduleTwo_dir = os.path.join(_systemTwo_dir, "ModuleTwo")
# 模块细分一的路径
_systemTwo_moduleTwo_subdivisionOne_dir = os.path.join(_systemTwo_moduleTwo_dir, "ModuleSubdivisionOne")
testData_systemTwo_moduleTwo_subdivisionOne_dir = os.path.join(_systemTwo_moduleTwo_subdivisionOne_dir, "scripts", "TestData")
# 模块细分二的路径
_systemTwo_moduleTwo_subdivisionTwo_dir = os.path.join(_systemTwo_moduleTwo_dir, "ModuleSubdivisionTwo")
testData_systemTwo_moduleTwo_subdivisionTwo_dir = os.path.join(_systemTwo_moduleTwo_subdivisionTwo_dir, "scripts", "TestData")


# print("Common路径：" + common_dir)
# print("Config路径：" + config_dir)
# print("日志存放路径：" + log_dir)
# print("截图存放路径：" + screen_dir)
# print("系统一，登录数据文件路径：" + testData_systemOne_login_dir)
# print("系统一，模块一，模块细分一数据文件路径：" + testData_systemOne_moduleOne_subdivisionOne_dir)
# print("系统一，模块一，模块细分二数据文件路径：" + testData_systemOne_moduleOne_subdivisionTwo_dir)
# print("系统一，模块二，模块细分一数据文件路径：" + testData_systemOne_moduleTwo_subdivisionOne_dir)
# print("系统一，模块二，模块细分二数据文件路径：" + testData_systemOne_moduleTwo_subdivisionTwo_dir)
# print("系统一，登录数据文件路径：" + testData_systemTwo_login_dir)
# print("系统二，模块一，模块细分一数据文件路径：" + testData_systemTwo_moduleOne_subdivisionOne_dir)
# print("系统二，模块一，模块细分二数据文件路径：" + testData_systemTwo_moduleOne_subdivisionTwo_dir)
# print("系统二，模块二，模块细分一数据文件路径：" + testData_systemTwo_moduleTwo_subdivisionOne_dir)
# print("系统二，模块二，模块细分二数据文件路径：" + testData_systemTwo_moduleTwo_subdivisionTwo_dir)