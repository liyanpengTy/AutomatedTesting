# -*- coding: utf-8 -*-
# @File    :parseJson
# @Date    :2023/3/28 8:38
# @Name    :LYP

import json

""" JSON解析 """
def analyze_data(path, filename):
    with open(path + filename, "r", encoding="utf-8") as f:
        list_data = []
        dict_data = json.load(f)
        for value in dict_data.values():
            list_data.append(value)
        return list_data