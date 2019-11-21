"""
主窗口界面
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from DataBaseInformationSystem.SystemGui.shetuanxinxiGUI import TableShetuanInfo
from DataBaseInformationSystem.SystemGui.caiwuguanliGUI import TableCaiWuInfo
from DataBaseInformationSystem.SystemGui.sheyuanGUI import TableSheYuanInfo
from DataBaseInformationSystem.SystemGui.huodongGUI import TableHuoDongInfo
from DataBaseInformationSystem.SystemGui.shetuantuanzhangGUI import TableSheTuanTuanZhangInfo
from DataBaseInformationSystem.SystemGui.hezuodanweiGUI import TableHeZuoInfo
from DataBaseInformationSystem.SystemGui.teacherGUI import TableZhidaoTeacherInfo
from DataBaseInformationSystem.SystemGui.systemGUI import TableSystemInfo


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.init_GUI()

    def init_GUI(self):
        self.shetuaninfo_btn = QPushButton('社团信息', self)
        self.zhibaninfo_btn = QPushButton('系统信息管理', self)
        self.caiwuinfo_btn = QPushButton('财务管理', self)
        self.shetuantuanzhanginfo_btn = QPushButton('社团团长信息', self)
        self.sheyuaninfo_btn = QPushButton('社员信息', self)
        self.hezuodanwei_btn = QPushButton('合作单位', self)
        self.huodonginfo_btn = QPushButton('活动信息', self)
        self.zhidaoteach_btn = QPushButton('指导老师', self)

        self.mainlbl = QLabel('信息管理系统', self)
        self.mainlbl.resize(80, 40)
        self.mainlbl.move((self.width() - self.mainlbl.width() / 2),
                          (self.height() - self.mainlbl.height()) / 2)
        self.mainlbl.setAlignment(Qt.AlignCenter)
        self.v_layout = QVBoxLayout()
        self.gridlayout = QGridLayout()
        self.gridlayout.setSpacing(20)
        self.gridlayout.addWidget(self.shetuaninfo_btn, 1, 0)
        self.gridlayout.addWidget(self.zhibaninfo_btn, 1, 1)
        self.gridlayout.addWidget(self.caiwuinfo_btn, 2, 0)
        self.gridlayout.addWidget(self.shetuantuanzhanginfo_btn, 2, 1)
        self.gridlayout.addWidget(self.sheyuaninfo_btn, 3, 0)
        self.gridlayout.addWidget(self.hezuodanwei_btn, 3, 1)
        self.gridlayout.addWidget(self.huodonginfo_btn, 4, 0)
        self.gridlayout.addWidget(self.zhidaoteach_btn, 4, 1)

        self.v_layout.addWidget(self.mainlbl)
        self.v_layout.addLayout(self.gridlayout)

        self.setLayout(self.v_layout)
        self.desktopRect = QApplication.desktop().screenGeometry()
        self.resize(500, 400)
        self.position_centerx = QApplication.desktop().width() - self.width()
        self.position_centery = QApplication.desktop().height() - self.height()
        self.move(self.position_centerx / 2, self.position_centery / 2)

        self.btn_method()

    def btn_method(self):
        self.shetuaninfo_btn.clicked.connect(self.shetuanxinxi_show)
        self.caiwuinfo_btn.clicked.connect(self.caiwuxinxi_show)
        self.sheyuaninfo_btn.clicked.connect(self.sheyuanxinxi_show)
        self.huodonginfo_btn.clicked.connect(self.huodongxinxi_show)
        self.shetuantuanzhanginfo_btn.clicked.connect(self.shetuantuanzhang_show)
        self.hezuodanwei_btn.clicked.connect(self.hezuodanwei_show)
        self.zhidaoteach_btn.clicked.connect(self.zhidaolaoshi_show)
        self.zhibaninfo_btn.clicked.connect(self.xitongguanli_show)

    def shetuanxinxi_show(self):
        self.shetuanxinxi_ = TableShetuanInfo()
        self.shetuanxinxi_.show()

    def caiwuxinxi_show(self):
        self.caiwuxinxi_ = TableCaiWuInfo()
        self.caiwuxinxi_.show()

    def sheyuanxinxi_show(self):
        self.sheyuanxinxi_ = TableSheYuanInfo()
        self.sheyuanxinxi_.show()

    def huodongxinxi_show(self):
        self.huodongxinxi_ = TableHuoDongInfo()
        self.huodongxinxi_.show()

    def xitongguanli_show(self):
        self.system_ = TableSystemInfo()
        self.system_.show()

    def shetuantuanzhang_show(self):
        self.shetuantuanzhangxinxi_ = TableSheTuanTuanZhangInfo()
        self.shetuantuanzhangxinxi_.show()

    def hezuodanwei_show(self):
        self.hezuodanwei_ = TableHeZuoInfo()
        self.hezuodanwei_.show()

    def zhidaolaoshi_show(self):
        self.zhidaolaoshi_ = TableZhidaoTeacherInfo()
        self.zhidaolaoshi_.show()

    def close(self):
        self.shetuanxinxi_.close()
        self.caiwuxinxi_.close()
        self.sheyuanxinxi_.close()
        self.huodongxinxi_.close()
        self.shetuantuanzhangxinxi_.close()
        self.hezuodanwei_.close()
        self.zhidaolaoshi_.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MainWin()
    mainwin.show()
    sys.exit(app.exec_())
