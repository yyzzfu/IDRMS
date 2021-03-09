import mysql.connector
from Common.dir_config import *
from Common.read_config import ReadConfig
from Common.my_log import MyLog


class DoMysql:

    def delete_all_datas_from_table(self, table_name):  # 用来删除指定表中的所有数据
        '''
        :param table_name: 数据库中表的名字
        :return:
        '''
        try:
            db_config = eval(ReadConfig().get_config_data(config_path, 'DB', 'db_config'))
            cnn = mysql.connector.connect(**db_config)  # 建立数据库连接
            cursor = cnn.cursor()  # 游标cursor
            sql = 'delete from {}'.format(table_name)
            cursor.execute(sql)  # 执行语句
            cnn.commit()  # 提交
            cursor.close()   # 关闭游标
            cnn.close()   # 关闭连接
            MyLog().info('删除数据库中--》{}表《--成功！！！'.format(table_name))
        except:
            MyLog().error('删除数据库中--》{}表《--失败！！！'.format(table_name))

    def delete_datas_from_table_with_sql(self, sql):  # 用来删除指定表中的所有数据
        '''
        :param table_name: 数据库中表的名字
        :return:
        '''
        try:
            db_config = eval(ReadConfig().get_config_data(config_path, 'DB', 'db_config'))
            cnn = mysql.connector.connect(**db_config)  # 建立数据库连接
            cursor = cnn.cursor()  # 游标cursor
            cursor.execute(sql)  # 执行语句
            cnn.commit()  # 提交
            cursor.close()   # 关闭游标
            cnn.close()   # 关闭连接
            MyLog().info('执行数据库语句--》{}《--成功！！！'.format(sql))
        except:
            MyLog().error('执行数据库语句--》{}《--失败！！！'.format(sql))

    def get_datas_from_database(self, sql, state='all'):   # 读取数据
        '''
        :param sql: 需要执行的sql语句
        :param state: 查询一条数据时,state=1；查询多条数据时,state='all'
        :return: res为查询到的结果
        '''
        db_config = eval(ReadConfig().get_config_data(config_path, 'DB', 'db_config'))
        cnn = mysql.connector.connect(**db_config)  # 建立数据库连接
        cursor = cnn.cursor()  # 游标cursor
        cursor.execute(sql)  # 执行语句
        # cnn.commit()
        if state == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        cursor.close()   # 关闭游标
        cnn.close()   # 关闭连接
        return res


if __name__ == '__main__':
    table_name = 'ar_data_point'
    # DoMysql().delete_all_datas_from_table(table_name)
    sql = 'DELETE FROM sys_user WHERE login_name <> "{}" and login_name <> "{}" and login_name <> "{}"'.format('thinkgem', 'idrmstest', 'idrmstest1')
    # sql = 'SELECT * FROM sys_user WHERE login_name = "{}"'.format('thinkgem')
    a = DoMysql().delete_datas_from_table_with_sql(sql)
    # print(a)
    # print(len(a))
