# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistaDoctor import Ui_MainWindowDoc
import socket
import re
import datetime



class Ui_MainWindow(object):

    def openMain(self):

        self.window = QtWidgets.QMainWindow()
        self.UI = Ui_MainWindowDoc()
        self.UI.setupUi(self.window)
        self.UI.usuario = self.usuario.text()
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 146)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario.setObjectName("usuario")
        self.verticalLayout_2.addWidget(self.usuario)
        self.contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasena.setObjectName("contrasena")
        self.verticalLayout_2.addWidget(self.contrasena)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 241, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Usuario:"))
        self.label_2.setText(_translate("MainWindow", "Contraseña:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(self.clickLogin)

    def popUpCritical(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()


    def clickLogin(self):
        user =  self.usuario.text()
        print(user)
        contra =  self.contrasena.text()
        print(contra)

        if (len(user) and len(user) > 0):
            input1 = user + "/" + contra
            print(input1)
            inputLen = len(input1)

            inputLenStr = '{:05d}'.format(inputLen)

            message = inputLenStr + 'login' + input1

            # Convert the message string to bytes just before sending
            message_bytes = message.encode('utf-8')

            sock.sendall(message_bytes)

            amount_received = 0
            amount_expected = int(sock.recv(5))

            while amount_received < amount_expected:
                data = sock.recv(amount_expected - amount_received)
                amount_received += len(data)

            print("Processing ...")
            resp = '{:05d}'.format(len(data)) + data.decode('utf-8')
            print(resp)

            respSize = resp[0:5]
            respSizeInt = int(respSize)
            respCode = resp[12:14]

            if respCode == 'OK':

                self.openMain()
                MainWindow.close()


                
            else: self.popUpCritical("Usuario o Contraseña no valido")





if __name__ == "__main__":
    import sys


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print('Connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    print('Connected successfully')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
