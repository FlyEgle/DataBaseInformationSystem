"""
增加数据库中的数据信息
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QDialog, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


# 社团信息增加数据对话框
class ShetuanxinxiAddDatabase(QDialog):
    def __init__(self):
        super(ShetuanxinxiAddDatabase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width())/2, 5)

        self.shetuanbianhao = QLabel('社团编号', self)
        self.shetuanming = QLabel('社团名', self)
        self.shetuandidian = QLabel('社团地点', self)
        self.lianxifangshi = QLabel('联系方式', self)

        self.shetuanbianhao_line = QLineEdit(self)
        self.shetuanming_line = QLineEdit(self)
        self.shetuandidian_line = QLineEdit(self)
        self.lianxifangshi_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.shetuanbianhao)
        self.h_box1.addWidget(self.shetuanbianhao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.shetuanming)
        self.h_box2.addWidget(self.shetuanming_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.shetuandidian)
        self.h_box3.addWidget(self.shetuandidian_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.lianxifangshi)
        self.h_box4.addWidget(self.lianxifangshi_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['association_id'] = self.shetuanbianhao_line.text()
        self.data_dict['association_name'] = self.shetuanming_line.text()
        self.data_dict['association_location'] = self.shetuandidian_line.text()
        self.data_dict['association_phone'] = self.lianxifangshi_line.text()
        self.close()


# 财务管理增加数据对话框
class CaiwuguanliAddDatabase(QDialog):
    def __init__(self):
        super(CaiwuguanliAddDatabase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.fapiaobianhao = QLabel('发票编号', self)
        self.fapiaotaitou = QLabel('发票抬头', self)
        self.jingfeiedu = QLabel('经费额度', self)
        self.baoxiaoshijian = QLabel('报销时间', self)

        self.fapiaobianhao_line = QLineEdit(self)
        self.fapiaotaitou_line = QLineEdit(self)
        self.jingfeiedu_line = QLineEdit(self)
        self.baoxiaoshijian_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.fapiaobianhao)
        self.h_box1.addWidget(self.fapiaobianhao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.fapiaotaitou)
        self.h_box2.addWidget(self.fapiaotaitou_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.jingfeiedu)
        self.h_box3.addWidget(self.jingfeiedu_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.baoxiaoshijian)
        self.h_box4.addWidget(self.baoxiaoshijian_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)
        self.show()

    def save_clicked(self):
        self.data_dict['money_id'] = self.fapiaobianhao_line.text()
        self.data_dict['money_title'] = self.fapiaotaitou_line.text()
        self.data_dict['money_cost'] = self.jingfeiedu_line.text()
        self.data_dict['money_time'] = self.baoxiaoshijian_line.text()
        self.close()


# 社员增加数据对话框
class SheyunAddDatabase(QDialog):
    def __init__(self):
        super(SheyunAddDatabase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.xuehao = QLabel('学号', self)
        self.name = QLabel('名字', self)
        self.sex = QLabel('性别', self)
        self.suozaixi = QLabel('所在系', self)
        self.lianxifangshi = QLabel('联系方式', self)

        self.xuehao_line = QLineEdit(self)
        self.name_line = QLineEdit(self)
        self.sex_line = QLineEdit(self)
        self.suozaixi_line = QLineEdit(self)
        self.lianxifangshi_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.xuehao)
        self.h_box1.addWidget(self.xuehao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.name)
        self.h_box2.addWidget(self.name_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.sex)
        self.h_box3.addWidget(self.sex_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.suozaixi)
        self.h_box4.addWidget(self.suozaixi_line)
        self.h_box5.setStretch(5, 5)
        self.h_box5.addWidget(self.lianxifangshi)
        self.h_box5.addWidget(self.lianxifangshi_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['person_id'] = self.xuehao_line.text()
        self.data_dict['person_name'] = self.name_line.text()
        self.data_dict['person_sex'] = self.sex_line.text()
        self.data_dict['person_locate'] = self.suozaixi_line.text()
        self.data_dict['person_iphone'] = self.lianxifangshi_line.text()
        print(self.data_dict)
        self.close()


# 活动信息增加数据
class HuoDongXinXiAddDataBase(QDialog):
    def __init__(self):
        super(HuoDongXinXiAddDataBase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.huodongdidian = QLabel('活动地点', self)
        self.huodongshijian = QLabel('活动时间', self)
        self.huodongneirong = QLabel('活动内容', self)

        self.huodongdidian_line = QLineEdit(self)
        self.huodongshijian_line = QLineEdit(self)
        self.huodongneirong_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.huodongdidian)
        self.h_box1.addWidget(self.huodongdidian_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.huodongshijian)
        self.h_box2.addWidget(self.huodongshijian_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.huodongneirong)
        self.h_box3.addWidget(self.huodongneirong_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['activate_locate'] = self.huodongdidian_line.text()
        self.data_dict['activate_time'] = self.huodongshijian_line.text()
        self.data_dict['activate_content'] = self.huodongneirong_line.text()
        print(self.data_dict)
        self.close()


# 社团团长增加数据
class ShetuantuanzhangAddDataBase(QDialog):
    def __init__(self):
        super(ShetuantuanzhangAddDataBase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.tuanzhangbianhao = QLabel('团长编号', self)
        self.weiyuanming = QLabel('委员名', self)
        self.suozaixi = QLabel('所在系', self)
        self.xingbie = QLabel('性别', self)
        self.lianxifangshi = QLabel('联系方式', self)

        self.tuanzhangbianhao_line = QLineEdit(self)
        self.weiyuanming_line = QLineEdit(self)
        self.suozaixi_line = QLineEdit(self)
        self.xingbie_line = QLineEdit(self)
        self.lianxifangshi_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.tuanzhangbianhao)
        self.h_box1.addWidget(self.tuanzhangbianhao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.weiyuanming)
        self.h_box2.addWidget(self.weiyuanming_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.xingbie)
        self.h_box3.addWidget(self.xingbie_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.suozaixi)
        self.h_box4.addWidget(self.suozaixi_line)
        self.h_box5.setStretch(5, 5)
        self.h_box5.addWidget(self.lianxifangshi)
        self.h_box5.addWidget(self.lianxifangshi_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['shetuantuanzhang_id'] = self.tuanzhangbianhao_line.text()
        self.data_dict['shetuantuanzhang_name'] = self.weiyuanming_line.text()
        self.data_dict['shetuantuanzhang_locate'] = self.suozaixi_line.text()
        self.data_dict['shetuantuanzhang_sex'] = self.xingbie_line.text()
        self.data_dict['shetuantuanzhang_iphone'] = self.lianxifangshi_line.text()
        print(self.data_dict)
        self.close()


# 合作单位增加数据
class HeZuoDanWeiAddDataBase(QDialog):
    def __init__(self):
        super(HeZuoDanWeiAddDataBase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.danweimingcheng = QLabel('单位名称', self)
        self.danweidizhi = QLabel('单位地址', self)
        self.lianxidianhua = QLabel('联系电话', self)
        self.hezuoxiangmu = QLabel('合作项目', self)

        self.danweimingcheng_line = QLineEdit(self)
        self.danweidizhi_line = QLineEdit(self)
        self.lianxidianhua_line = QLineEdit(self)
        self.hezuoxiangmu_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.danweimingcheng)
        self.h_box1.addWidget(self.danweimingcheng_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.danweidizhi)
        self.h_box2.addWidget(self.danweidizhi_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.lianxidianhua)
        self.h_box3.addWidget(self.lianxidianhua_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.hezuoxiangmu)
        self.h_box4.addWidget(self.hezuoxiangmu_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['hezuodanwei_name'] = self.danweimingcheng_line.text()
        self.data_dict['hezuodanwei_locate'] = self.danweidizhi_line.text()
        self.data_dict['hezuodanwei_iphone'] = self.lianxidianhua_line.text()
        self.data_dict['hezuodanwei_project'] = self.hezuoxiangmu_line.text()
        print(self.data_dict)
        self.close()


# 指导老师增加数据
class ZhidaoLaoshiAddDataBase(QDialog):
    def __init__(self):
        super(ZhidaoLaoshiAddDataBase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.jiaoshibianhao = QLabel('教师编号', self)
        self.jiaoshiming = QLabel('教师名', self)
        self.zhicheng = QLabel('职称', self)
        self.suozaixi = QLabel('所在系', self)
        self.bangongdizhi = QLabel('办公地址', self)

        self.jiaoshibianhao_line = QLineEdit(self)
        self.jiaoshiming_line = QLineEdit(self)
        self.suozaixi_line = QLineEdit(self)
        self.zhicheng_line = QLineEdit(self)
        self.bangongdizhi_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.jiaoshibianhao)
        self.h_box1.addWidget(self.jiaoshibianhao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.jiaoshiming)
        self.h_box2.addWidget(self.jiaoshiming_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.zhicheng)
        self.h_box3.addWidget(self.zhicheng_line)
        self.h_box4.setStretch(5, 5)
        self.h_box4.addWidget(self.suozaixi)
        self.h_box4.addWidget(self.suozaixi_line)
        self.h_box5.setStretch(5, 5)
        self.h_box5.addWidget(self.bangongdizhi)
        self.h_box5.addWidget(self.bangongdizhi_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['teacher_id'] = self.jiaoshibianhao_line.text()
        self.data_dict['teacher_name'] = self.jiaoshiming_line.text()
        self.data_dict['teacher_prof'] = self.zhicheng_line.text()
        self.data_dict['teacher_locate'] = self.suozaixi_line.text()
        self.data_dict['teacher_home'] = self.bangongdizhi_line.text()
        print(self.data_dict)
        self.close()


# 系统信息增加数据
class SystemAddDataBase(QDialog):
    def __init__(self):
        super(SystemAddDataBase, self).__init__()
        self.data_dict = {}
        self.init_GUI()

    def init_GUI(self):
        self.resize(300, 300)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.titlelbl = QLabel('增加数据', self)
        self.titlelbl.resize(100, 30)
        self.titlelbl.move((self.width() - self.titlelbl.width()) / 2, 5)

        self.xitongbianhao_lbl = QLabel('系统编号', self)
        self.xitongzhanghao_lbl = QLabel('账号', self)
        self.xitongmima_lbl = QLabel('密码', self)

        self.xitongbianhao_line = QLineEdit(self)
        self.xitongzhanghao_line = QLineEdit(self)
        self.xitongmima_line = QLineEdit(self)

        self.save_btn = QPushButton('保存', self)
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.h_box1.setStretch(5, 5)
        self.h_box1.addWidget(self.xitongbianhao_lbl)
        self.h_box1.addWidget(self.xitongbianhao_line)
        self.h_box2.setStretch(5, 5)
        self.h_box2.addWidget(self.xitongzhanghao_lbl)
        self.h_box2.addWidget(self.xitongzhanghao_line)
        self.h_box3.setStretch(5, 5)
        self.h_box3.addWidget(self.xitongmima_lbl)
        self.h_box3.addWidget(self.xitongmima_line)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addWidget(self.save_btn)

        self.setLayout(self.v_box)
        self.save_btn.clicked.connect(self.save_clicked)

        self.show()

    def save_clicked(self):
        self.data_dict['system_id'] = self.xitongbianhao_line.text()
        self.data_dict['system_account'] = self.xitongzhanghao_line.text()
        self.data_dict['system_password'] = self.xitongmima_line.text()
        print(self.data_dict)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    add_database = SystemAddDataBase()
    sys.exit(add_database.exec_())
