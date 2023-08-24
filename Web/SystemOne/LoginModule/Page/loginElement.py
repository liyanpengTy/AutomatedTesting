# -*- coding: utf-8 -*-
# @File    :loginElement
# @Date    :2023/3/28 16:22
# @Name    :LYP

from selenium.webdriver.common.by import By

class LoginElement:
    phone_element = By.XPATH, "//INPUT[@placeholder='手机号']"
    code_element = By.XPATH, "//INPUT[@placeholder='短信验证码']"
    login_button_element = By.XPATH, "(//BUTTON[@type='button'])[2]"
    cue = By.XPATH, "//div[@class='message-container message-container-error']/div"