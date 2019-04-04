# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyProjects\MotdDyn\UI\motd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 74)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMensaje = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lblMensaje.setFont(font)
        self.lblMensaje.setTextFormat(QtCore.Qt.PlainText)
        self.lblMensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensaje.setObjectName("lblMensaje")
        self.verticalLayout.addWidget(self.lblMensaje)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblMensaje.setText(_translate("MainWindow", "Ofrece FULL CLARO"))

