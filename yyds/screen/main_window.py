# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_3.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 12pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.current_username_label = QtWidgets.QLabel(self.centralwidget)
        self.current_username_label.setMinimumSize(QtCore.QSize(70, 0))
        self.current_username_label.setStyleSheet("font: 12pt \"宋体\";")
        self.current_username_label.setText("")
        self.current_username_label.setObjectName("current_username_label")
        self.horizontalLayout.addWidget(self.current_username_label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setStyleSheet("font: 12pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.current_role_label = QtWidgets.QLabel(self.centralwidget)
        self.current_role_label.setMinimumSize(QtCore.QSize(50, 0))
        self.current_role_label.setStyleSheet("font: 12pt \"宋体\";")
        self.current_role_label.setText("")
        self.current_role_label.setObjectName("current_role_label")
        self.horizontalLayout.addWidget(self.current_role_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.version_lable = QtWidgets.QLabel(self.centralwidget)
        self.version_lable.setMinimumSize(QtCore.QSize(100, 0))
        self.version_lable.setObjectName("version_lable")
        self.horizontalLayout.addWidget(self.version_lable)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("font: 12pt \"宋体\";")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.main_hbox = QtWidgets.QHBoxLayout()
        self.main_hbox.setObjectName("main_hbox")
        self.tabListWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabListWidget.sizePolicy().hasHeightForWidth())
        self.tabListWidget.setSizePolicy(sizePolicy)
        self.tabListWidget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tabListWidget.setObjectName("tabListWidget")
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tabListWidget.addItem(item)
        self.main_hbox.addWidget(self.tabListWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_hbox.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sel_label = QtWidgets.QLabel(self.centralwidget)
        self.sel_label.setMinimumSize(QtCore.QSize(80, 0))
        self.sel_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.sel_label.setObjectName("sel_label")
        self.gridLayout_2.addWidget(self.sel_label, 2, 6, 1, 1)
        self.selAllCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.selAllCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selAllCheckBox.setObjectName("selAllCheckBox")
        self.gridLayout_2.addWidget(self.selAllCheckBox, 2, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 2, 3, 5, 1)
        self.clearPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearPushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.clearPushButton.setObjectName("clearPushButton")
        self.gridLayout_2.addWidget(self.clearPushButton, 2, 5, 1, 1)
        self.refreshPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshPushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.refreshPushButton.setObjectName("refreshPushButton")
        self.gridLayout_2.addWidget(self.refreshPushButton, 2, 1, 1, 1)
        self.selectListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.selectListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectListWidget.setToolTip("")
        self.selectListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selectListWidget.setObjectName("selectListWidget")
        self.gridLayout_2.addWidget(self.selectListWidget, 5, 4, 1, 4)
        self.typComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.typComboBox.setMinimumSize(QtCore.QSize(85, 0))
        self.typComboBox.setObjectName("typComboBox")
        self.typComboBox.addItem("")
        self.typComboBox.addItem("")
        self.typComboBox.addItem("")
        self.gridLayout_2.addWidget(self.typComboBox, 2, 0, 1, 1)
        self.rowListFilterEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rowListFilterEdit.setObjectName("rowListFilterEdit")
        self.gridLayout_2.addWidget(self.rowListFilterEdit, 3, 0, 1, 3)
        self.SelectListFilterEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SelectListFilterEdit.setObjectName("SelectListFilterEdit")
        self.gridLayout_2.addWidget(self.SelectListFilterEdit, 3, 4, 1, 4)
        self.rawListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.rawListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rawListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rawListWidget.setObjectName("rawListWidget")
        self.gridLayout_2.addWidget(self.rawListWidget, 5, 0, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.main_hbox.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.main_hbox.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.main_hbox.addLayout(self.verticalLayout_2)
        self.main_hbox.setStretch(0, 1)
        self.main_hbox.setStretch(1, 3)
        self.main_hbox.setStretch(2, 3)
        self.main_hbox.setStretch(4, 5)
        self.gridLayout.addLayout(self.main_hbox, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "启动和管理窗口"))
        self.label_2.setText(_translate("MainWindow", "用户:"))
        self.label_4.setText(_translate("MainWindow", " 角色:"))
        self.version_lable.setText(_translate("MainWindow", "版本号"))
        self.exitButton.setText(_translate("MainWindow", "登出"))
        __sortingEnabled = self.tabListWidget.isSortingEnabled()
        self.tabListWidget.setSortingEnabled(False)
        item = self.tabListWidget.item(0)
        item.setText(_translate("MainWindow", "启动"))
        item = self.tabListWidget.item(1)
        item.setText(_translate("MainWindow", "消息群发"))
        item = self.tabListWidget.item(2)
        item.setText(_translate("MainWindow", "定时回复"))
        item = self.tabListWidget.item(3)
        item.setText(_translate("MainWindow", "自动回复"))
        item = self.tabListWidget.item(4)
        item.setText(_translate("MainWindow", "智能AI聊天"))
        item = self.tabListWidget.item(5)
        item.setText(_translate("MainWindow", "群管理"))
        item = self.tabListWidget.item(6)
        item.setText(_translate("MainWindow", "基础设置"))
        item = self.tabListWidget.item(7)
        item.setText(_translate("MainWindow", "关于"))
        self.tabListWidget.setSortingEnabled(__sortingEnabled)
        self.sel_label.setText(_translate("MainWindow", "联系人0"))
        self.selAllCheckBox.setText(_translate("MainWindow", "全选"))
        self.clearPushButton.setText(_translate("MainWindow", "清空"))
        self.refreshPushButton.setText(_translate("MainWindow", "数据刷新"))
        self.typComboBox.setItemText(0, _translate("MainWindow", "所有联系人"))
        self.typComboBox.setItemText(1, _translate("MainWindow", "选择群"))
        self.typComboBox.setItemText(2, _translate("MainWindow", "选择好友"))
        self.rowListFilterEdit.setPlaceholderText(_translate("MainWindow", "结果过滤"))
        self.SelectListFilterEdit.setPlaceholderText(_translate("MainWindow", "待操作联系人过滤"))
