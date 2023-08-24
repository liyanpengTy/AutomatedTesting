# -*- coding: utf-8 -*-
# @File    :operationMethod
# @Date    :2023/3/28 16:06
# @Name    :LYP

from Common.Log import log
from selenium.webdriver.common.action_chains import ActionChains


def getAttributes(List, number):
    # 批量获取文本
    return List[number].get_attribute("textContent").split()[0]


class OperationMethod:
    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)

    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    def input(self, element, context):
        return self.find_el(element).send_keys(context)

    def click(self, element):
        return self.find_el(element).click()

    def clear(self, element):
        return self.find_el(element).clear

    def getUrl(self):
        return self.driver.current_url

    def forward(self):
        # 浏览器前进操作
        return self.driver.forward()

    def back(self):
        # 浏览器后退操作
        return self.driver.back()

    def isSelected(self, element):
        # 判断元素是否被选中
        return self.find_el(element).is_selected()

    def isEnabled(self, element):
        # 判断元素是否可点击
        return self.find_el(element).is_enabled()

    def HoverElement(driver, element, newDriver):
        # 悬停元素
        elements = newDriver.find_el(element)
        ActionChains(driver).move_to_element(elements).perform()

    def MoveToVisibleElement(self, element):
        # 移动到可见元素
        target = self.find_el(element)
        self.driver.execute_script("arguments[0].scrollIntoView()", target)

    def GetHandle(self):
        # 获取所有句柄
        handle_list = self.driver.window_handles
        return handle_list

    def SwitchHandle(self, handle_list, number):
        # 切换句柄
        self.driver.switch_to.window(handle_list[number])

    def getText(self, element, choose=None):
        # 获取对应文本
        if choose is None:
            return self.find_el(element).text
        elif choose == "value":
            return self.find_el(element).get_attribute("value")
        elif choose == "placeholder":
            return self.find_el(element).get_attribute("placeholder")
        elif choose == "title":
            return self.find_el(element).get_attribute("title")
        else:
            _log.warning("||请选择获取文本的方式：None 或 value 或 placeholder 或 title")

    def isElementExist(self, element):
        # 判断元素是否存在
        flag = True
        try:
            self.find_el(element)
            return flag
        except:
            flag = False
            return flag
