# -*- coding: utf-8 -*-
# @File    :sendApirequest
# @Date    :2023/4/11 17:13
# @Name    :LYP

import json
import ast
import requests
from Common.Log import log
from Common.getExcel import GetExcel
from Common.initPath import data_ModuleOne

def headers(accessToken=None):
    if accessToken is None:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        }
    else:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Authorization": "Bearer {0}".format(accessToken)
        }
    return header

def Request(send, Data, accessToken=None, par=None):
    try:
        ret = None
        Method = Data["method"]
        Url = Data["url"]
        if Data["Parameter"] is None:
            parameter = None
        else:
            parameter = ast.literal_eval(Data["Parameter"])
        if Data["ParticipationWay"] == 1:
            if Data["Input"] == 0:
                ret = send.request(method=Method, url=Url, headers=headers(accessToken))
            elif Data["Input"] == 1:
                ret = send.request(method=Method, url=Url, headers=headers(accessToken), params=par)
            elif Data["Input"] == 2:
                ret = send.request(method=Method, url=Url, headers=headers(accessToken), params=parameter)
        else:
            ret = send.request(method=Method, url=Url, headers=headers(accessToken), json=parameter)
        return ret
    except Exception as e:
        log.error(e)