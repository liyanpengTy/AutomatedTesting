# -*- coding: utf-8 -*-
# @File    :assertion
# @Date    :2023/3/28 16:00
# @Name    :LYP

from time import sleep
from Common.Log import log
from Common.getTime import Time
from Common.screenshot import screenshot

def Pass(title):
    sleep(0.5)
    return log.info("||【" + str(title) + "】测试通过。执行时间：【{0}】".format(Time("DataFormat")))

def failure(title):
    sleep(0.5)
    screenshot(title + "_测试失败", "失败")
    return log.error("||【" + str(title) + "】测试失败。执行时间：【{0}】".format(Time("DataFormat")))