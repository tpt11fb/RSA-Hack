#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 15:02
# @Author : Tptfb11
# @File : RsaAttack.py
# @Software : PyCharm
# 密文：704796792
# 公钥：{920139713,19}
# 920139713质因数分解：18443×49891：即p,q分别为18443,49891
import sys
from untitled import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Attack import wienerHacker, djmzs
from Attack import dpDivulge

class ShowGui(QMainWindow,Ui_Dialog):
    def __init__(self,parent=None):
        super(ShowGui,self).__init__(parent)
        self.setupUi(self)
        # 设置不可点击
        self.pushButton.setEnabled(False)
        # 监听下拉选项
        self.comboBox.currentIndexChanged.connect(self.selectMethods)
        # 重置按钮
        self.pushButton_2.clicked.connect(self.initcontent)

    # 监听下拉选项的函数
    def selectMethods(self):
        selectMethod = self.comboBox.currentText()
        if selectMethod == "基于连分数的Wiener攻击":
            print("======基于连分数的Wiener攻击======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            self.lineEdit_2.setPlaceholderText("请输入参数e")
            self.lineEdit_4.setPlaceholderText("请输入参数n")
            # 点击Hack, 调用clickHack函数
            self.pushButton.clicked.connect(self.clickHackWiener)
            return

        elif selectMethod == "dp泄露":
            print("======dp泄露======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            self.plainTextEdit.setPlaceholderText("请输入密文")
            self.lineEdit_2.setPlaceholderText("请输入参数e")
            self.lineEdit_4.setPlaceholderText("请输入参数n")
            self.lineEdit_5.setPlaceholderText("请输入参数dp")
            self.pushButton.clicked.connect(self.clickHackdp)
            return

        elif selectMethod == "dp和dq泄露":
            print("======dp和dq泄露======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            self.lineEdit.setPlaceholderText("请输入参数p")
            self.lineEdit_3.setPlaceholderText("请输入参数q")
            self.lineEdit_5.setPlaceholderText("请输入参数dp")
            self.lineEdit_6.setPlaceholderText("请输入参数dq")
            self.plainTextEdit.setPlaceholderText("请输入密文")
            self.pushButton.clicked.connect(self.clickHackdpdq)
            return

        elif selectMethod == "共模攻击":
            print("======共模攻击======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            return


        elif selectMethod == "低加密指数攻击":
            print("======低加密指数攻击======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            self.lineEdit_2.setPlaceholderText("请输入参数e")
            self.lineEdit_4.setPlaceholderText("请输入参数n")
            self.plainTextEdit.setPlaceholderText("请输入密文")
            self.pushButton.clicked.connect(self.clickHackdjmzs)
            return

        elif selectMethod == "gcd去求解共同的素因子q":
            print("======gcd去求解共同的素因子q======")
            self.initcontent()
            self.pushButton.setEnabled(True)
            return
        else:
            print("======请选择攻击方式======")
            self.initcontent()
            self.pushButton.setEnabled(False)
            return

    # 调用 Wiener攻击
    def clickHackWiener(self):
        e = self.lineEdit_2.text()
        n = self.lineEdit_4.text()
        if self.plainTextEdit.toPlainText() != None:
            res = wienerHacker.wienerAttack(int(e), int(n))
            QMessageBox.information(self, "结果", f"私钥d={res}",
                                    QMessageBox.Yes)
        else:
            res = wienerHacker.wienerAttack(int(e),int(n))
            QMessageBox.information(self, "错误", f"{res}",
                                    QMessageBox.Yes)

    # 调用 dp泄露
    def clickHackdp(self):
        e = self.lineEdit_2.text()
        n = self.lineEdit_4.text()
        dp = self.lineEdit_5.text()
        c = self.plainTextEdit.toPlainText()
        if self.plainTextEdit.toPlainText() != None:
            try:
                res = dpDivulge.action(int(e), int(n), int(c), int(dp))
                if res == "此方法不适用":
                    QMessageBox.information(self, "结果", f"{res}",
                                        QMessageBox.Yes)
                self.plainTextEdit_2.setPlainText(str(res))
            except:
                QMessageBox.information(self, "结果", "请输入整数",
                                        QMessageBox.Yes)
        else:
            QMessageBox.information(self, "错误", f"请输入密文",
                                    QMessageBox.Yes)
    # 调用 dp,dq泄露
    def clickHackdpdq(self):

        return
    # 调用 gcd攻击
    def clickHackgcd(self):

        return
    # 调用 共模攻击
    def clickHackgm(self):

        return
    # 调用 低加密指数攻击，e过于小
    def clickHackdjmzs(self):
        e = self.lineEdit_2.text()
        n = self.lineEdit_4.text()
        c = self.plainTextEdit.toPlainText()
        if self.plainTextEdit.toPlainText() != None:
            res = djmzs.action(int(e), int(n), int(c))
            self.plainTextEdit_2.setPlainText(str(res))
        else:
            QMessageBox.information(self, "错误", f"请输入密文",
                                    QMessageBox.Yes)
        return

    # 初始化 组件
    def initcontent(self):
        self.pushButton.setEnabled(False)
        # 文本内容
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")
        # 背景提示
        self.lineEdit.setPlaceholderText("")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_6.setPlaceholderText("")
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit_2.setPlaceholderText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ShowGui()
    ui.show()
    sys.exit(app.exec_())