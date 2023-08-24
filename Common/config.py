# -*- coding: utf-8 -*-
# @File    :config
# @Date    :2023/3/27 15:35
# @Name    :LYP

import os
from configparser import ConfigParser
from Common.initPath import config_dir

class Config(ConfigParser):
    """ 解析config.ini文件 """
    def __init__(self, config_file=config_dir, fileName='config.ini'):
        self.config_name = self._filePath(config_file, fileName)
        super(Config, self).__init__()
        super().read(self.config_name, encoding="utf-8")

    def _filePath(self, config_file, fileName):
        """

        :param config_file: 配置文件路径
        :param fileName: 配置文件名称
        :return:  配置文件路径 + 文件名称
        """
        config_path = os.path.join(config_file, fileName)
        return config_path

    def get_all_sections(self):
        """

        :return: 返回所有节点的名称
        """
        return super().sections()

    def get_options(self, sectioName):
        """

        :param sections: 节点名称
        :return: 返回所有节点的key
        """
        return super().options(sectioName)

    def get_items(self, sectionName):
        """

        :param sectionName: 节点名称
        :return: 返回节点的item
        """
        return super().items(sectionName)

    def get_value(self, sectioName, key):
        """

        :param sectioName: 节点名称
        :param key:  key的名称
        :return: 节点名称下的value
        """
        return super().get(sectioName, key)

    def save_data(self, sectioName, key, value):
        """
        向config.ini配置文件中增加配置
        :param sectioName: 节点名称
        :param key: 节点的key
        :param value: 节点key对应的value值
        :return:
        """
        super().set(section=sectioName, option=key, value=value)
        super().write(fp=open(self.config_name, "w"))

    def as_dict(self):
        d =dict(self._sections)
        for k in d:
            d[k] =dict(d[k])
        return d

    def get_all_config(self):
        """

        :return: 读取所有配置文件中的信息，以字典形式输出
        """
        _config = Config()
        result = {}
        if self.config_name:
            try:
                _config.read(self.config_name, encoding="utf-8")
                result = self.as_dict()
            except OSError:
                raise ValueError("Read config file failed: {0}".format(OSError))
        return result


# 调用其他方法获取数据
conf = Config()
# 直接获取字典类型的数据
config = conf.get_all_config()
# sectioNameList = conf.get_all_sections()
# print("所有节点的名称列表：【{0}】".format(sectioNameList))
# optionsList = conf.get_options(sectioNameList[1])
# print("节点：【{0}】，key列表：【{1}】".format(sectioNameList[1], optionsList))
# items = conf.get_items(sectioNameList[0])
# print("节点：【{0}】，item：【{1}】".format(sectioNameList[0], items))
# value = conf.get_value(sectioNameList[1], optionsList[1])
# print("节点：【{0}】，key：【{1}】，value的值：【{2}】".format(sectioNameList[1], optionsList[1], value))
# configList = conf.get_all_config()
# print("config.ini配置文件组成的字典：【{0}】".format(configList))