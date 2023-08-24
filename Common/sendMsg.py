# -*- coding: utf-8 -*-
# @File    :sendMsg
# @Date    :2023/3/28 8:43
# @Name    :LYP

import json
import requests
from Common.config import conf


class SendRobot:
    """企业微信-群聊机器人"""
    def __init__(self):
        self.webhook = conf.get_value("wechat", "apiRobot")
        self.header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

    def send_text(self, content, mentioned_list=None, mentioned_mobile_list=None):
        """ 发送文本消息 """
        data = {

            "msgtype": "text",
            "text": {
                "content": content
                , "mentioned_list": mentioned_list
                , "mentioned_mobile_list": mentioned_mobile_list
            }
        }
        data = json.dumps(data)
        requests.post(url=self.webhook, data=data, headers=self.header)

    # 发送markdown消息
    def send_md(self, content):
        """ 发送markdown消息 """
        data = {

            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        data = json.dumps(data)
        requests.post(url=self.webhook, data=data, headers=self.header)

class SendMsg(object):
    """
    企业微信-应用级别;
    需配置企业级别的相关企业微信参数，否则不可用
    """
    def __init__(self):
        """企业微信参数"""
        self.token = None
        self.corpid = conf.get_value("wechat", "corpid")
        self.corpsecret = conf.get_value("wechat", "corpsecret")
        self.agentid = conf.get_value("wechat", "agentid")

    def getToken(self):
        if self.corpid is None or self.corpsecret is None:
            return False, '企业微信相关信息未配置'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self.corpid + '&corpsecret=' + self.corpsecret
        response = requests.get(url)
        res = response.json()
        self.token = res['access_token']
        print(self.token)
        return True, '企业微信token获取成功'

    def sendMsg(self, msg):
        _isOK, result = self.getToken()
        if _isOK:
            url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.token
            jsonmsg = {
                "touser": "@all",
                "msgtype": "text",
                "agentid": self.agentid,
                "text": {
                    "content": msg
                },
                "safe": 0
            }
            data = (bytes(json.dumps(jsonmsg), 'utf-8'))
            requests.post(url, data, verify=False)
        else:
            print(result)


sendText = SendRobot()
# sendText.send_text(content='我就试一下')
# sendText.send_md(content='# 发个消息@裕彤 \n 我就试一下,发现更多精彩👍')