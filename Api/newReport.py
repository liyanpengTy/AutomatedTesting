# -*- coding: utf-8 -*-
# @File    :netReport
# @Date    :2023/4/19 11:25
# @Name    :LYP

import os

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new