"""
更新数据库中的信息，按两种方式进行排序，一个是按编号更新，一个是按名称更新
"""
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QComboBox
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import Qt


# 社团信息
class SheTuanInfoUpdateDataBase(QDialog):
    def __init__(self):
        super(SheTuanInfoUpdateDataBase, self).__init__()
        self.label_dict = {'社团名称': 'association_name',
                           '社团编号': 'association_id'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('社团地点', self)
        self.lianxifangshi_lbl = QLabel('联系方式', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.locate_line = QLineEdit(self)
        self.locate_line.resize(100, 20)
        self.locate_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("社团名称")
        self.combo.addItem("社团编号")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.locate_text = self.locate_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.locate_text, self.get_data_index)
        self.close()


# 财务管理
class CaiwuguanliUpdateDataBase(QDialog):
    def __init__(self):
        super(CaiwuguanliUpdateDataBase, self).__init__()
        self.label_dict = {'发票编号': 'money_id',
                           '发票抬头': 'money_title'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('经费额度', self)
        self.lianxifangshi_lbl = QLabel('报销时间', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.locate_line = QLineEdit(self)
        self.locate_line.resize(100, 20)
        self.locate_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("发票编号")
        self.combo.addItem("发票抬头")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.locate_text = self.locate_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.locate_text, self.get_data_index)
        self.close()


# 社员信息
class SheyuanInfoUpdateDataBase(QDialog):
    def __init__(self):
        super(SheyuanInfoUpdateDataBase, self).__init__()
        self.label_dict = {'学号': 'person_id',
                           '姓名': 'person_name'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('所在系', self)
        self.lianxifangshi_lbl = QLabel('联系电话', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.locate_line = QLineEdit(self)
        self.locate_line.resize(100, 20)
        self.locate_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("学号")
        self.combo.addItem("姓名")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.locate_text = self.locate_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.locate_text, self.get_data_index)
        self.close()


# 活动信息
class HuodongxinxiUpdateDataBase(QDialog):
    def __init__(self):
        super(HuodongxinxiUpdateDataBase, self).__init__()
        self.label_dict = {'活动地点': 'activate_locate',
                           '活动时间': 'activate_time'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('活动内容', self)
        # self.lianxifangshi_lbl = QLabel('联系电话', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        # self.lianxifangshi_lbl.resize(60, 20)
        # self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.context_line = QLineEdit(self)
        self.context_line.resize(100, 20)
        self.context_line.move(150, 80)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("活动地点")
        self.combo.addItem("活动时间")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.context_text = self.context_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.context_text, self.get_data_index)
        self.close()


# 系统管理
# 社团团长
class ShetuantuanzhangUpdateDataBase(QDialog):
    def __init__(self):
        super(ShetuantuanzhangUpdateDataBase, self).__init__()
        self.label_dict = {'团长编号': 'shetuantuanzhang_id',
                           '委员名': 'shetuantuanzhang_name'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.suozaixi_lbl = QLabel('所在系', self)
        self.lianxifangshi_lbl = QLabel('联系电话', self)
        self.suozaixi_lbl.resize(60, 20)
        self.suozaixi_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.suozaixi_line = QLineEdit(self)
        self.suozaixi_line.resize(100, 20)
        self.suozaixi_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("团长编号")
        self.combo.addItem("委员名")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.suozaixi_text = self.suozaixi_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.suozaixi_text, self.get_data_index)
        self.close()


# 合作单位
class HezuodanweiUpdateDataBase(QDialog):
    def __init__(self):
        super(HezuodanweiUpdateDataBase, self).__init__()
        self.label_dict = {'单位地址': 'hezuodanwei_locate',
                           '单位名称': 'hezuodanwei_name'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('合作项目', self)
        self.lianxifangshi_lbl = QLabel('联系电话', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.locate_line = QLineEdit(self)
        self.locate_line.resize(100, 20)
        self.locate_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("单位地址")
        self.combo.addItem("单位名称")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.locate_text = self.locate_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.locate_text, self.get_data_index)
        self.close()


# 指导老师
class ZhidaoTeacherUpdateDataBase(QDialog):
    def __init__(self):
        super(ZhidaoTeacherUpdateDataBase, self).__init__()
        self.label_dict = {'教师编号': 'teacher_id',
                           '教师名': 'teacher_name'}
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.locate_lbl = QLabel('所在系', self)
        self.lianxifangshi_lbl = QLabel('办公室', self)
        self.locate_lbl.resize(60, 20)
        self.locate_lbl.move(60, 80)
        self.lianxifangshi_lbl.resize(60, 20)
        self.lianxifangshi_lbl.move(60, 120)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.locate_line = QLineEdit(self)
        self.locate_line.resize(100, 20)
        self.locate_line.move(150, 80)
        self.lianxifangshi_line = QLineEdit(self)
        self.lianxifangshi_line.resize(100, 20)
        self.lianxifangshi_line.move(150, 120)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("教师编号")
        self.combo.addItem("教师名")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.lianxifangshi_text = self.lianxifangshi_line.text()
        self.locate_text = self.locate_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.lianxifangshi_text, self.locate_text, self.get_data_index)
        self.close()


# 系统更新
class SystemUpdateDataBase(QDialog):
    def __init__(self):
        super(SystemUpdateDataBase, self).__init__()
        self.label_dict = {
            '系统编号': 'system_id',
            '系统账号': 'system_account'
        }
        self.init_gui()

    def init_gui(self):
        self.resize(300, 240)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('更新数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)
        self.titlelbl.setAlignment(Qt.AlignCenter)

        self.input_lbl = QLabel('输入信息', self)
        self.input_lbl.resize(60, 20)
        self.input_lbl.move(60, 40)
        self.pwd_lbl = QLabel('系统密码', self)
        self.pwd_lbl.resize(60, 20)
        self.pwd_lbl.move(60, 80)

        # 输入信息框
        self.input_line = QLineEdit(self)
        self.input_line.resize(100, 20)
        self.input_line.move(150, 40)
        self.pwd_line = QLineEdit(self)
        self.pwd_line.resize(100, 20)
        self.pwd_line.move(150, 80)

        # 下拉菜单
        self.combo = QComboBox(self)
        self.combo.addItem("系统编号")
        self.combo.addItem("系统账号")
        self.combo.move((self.width() - self.combo.width()) / 2, 160)

        # save button
        self.save_btn = QPushButton('更新', self)
        self.save_btn.move((self.width() - self.save_btn.width()) / 2, 200)
        self.show()

        self.save_btn.clicked.connect(self.clicked_method)

    def clicked_method(self):
        global text_string
        self.pwd_text = self.pwd_line.text()
        self.get_data_value = self.input_line.text()
        text = self.combo.currentText()
        for key, value in self.label_dict.items():
            if text == key:
                text_string = self.label_dict[key]
                break
        self.get_data_index = text_string

        print(self.pwd_text, self.get_data_index)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    update = SystemUpdateDataBase()
    sys.exit(app.exec_())
