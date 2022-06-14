#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 22:23
# @Author : Tptfb11
# @File : test.py
# @Software : PyCharm
import sys
from untitled import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QMainWindow
from Attack import wienerHacker

class ShowGui(QMainWindow,Ui_Dialog):
    def __init__(self,parent=None):
        super(ShowGui,self).__init__(parent)
        self.setupUi(self)
        # 点击Hack, 调用clickHack
        self.pushButton.clicked.connect(self.clickHack)

    def clickHack(self):
        res = 1
        self.plainTextEdit_2.setPlainText("res")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ShowGui()
    ui.show()
    sys.exit(app.exec_())