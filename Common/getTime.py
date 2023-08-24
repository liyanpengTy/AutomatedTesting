# -*- coding: utf-8 -*-
# @File    :getTime
# @Date    :2023/3/27 19:04
# @Name    :LYP

import time
import datetime
from Common.Log import log


def Time(DataFormat):
    """
    :return: 按照对应格式，获取当前时间
    """
    newTime = None
    if DataFormat == "DataFormat":
        newTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    elif DataFormat == "LongDataFormat":
        newTime = time.strftime("%Y-%m-%d", time.localtime())
    elif DataFormat == "runDataFormat":
        newTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    else:
        log.warning("||请输入想要的日期格式：DataFormat or LongDataFormat")
    return newTime

def getTime():
    newTime = datetime.datetime.now()
    return newTime

def getDay():
    newTimeDay = time.strftime("%Y", time.localtime())
    return newTimeDay

def countdown(number):
    for i in range(0, number):
        log.info("||请等待{0}秒，加载页面".format(number-i))
        time.sleep(1)
