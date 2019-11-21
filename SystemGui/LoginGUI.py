"""
登录，注册界面
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel
from DataBaseInformationSystem.SystemGui.mainWinGUI import MainWin
from DataBaseInformationSystem.Method.msqlCls import ConnectSQLdb


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.loginpasswdtext = QLineEdit(self)
        self.loginaccounttext = QLineEdit(self)
        self.registbtn = QPushButton('注册', self)
        self.loginbtn = QPushButton('登录', self)
        self.accountlbl = QLabel('账号', self)
        self.passwordlbl = QLabel('密码', self)

        self.regist_account_text = QLineEdit(self)
        self.regist_password_text = QLineEdit(self)
        self.registion_btn = QPushButton('注册', self)

        # systemdatabase init
        self.sys_db = ConnectSQLdb('SYSTEMBASE').sql_connect()
        self.sys_db_cursor = self.sys_db.cursor()

        self.init_GUI()

    def init_GUI(self):
        self.resize(200, 200)
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        # 登录gui
        self.loginaccounttext.resize(100, 30)
        self.loginpasswdtext.resize(100, 30)
        self.loginbtn.resize(60, 30)
        self.registbtn.resize(60, 30)
        self.accountlbl.resize(30, 30)
        self.passwordlbl.resize(30, 30)

        self.loginaccounttext.move(60, 40)
        self.loginpasswdtext.move(60, 80)
        self.accountlbl.move(20, 40)
        self.passwordlbl.move(20, 80)
        self.loginbtn.move(100, 140)
        self.registbtn.move(20, 140)

        # 注册gui
        self.regist_account_text.resize(100, 30)
        self.regist_password_text.resize(100, 30)
        self.registion_btn.resize(60, 30)

        self.regist_account_text.move(60, 40)
        self.regist_password_text.move(60, 80)
        self.registion_btn.move(60, 140)
        self.registion_btn.hide()
        self.regist_account_text.hide()
        self.regist_password_text.hide()

        self.buttonMethod()

        self.setWindowTitle('登录信息系统')
        self.show()

    def buttonMethod(self):
        self.loginbtn.clicked.connect(self.loginMethod)
        self.registbtn.clicked.connect(self.registionMethod)
        self.registion_btn.clicked.connect(self.registionClickedMethod)

    # 登录方法
    def loginMethod(self):
        """进行数据库查表操作，如果账号和密码匹配到数据库就进入主界面，如果么有返回一个
        提示框，提醒输入不正确！
        """
        sql_query = "SELECT * FROM system_information"
        self.sys_db_cursor.execute(sql_query)
        data = self.sys_db_cursor.fetchall()
        for i in range(len(data)):
            if self.loginaccounttext.text() == data[i][1]:
                if self.loginpasswdtext.text() == data[i][2]:
                    self.hide()
                    self.main_win = MainWin()
                    self.main_win.show()
                    break

    # 注册信息
    def registionMethod(self):
        self.loginaccounttext.hide()
        self.loginpasswdtext.hide()
        self.registbtn.hide()
        self.loginbtn.hide()
        self.registion_btn.show()
        self.regist_account_text.show()
        self.regist_password_text.show()

    def registionClickedMethod(self):
        """每次点击注册，先获取数据库中的数据信息，计算当前数据库的长度，再把填写好的数据库信息进行插入
        """
        count_sql = 'SELECT COUNT(*) FROM system_information'
        self.sys_db_cursor.execute(count_sql)
        count_data = self.sys_db_cursor.fetchone()
        # 当前编号是数据库中已有信息的长度+1
        current_sysID = int(count_data[0]) + 1
        # insert into database
        insert_sql = "INSERT INTO system_information VALUES ('%s', '%s', '%s')"
        regist_account = self.regist_account_text.text()
        regist_password = self.regist_password_text.text()
        self.sys_db_cursor.execute(insert_sql % (str(current_sysID), str(regist_account), str(regist_password)))
        self.sys_db.commit()

        self.loginaccounttext.show()
        self.loginpasswdtext.show()
        self.registbtn.show()
        self.loginbtn.show()
        self.registion_btn.hide()
        self.regist_account_text.hide()
        self.regist_password_text.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())

