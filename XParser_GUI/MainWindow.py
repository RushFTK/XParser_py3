# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 304, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_tips_quickstart = QtWidgets.QLabel(self.layoutWidget)
        self.label_tips_quickstart.setObjectName("label_tips_quickstart")
        self.verticalLayout.addWidget(self.label_tips_quickstart)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_tips_targetwebsite = QtWidgets.QLabel(self.layoutWidget)
        self.label_tips_targetwebsite.setObjectName("label_tips_targetwebsite")
        self.horizontalLayout.addWidget(self.label_tips_targetwebsite)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_quickstartanalyze = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_quickstartanalyze.setObjectName("pushButton_quickstartanalyze")
        self.horizontalLayout.addWidget(self.pushButton_quickstartanalyze)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_tips_quickstart_options = QtWidgets.QLabel(self.layoutWidget1)
        self.label_tips_quickstart_options.setObjectName("label_tips_quickstart_options")
        self.verticalLayout_2.addWidget(self.label_tips_quickstart_options)
        self.checkBox_dontanalyzestructer = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_dontanalyzestructer.setObjectName("checkBox_dontanalyzestructer")
        self.verticalLayout_2.addWidget(self.checkBox_dontanalyzestructer)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_analyzedeeper = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_analyzedeeper.setObjectName("checkBox_analyzedeeper")
        self.horizontalLayout_2.addWidget(self.checkBox_analyzedeeper)
        self.lineEdit_analyzedeeper = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_analyzedeeper.setObjectName("lineEdit_analyzedeeper")
        self.horizontalLayout_2.addWidget(self.lineEdit_analyzedeeper)
        self.label_tips_analyzedeeper_unit = QtWidgets.QLabel(self.layoutWidget1)
        self.label_tips_analyzedeeper_unit.setObjectName("label_tips_analyzedeeper_unit")
        self.horizontalLayout_2.addWidget(self.label_tips_analyzedeeper_unit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_showlogdialog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_showlogdialog.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.pushButton_showlogdialog.setObjectName("pushButton_showlogdialog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_helpmenu = QtWidgets.QAction(MainWindow)
        self.action_helpmenu.setObjectName("action_helpmenu")
        self.action_checkupdate = QtWidgets.QAction(MainWindow)
        self.action_checkupdate.setObjectName("action_checkupdate")
        self.actionbegin = QtWidgets.QAction(MainWindow)
        self.actionbegin.setObjectName("actionbegin")
        self.menu_F.addAction(self.actionbegin)
        self.menu_H.addAction(self.action_helpmenu)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_checkupdate)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_about)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_tips_quickstart.setText(_translate("MainWindow", "快速开始:"))
        self.label_tips_targetwebsite.setText(_translate("MainWindow", "待测网站"))
        self.pushButton_quickstartanalyze.setText(_translate("MainWindow", "开始"))
        self.label_tips_quickstart_options.setText(_translate("MainWindow", "快速开始选项"))
        self.checkBox_dontanalyzestructer.setText(_translate("MainWindow", "不分析网页结构"))
        self.checkBox_analyzedeeper.setText(_translate("MainWindow", "自定义分析网页层数："))
        self.label_tips_analyzedeeper_unit.setText(_translate("MainWindow", "层"))
        self.pushButton_showlogdialog.setText(_translate("MainWindow", "显示日志窗口(&L)"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.action_about.setText(_translate("MainWindow", "关于(&A)"))
        self.action_helpmenu.setText(_translate("MainWindow", "XParser帮助(&T)"))
        self.action_checkupdate.setText(_translate("MainWindow", "检查更新(&C)"))
        self.actionbegin.setText(_translate("MainWindow", "开始一项漏洞测试..."))

