# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyProjects\MotdDyn\UI\motd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 147)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setTextFormat(QtCore.Qt.PlainText)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.lblMensaje = QtWidgets.QLabel(self.centralwidget)
        self.lblMensaje.setWordWrap(True)
        self.lblMensaje.setObjectName("lblMensaje")
        self.verticalLayout.addWidget(self.lblMensaje)
        self.lblTitular = QtWidgets.QLabel(self.centralwidget)
        self.lblTitular.setObjectName("lblTitular")
        self.verticalLayout.addWidget(self.lblTitular)
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setWordWrap(True)
        self.lblUsuario.setObjectName("lblUsuario")
        self.verticalLayout.addWidget(self.lblUsuario)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitulo.setText(_translate("MainWindow", "Ofrece FULL CLARO"))
        self.lblMensaje.setText(_translate("MainWindow", "Sr. Juan, usted cuenta con el beneficio de FULL CLARO el cual le brinda hasta el 50% de su velocidad contratada TOTALMENTE GRATIS."))
        self.lblTitular.setText(_translate("MainWindow", "- Si es TITULAR realizar esta pregunta: ¿Lo activamos en su servicio fijo o movil?"))
        self.lblUsuario.setText(_translate("MainWindow", "- Si es USUARIO recordarle que debe comunicarse el titular del servicio para activar este beneficio!!!"))


