import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from UI.UI_motd import Ui_MainWindow


class MainW(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_salir = False
        self.oldPos = self.pos()
        # self.lblMensaje.setStyleSheet("QLabel { color: #64de64; }")
        self.lblTitulo.setStyleSheet("QLabel { color: red; }")
        self.lblTitulo.setFont(QtGui.QFont("Arial Black", 25, QtGui.QFont.Bold))
        self.lblMensaje.setStyleSheet("QLabel { color: blue; }")
        self.lblMensaje.setFont(QtGui.QFont("Arial Black", 10, QtGui.QFont.Bold))
        self.lblTitular.setStyleSheet("QLabel { color: blue; }")
        self.lblTitular.setFont(QtGui.QFont("Arial Black", 10, QtGui.QFont.Bold))
        self.lblUsuario.setStyleSheet("QLabel { color: blue; }")
        self.lblUsuario.setFont(QtGui.QFont("Arial Black", 10, QtGui.QFont.Bold))
        salir = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Alt+Shift+Q"), self)
        salir.activated.connect(self.salir)

    def salir(self):
        self.flag_salir = True
        # print("salir")
        sys.exit()

    def closeEvent(self, event):
        if not self.flag_salir:
            event.ignore()
            print("Intento Salir")
        # self.setWindowState(QtCore.Qt.WindowMinimized)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        # print(str(event.globalPos()))
        y = QtWidgets.QDesktopWidget().screenGeometry().height()
        x = QtWidgets.QDesktopWidget().screenGeometry().width()

        # print(self.geometry().x())
        if self.geometry().x() < -80:
            self.move(self.geometry().x() + self.width(), self.geometry().y())
            # self.move(60, self.geometry().y())
        if self.geometry().x() > x - self.width() + 80:
            self.move(self.geometry().x() - self.width(), self.geometry().y())

        if self.geometry().y() < -(self.height()*0.45):
            self.move(self.geometry().x(), self.geometry().y() + self.height())
        if self.geometry().y() > y - self.height() + (self.height() * 0.45):
            self.move(self.geometry().x(), self.geometry().y() - self.height())

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainW()
    myapp.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
    # myapp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    myapp.setWindowOpacity(0.7)
    myapp.show()
    sys.exit(app.exec_())
