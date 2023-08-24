# -*- coding: utf-8 -*-
# @File    :operation_db
# @Date    :2023/3/28 8:55
# @Name    :LYP

import pymysql
from Common.config import conf
from Common.getTime import Time


class OperationDB(object):
    """ MySQL数据库操作 """

    def __init__(self, sectioName):
        self.db = None
        self.sectioName = sectioName
        self.keyList = conf.get_options(self.sectioName)

    def connect_db(self):
        """
        连接数据库
        :return:
        """
        host = conf.get_value(self.sectioName, self.keyList[0])
        port = conf.get_value(self.sectioName, self.keyList[1])
        user = conf.get_value(self.sectioName, self.keyList[2])
        passwd = conf.get_value(self.sectioName, self.keyList[3])
        # database = conf.get_value(self.sectioName, self.keyList[4])
        charset = conf.get_value(self.sectioName, self.keyList[5])
        try:
            # self.db = pymysql.connect(host=host, port=int(port), user=user, password=passwd, database=database, charset=charset)
            self.db = pymysql.connect(host=host, port=int(port), user=user, password=passwd, charset=charset)
            return True, '连接数据成功'
        except Exception as e:
            return False, '连接数据失败【' + str(e) + '】'

    def close_db(self):
        """
        关闭数据连接
        :return:
        """
        self.db.close()

    def excel_sql(self, SQL, state):
        """
        执行SQL方法
        :param state:
        :param SQL: SQL语句
        :return:
        """
        isOKs, results = self.connect_db()
        if isOKs is False:
            return isOKs, results
        try:
            # 创建游标
            cursor = self.db.cursor()
            cursor.execute(SQL)
            rows = None
            if state == "double":
                rows = cursor.fetchall()  # 查询所有数据
            elif state == "single":
                rows = list(cursor.fetchone())  # 查询一条数据
            results = {}
            # 判断是不是查询数据
            if rows is not None and 'select' in SQL.lower():
                des = cursor.description
                title_list = [item[0] for item in des]  # 获取对应表的字段名列表
                # 获取全部数据
                if state == "double":
                    # 遍历循环查询到的数据量
                    for i in range(len(rows)):
                        value_dict = {}
                        # 遍历循环将每一条查询到的数据，插入到对应的字段名中，形成字典
                        for j in range(len(title_list)-1):
                            value_dict[title_list[j + 1]] = rows[i][j+1]
                        results[rows[i][0]] = value_dict
                # 获取查询结果的第一条数据
                elif state == "single":
                    for i in range(len(rows)):
                        for j in range(len(title_list)):
                            results[title_list[j]] = rows[j]
            # 判断是不是插入或者更新数据
            elif rows is None and ('insert' in SQL.lower() or 'update' in SQL.lower()):
                # 提交数据操作，不然插入或者更新，数据只会更新在缓存，没正式落库
                self.db.commit()
                results = ''
            cursor.close()
            self.close_db()
            return True, results
        except Exception as e:
            return False, 'SQL执行失败,原因：[' + str(e) + ']'


# oper = OperationDB("test_db")
# sql = "SELECT phone,id FROM master_db.user_info WHERE data_or_inside = 1 AND state = 0"
# isOk, phone = oper.excel_sql(sql, "single")
# # # isOk, phone = oper.oper.excel_sql(sql, "double")
# print(isOk, phone)
# print(phone["phone"])
