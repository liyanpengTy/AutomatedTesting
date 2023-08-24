# -*- coding: utf-8 -*-
# @File    :operation_redis
# @Date    :2023/3/29 10:51
# @Name    :LYP
import redis
from Common.config import conf


def getConfig(sectioName):
    keyList = conf.get_options(sectioName)
    host = conf.get_value(sectioName, keyList[0])
    port = conf.get_value(sectioName, keyList[1])
    return host, port

class OperationRedis(object):
    """ redis操作 """

    def __init__(self, sectioName):
        self.pool = None
        self.redis = self.connect_redis(sectioName)

    def handleOver(self):
        self.pool.disconnect()
        self.redis.close()

    def connect_redis(self, sectioName):
        host, port = getConfig(sectioName)
        self.pool = redis.ConnectionPool(host=host, port=int(port), decode_responses=True)
        red = redis.Redis(connection_pool=self.pool)
        return red

    def set_redis(self, key):
        value = self.redis.get(str(key))
        value_num = self.redis.get(str(key)+"num")
        if str(value) != "1234":
            self.redis.set(key, "1234")
        if str(value_num) != "1":
            self.redis.set(key + "num", "1")

    def get_value(self, key):
        value = self.redis.get(key)
        return value


# phone = "18370601280"
# red = OperationRedis("redis")
# red.set_redis(phone)
# code = red.get_value(phone)
# code_num = red.get_value(phone + "num")
# print(code)
# print(code_num)