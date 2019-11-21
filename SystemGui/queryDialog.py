"""
查询数据库中的信息，按两种方式进行查询，一个是按编号排序，一个是按名称排序
"""
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QComboBox
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import Qt


# 社团信息
class SheTuanInfoQueryDataBase(QDialog):
    def __init__(self):
        super(SheTuanInfoQueryDataBase, self).__init__()
        self.label_dict = {'社团名称': 'association_name',
                           '社团编号': 'association_id'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 输入信息
        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)


        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("社团名称")
        self.combo.addItem("社团编号")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 财务管理
class CaiWuManageQueryDataBase(QDialog):
    def __init__(self):
        super(CaiWuManageQueryDataBase, self).__init__()
        self.label_dict = {'发票编号': 'money_id',
                           '发票抬头': 'money_title'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        # 输入信息
        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("发票编号")
        self.combo.addItem("发票抬头")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 社员
class SheyuanQueryDataBase(QDialog):
    def __init__(self):
        super(SheyuanQueryDataBase, self).__init__()
        self.label_dict = {'学号': 'person_id',
                           '姓名': 'person_name'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("学号")
        self.combo.addItem("姓名")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 活动信息
class HuoDongQueryDataBase(QDialog):
    def __init__(self):
        super(HuoDongQueryDataBase, self).__init__()
        self.label_dict = {
            '活动地点': 'activate_locate',
            '活动时间': 'activate_time'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("活动地点")
        self.combo.addItem("活动时间")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 系统管理
class SystemManageQueryDataBase(QDialog):
    def __init__(self):
        super(SystemManageQueryDataBase, self).__init__()
        self.init_gui()

    def init_gui(self):
        pass


# 社团团长
class SheTuanTuanZhangQueryDataBase(QDialog):
    def __init__(self):
        super(SheTuanTuanZhangQueryDataBase, self).__init__()
        self.label_dict = {
            '团长编号': 'shetuantuanzhang_id',
            '委员名': 'shetuantuanzhang_name'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("团长编号")
        self.combo.addItem("委员名")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 合作单位
class HeZuoDanWeiQueryDataBase(QDialog):
    def __init__(self):
        super(HeZuoDanWeiQueryDataBase, self).__init__()
        self.label_dict = {
            '单位名称': 'hezuodanwei_name',
            '单位地址': 'hezuodanwei_locate'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("单位名称")
        self.combo.addItem("单位地址")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 指导老师
class ZhiDaoTeachQueryDataBase(QDialog):
    def __init__(self):
        super(ZhiDaoTeachQueryDataBase, self).__init__()
        self.label_dict = {
            '教师编号': 'teacher_id',
            '教师名': 'teacher_name'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("教师编号")
        self.combo.addItem("教师名")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


class SystemQueryDataBase(QDialog):
    def __init__(self):
        super(SystemQueryDataBase, self).__init__()
        self.label_dict = {
            '系统编号': 'system_id',
            '系统账号': 'system_account'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('查询数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)

        # 输入信息框
        self.info_line = QLineEdit(self)
        self.info_line.resize(100, 20)
        self.info_line.move(150, 40)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("系统编号")
        self.combo.addItem("系统账号")
        self.combo.move((self.width() - self.combo.width()) / 2, 70)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 100)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        self.get_data_value = self.info_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    query = SystemQueryDataBase()
    sys.exit(app.exec_())
