"""
pymsql connect mysql database
连接后返回一个数据库游标对象
param：操作的数据库
"""
import pymysql


class ConnectSQLdb:
    def __init__(self, databse_name):
        self.host = 'localhost'
        self.port = 3306
        self.username = 'root'
        self.password = '150713'
        self.charset = 'utf8'
        self.db = databse_name

    def sql_connect(self):
        # pymsql 连接数据库
        self.sql_database = pymysql.connect(host=self.host,
                                       port=self.port,
                                       user=self.username,
                                       password=self.password,
                                       charset=self.charset,
                                       db=self.db)
        # 返回数据库对象
        return self.sql_database


if __name__ == '__main__':
    sql_db = ConnectSQLdb('SHETUANXINXIDATABASE').sql_connect()
    # print(sql_db.sql_connect())
    sql_cursor = sql_db.cursor()
    # SELECT * from runoob_tbl ORDER BY submission_date ASC;
    sql_query = 'SELECT * FROM association_information ORDER BY association_name '
    sql_cursor.execute(sql_query)
    data = sql_cursor.fetchall()
    print(data)
