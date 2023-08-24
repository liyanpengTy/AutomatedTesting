# -*- coding: utf-8 -*-
# @File    :run_api
# @Date    :2023/4/19 11:40
# @Name    :LYP

import os
import unittest
from Common.getTime import Time
from Common.initPath import html_report_dir
from Common.initPath import run_ModuleOneCase
from Common.HTMLTestRunner import HTMLTestRunner
from Api.newReport import new_report


def add_case(test_path=run_ModuleOneCase):
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover


def run_case(all_case, result_path=html_report_dir):
    now = Time("runDataFormat")
    fileName = result_path + "\\" + now + ".html"
    fp = open(fileName, "wb")
    runner = HTMLTestRunner(
        stream=fp,
        title="API接口测试报告",
        description="环境：windows 10， 浏览器： chrome"
    )
    runner.run(all_case)
    fp.close()
    new_report(html_report_dir)


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
