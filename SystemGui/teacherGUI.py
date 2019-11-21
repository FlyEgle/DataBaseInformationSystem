"""
教师管理信息界面
增加，删除，修改，查询，显示， 排序界面
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt
from DataBaseInformationSystem.Method.msqlCls import ConnectSQLdb
from DataBaseInformationSystem.SystemGui.addDialog import ZhidaoLaoshiAddDataBase
from DataBaseInformationSystem.SystemGui.deleteDialog import ZhiDaoLaoshiDeleteDataBase
from DataBaseInformationSystem.SystemGui.queryDialog import ZhiDaoTeachQueryDataBase
from DataBaseInformationSystem.SystemGui.sortDialog import ZhidaoLaoshiSortDataBase
from DataBaseInformationSystem.SystemGui.updateDialog import ZhidaoTeacherUpdateDataBase


class TableZhidaoTeacherInfo(QWidget):
    def __init__(self):
        super(TableZhidaoTeacherInfo, self).__init__()
        self.sql_init()
        self.init_GUI()

    def init_GUI(self):
        self.addbtn = QPushButton('增加', self)
        self.deletebtn = QPushButton('删除', self)
        self.repairbtn = QPushButton('修改', self)
        self.querybtn = QPushButton('查询', self)

        self.titlelbl = QLabel('指导老师信息表', self)
        self.showbtn = QPushButton('显示', self)
        self.sortbtn = QPushButton('排序', self)

        self.tablelbl = QLabel('', self)

        self.desktopRect = QApplication.desktop().screenGeometry()
        self.resize(600, 400)
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl.resize(self.width() - 20, 40)
        self.titlelbl.move((self.width() - self.titlelbl.width())/2, 10)
        self.titlelbl.setStyleSheet('QLabel{border:2px solid blue}')
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.tablelbl.setStyleSheet('QLabel{border:2px solid blue}')
        self.tablelbl.resize(self.width() - 10, 280)
        self.tablelbl.move((self.width() - self.tablelbl.width())/2, 60)

        # 显示表格
        self.showTable = QTableWidget(5, 20)
        self.showTable.setHorizontalHeaderLabels(['teacher_id', 'teacher_name',
                                                  'teacher_prof', 'teacher_locate',
                                                  'teacher_home'])
        self.showTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showTable.resize(self.tablelbl.width(), self.tablelbl.height())
        self.showTable.setColumnCount(5)
        self.showTable.setRowCount(20)
        self.showTable.resizeColumnsToContents()
        self.showTable.resizeRowsToContents()

        # 设置表头属性
        self.showTable.horizontalHeader().setDefaultSectionSize(self.showTable.width()/4)
        self.showTable.horizontalHeader().setMinimumSectionSize(200)
        self.showTable.verticalHeader().setDefaultSectionSize(30)

        # 设置表格布局
        self.table_layout = QHBoxLayout()
        self.table_layout.addWidget(self.showTable)

        self.tablelbl.setLayout(self.table_layout)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.addbtn)
        self.h_layout.addWidget(self.deletebtn)
        self.h_layout.addWidget(self.repairbtn)
        self.h_layout.addWidget(self.querybtn)
        self.h_layout.addWidget(self.sortbtn)
        self.h_layout.addWidget(self.showbtn)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.h_layout)
        self.setLayout(self.vbox)

        # 点击事件
        self.button_method()

    def sql_init(self):
        self.shetuandatabase_db = ConnectSQLdb('TEACHERDATABASE').sql_connect()
        self.shetuandatabase_cursor = self.shetuandatabase_db.cursor()

    def button_method(self):
        self.showbtn.clicked.connect(self.show_database)
        self.addbtn.clicked.connect(self.add_database)
        self.deletebtn.clicked.connect(self.delete_database)
        self.querybtn.clicked.connect(self.query_database)
        self.sortbtn.clicked.connect(self.sort_database)
        self.repairbtn.clicked.connect(self.update_databse)

    # 显示按钮点击事件
    def show_database(self):
        self.showTable.update()
        self.showTable.clearContents()
        sql_db = ConnectSQLdb('TEACHERDATABASE').sql_connect()
        sql_cursor = sql_db.cursor()
        # 查询语句
        sql_query = 'SELECT * FROM teacher_information;'
        sql_cursor.execute(sql_query)
        data = sql_cursor.fetchall()
        for i in range(len(data)):
            for j in range(len(data[0])):
                newItem = QTableWidgetItem(str(data[i][j]))
                newItem.setTextAlignment(Qt.AlignCenter)
                self.showTable.setItem(i, j, newItem)

    # 增减数据点击事件
    def add_database(self):
        # 插入数据
        self.add_data_dialog = ZhidaoLaoshiAddDataBase()
        self.add_data_dialog.exec_()
        data = self.add_data_dialog.data_dict
        data_tuple = tuple([data['teacher_id'], data['teacher_name'],
                      data['teacher_prof'], data['teacher_locate'],
                            data['teacher_home']])
        print(data_tuple)
        sql_query = "INSERT INTO teacher_information VALUES ('%s', '%s', '%s', '%s', '%s')"
        self.shetuandatabase_cursor.execute(sql_query % (str(data_tuple[0]), str(data_tuple[1]),
                                                  str(data_tuple[2]), str(data_tuple[3]), str(data_tuple[4])))
        self.shetuandatabase_db.commit()

    # 删除数据点击事件
    def delete_database(self):
        # 删除数据
        self.delete_data_dialog = ZhiDaoLaoshiDeleteDataBase()
        self.delete_data_dialog.exec_()
        data_index = self.delete_data_dialog.get_data_index
        data_value = self.delete_data_dialog.get_data_value
        if type(data_value) == str:
            sql_query = "DELETE FROM teacher_information where %s='%s'" % (str(data_index), str(data_value))
        else:
            sql_query = "DELETE FROM teacher_information where %s=%s" % (str(data_index), str(data_value))
        try:
            self.shetuandatabase_cursor.execute(sql_query)
            self.shetuandatabase_db.commit()
        except:
            self.shetuandatabase_db.rollback()

    # 修改数据点击事件
    def update_databse(self):
        # 固定两个字段，更新其他属性
        self.update_data_dialog = ZhidaoTeacherUpdateDataBase()
        self.update_data_dialog.exec_()
        lianxifangshi = self.update_data_dialog.lianxifangshi_text
        suozaixi = self.update_data_dialog.locate_text
        data_index = self.update_data_dialog.get_data_index
        data_value = self.update_data_dialog.get_data_value
        if type(data_value) == str:
            sql_query = "UPDATE teacher_information SET teacher_locate='%s' WHERE %s='%s'" % (suozaixi,
                                                                                              data_index,
                                                                                              data_value)
        else:
            sql_query = "UPDATE teacher_information SET teacher_locate='%s' WHERE %s=%s" % (suozaixi,
                                                                                            data_index,
                                                                                            data_value)
        try:
            self.shetuandatabase_cursor.execute(sql_query)
            self.shetuandatabase_db.commit()
        except:
            self.shetuandatabase_db.rollback()
        if type(data_value) == str:
            sql_query2 = "UPDATE teacher_information SET teacher_home='%s' WHERE %s='%s'" % (lianxifangshi,
                                                                                             data_index,
                                                                                             data_value)
        else:
            sql_query2 = "UPDATE teacher_information SET teacher_home='%s' WHERE %s=%s" % (lianxifangshi,
                                                                                           data_index,
                                                                                           data_value)
        try:
            self.shetuandatabase_cursor.execute(sql_query2)
            self.shetuandatabase_db.commit()
        except:
            self.shetuandatabase_db.rollback()

    # 查找数据点击事件
    def query_database(self):
        # 查询出来的结果显示在tabel上
        self.query_data_dialog = ZhiDaoTeachQueryDataBase()
        self.query_data_dialog.exec_()
        data_index = self.query_data_dialog.get_data_index
        data_value = self.query_data_dialog.get_data_value
        if type(data_value) == str:
            sql_query = "SELECT * FROM teacher_information WHERE %s='%s'" % (str(data_index), str(data_value))
        else:
            sql_query = "SELECT * FROM teacher_information WHERE %s=%s" % (str(data_index), str(data_value))
        try:
            self.shetuandatabase_cursor.execute(sql_query)
            self.shetuandatabase_db.commit()
            data = self.shetuandatabase_cursor.fetchall()
            if len(data) >= 1:
                self.showTable.clearContents()
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        newItem = QTableWidgetItem(str(data[i][j]))
                        newItem.setTextAlignment(Qt.AlignCenter)
                        self.showTable.setItem(i, j, newItem)
        except:
            self.shetuandatabase_db.rollback()

    # 排序数据点击事件
    def sort_database(self):
        self.sort_data_dialog = ZhidaoLaoshiSortDataBase()
        self.sort_data_dialog.exec_()
        data_index = self.sort_data_dialog.get_data_index
        sql_query = "SELECT * from teacher_information ORDER BY %s ASC" % (str(data_index))
        try:
            self.shetuandatabase_cursor.execute(sql_query)
            self.shetuandatabase_db.commit()
            data = self.shetuandatabase_cursor.fetchall()
            if len(data) >= 1:
                self.showTable.clearContents()
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        newItem = QTableWidgetItem(str(data[i][j]))
                        newItem.setTextAlignment(Qt.AlignCenter)
                        self.showTable.setItem(i, j, newItem)
        except:
            self.shetuandatabase_db.rollback()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tableshow = TableZhidaoTeacherInfo()
    tableshow.show()
    sys.exit(app.exec_())
