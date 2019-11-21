"""
排序数据库中的信息，按两种方式进行排序，一个是按编号排序，一个是按名称排序
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtWidgets import QDialog, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


# 社团信息排序数据库数据
class SheTuanXinXiSortDataBase(QDialog):
    def __init__(self):
        super(SheTuanXinXiSortDataBase, self).__init__()
        self.label_dict = {'社团名称': 'association_name',
                           '社团编号': 'association_id'}
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("社团名称")
        self.combo.addItem("社团编号")
        self.combo.move((self.width() - self.combo.width())/2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)

        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 财务管理排序数据库数据
class CaiWuGuanLiSortDataBase(QDialog):
    def __init__(self):
        super(CaiWuGuanLiSortDataBase, self).__init__()
        self.label_dict = {'发票编号': 'money_id',
                           '发票抬头': 'money_title'}
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("发票编号")
        self.combo.addItem("发票抬头")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)

        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 社员排序数据库数据
class SheYuanSortDataBase(QDialog):
    def __init__(self):
        super(SheYuanSortDataBase, self).__init__()
        self.label_dict = {'学号': 'person_id',
                           '姓名': 'person_sex'}
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("学号")
        self.combo.addItem("姓名")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 活动信息
class HuodongSortDataBase(QDialog):
    def __init__(self):
        super(HuodongSortDataBase, self).__init__()
        self.label_dict = {
            '活动地点': 'activate_locate',
            '活动时间': 'activate_time'
        }
        self.init_gui()

    def init_gui(self):

        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("活动地点")
        self.combo.addItem("活动时间")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        print(self.get_data_index)
        self.close()


# 系统管理
class SystemManageSortDataBase(QDialog):
    def __init__(self):
        super(SystemManageSortDataBase, self).__init__()
        self.label_dict = {
            '系统编号': 'system_id',
            '系统账号': 'system_account'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("系统编号")
        self.combo.addItem("系统账号")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        print(self.get_data_index)
        self.close()


# 社团团长
class SheTuanTuanZhangSortDataBase(QDialog):
    def __init__(self):
        super(SheTuanTuanZhangSortDataBase, self).__init__()
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

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("团长编号")
        self.combo.addItem("委员名")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 合作单位
class HeZuoDanweiSortDataBase(QDialog):
    def __init__(self):
        super(HeZuoDanweiSortDataBase, self).__init__()
        self.label_dict = {
            '单位名称': 'hezuodanwei_name',
            '单位地址': 'hezuodanwei_locate'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("单位名称")
        self.combo.addItem("单位地址")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('排序', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


# 指导老师
class ZhidaoLaoshiSortDataBase(QDialog):
    def __init__(self):
        super(ZhidaoLaoshiSortDataBase, self).__init__()
        self.label_dict = {
            '教师编号': 'teacher_id',
            '教师名': 'teacher_name'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(200, 150)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('排序数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("教师编号")
        self.combo.addItem("教师名")
        self.combo.move((self.width() - self.combo.width()) / 2, 40)

        # save button
        self.save_btn = QPushButton('查询', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 80)
        self.save_btn.clicked.connect(self.clicked_method)
        self.show()

    def clicked_method(self):
        global text_string
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sortdatabase = SystemManageSortDataBase()
    sys.exit(sortdatabase.exec_())
