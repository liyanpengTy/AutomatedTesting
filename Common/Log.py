# -*- coding: utf-8 -*-
# @File    :Log
# @Date    :2023/3/27 19:06
# @Name    :LYP

import os
import time
import logging
import colorlog
from Common.initPath import log_dir
from Common.config import config
from logging.handlers import TimedRotatingFileHandler

_log_format = config["log"]["log_format"]
_log_level = config["log"]["log_level"]

class LogInit:
    """ 封装日志模块 """
    def __init__(self):
        self._log_file = os.path.join(log_dir, '{0}.log'.format(time.strftime("%Y%m%d%H")))
        self.logger = logging.getLogger('main')
        self.logger.setLevel(_log_level)
        self.log_colors_config = {
            "DEBUG": "blue",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "cyan"
        }
        self.formatter = colorlog.ColoredFormatter(_log_format, log_colors=self.log_colors_config)

    def __console(self, level, message):
        """日志文件打印日志"""
        # when: 周(W), 天(D), 时(H), 分(M), 秒(S)
        # interval: 根据interval设置的值，在when个周期进行切割
        # backupCount: 保留文件的个数，超出删除最早的
        handler = TimedRotatingFileHandler(filename=self._log_file, when="D", backupCount=7, encoding='utf-8')
        # handler = logging.FileHandler(filename=self._log_file, mode='a', encoding='utf8')
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

        """ 终端打印日志 """
        console = logging.StreamHandler()
        console.setFormatter(self.formatter)
        self.logger.addHandler(console)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        self.logger.removeHandler(console)
        self.logger.removeHandler(handler)
        handler.close()

    def info(self, message):
        self.__console('info', message)

    def debug(self, message):
        self.__console('debug', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def critical(self, message):
        self.__console('critical', message)


log = LogInit()
# log.info('测试开始')
# log.error('测试体')
# log.warning('测试结束')
# log.debug('测试结束')
# log.critical('测试结束')

