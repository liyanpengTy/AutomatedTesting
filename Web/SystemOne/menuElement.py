# -*- coding: utf-8 -*-
# @File    :menuElement
# @Date    :2023/3/28 16:15
# @Name    :LYP

from Common.Log import log
from selenium.webdriver.common.by import By


ElementData = {
    "城市洞察": "#/Insight/City/iframe",
    "城市统计": "#/Insight/City/stat/cityStat",
    "企业财务分析": "#/Insight/enterprise/111/iframe",
    "三道红线": "#/Insight/enterprise/112/iframe",
    "企业融资成本分析": "#/Insight/enterprise/113/iframe",
    "企业收入质量分析": "#/Insight/enterprise/114/iframe",
    "企业销售及土地储备分析": "#/Insight/enterprise/115/iframe",
    "竞企-财务": "#/Insight/enterprise/competing/financial",
    "企业搜索": "#/Insight/enterprise/enterpriseHome/enterpriseSearch",
    "企业信息": "#/Insight/enterprise/enterpriseHome/reHouseEnterprise/information",
    "房企-财务": "#/Insight/enterprise/enterpriseHome/reHouseEnterprise/finance",
    "融资": "#/Insight/enterprise/enterpriseHome/reHouseEnterprise/financing/index.vue",
    "销售": "#/Insight/enterprise/enterpriseHome/reHouseEnterprise/sale",
    "土地储备": "#/Insight/enterprise/enterpriseHome/reHouseEnterprise/landReserve",
    "运营统计": "#/Insight/enterprise/bank/operate",
    "银行信息": "#/Insight/enterprise/bank/bankInformation",
    "土地观察": "#/Insight/land/107/iframe",
    "土地概览": "#/Insight/land/landOverview",
    "列表搜索": "#/Insight/land/listSearch",
    "地图搜索": "#/Insight/land/mapSearch",
    "首发": "#/Insight/financialMarket/financialProduct/stock",
    "境内债": "#/Insight/financialMarket/financialProduct/Bond/domesticDebt",
    "境外债": "#/Insight/financialMarket/financialProduct/Bond/foreignDebt",
    "经济视野": "#/Insight/MacroEconomy/iframe",
    "地图概览": "#/Insight/MacroEconomy/EconomicStatistics/MapView",
    "数据查询": "#/Insight/MacroEconomy/EconomicStatistics/DataSearch",
}

def menu(level, choose, number=None, value=None):
    if level == 1:
        if choose == 0:
            """ 1：首页； 2：大数据赋能； 3：数据洞察； 4：定制化； 5：深度研究 """
            return By.XPATH, "(//div[@tag='div'])[" + str(number) + "]"
        elif choose == 1:
            """ 导航栏-姓名位置 """
            return By.XPATH, "//i[@class='ivu-icon ivu-icon-ios-arrow-down']/.."
        else:
            log.warning("||请选择正确的菜单编号")
    elif level == 2:
        if choose == 0:
            """ 1：城市系统/房屋智能估价； 2：企业监测； 3：土地市场； 4：金融市场； 5：宏观经济 """
            return By.XPATH, "(//DIV[@class='tabItem-box-item'])["+str(number)+"]"
        else:
            log.warning("||请选择正确的菜单编号")
    elif level == 3:
        """ 侧边栏菜单 """
        if choose == 0:
            if 0 < value < 6:
                """
                value:
                1：房屋智能估价（单套）、商品房统计、企业视角、地块列表、金融产品、经济统计;
                2：房屋智能估价（批量）、企业分析、债券;
                3：企业大数据;
                4：房企;
                5：银行;
                """
                return By.XPATH, "(//div[@class='ivu-menu-submenu-title'])["+str(number)+"]"
            else:
                log.warning("||请选择正确的菜单编号")
        elif choose == 1:
            """数据洞察下的菜单"""
            return By.XPATH, "//a[@href='"+str(ElementData[value])+"']"
        elif choose == 2:
            """ value为菜单名称 """
            return By.XPATH, "//li[text()='"+str(value)+"']"
            # driver.find_element(By.XPATH, "//*[contains(text(), '下一页')]")
        else:
            log.warning("||请选择正确的侧边栏菜单")
    else:
        log.warning("||请选择正确的菜单级别")