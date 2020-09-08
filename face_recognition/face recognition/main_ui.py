# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 547)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setMinimumSize(QtCore.QSize(640, 360))
        self.video_label.setMaximumSize(QtCore.QSize(640, 360))
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.verticalLayout.addWidget(self.video_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.id_line = QtWidgets.QLineEdit(self.centralwidget)
        self.id_line.setObjectName("id_line")
        self.horizontalLayout_2.addWidget(self.id_line, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.camera_button.setObjectName("camera_button")
        self.verticalLayout_2.addWidget(self.camera_button)
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        self.register_button.setEnabled(False)
        self.verticalLayout_2.addWidget(self.register_button)
        self.recognize_button = QtWidgets.QPushButton(self.centralwidget)
        self.recognize_button.setObjectName("recognize_button")
        self.recognize_button.setEnabled(False)
        self.verticalLayout_2.addWidget(self.recognize_button)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "学生姓名："))
        self.label_3.setText(_translate("MainWindow", "学生学号："))
        self.camera_button.setText(_translate("MainWindow", "打开摄像头"))
        self.register_button.setText(_translate("MainWindow", "录入"))
        self.recognize_button.setText(_translate("MainWindow", "检测"))


