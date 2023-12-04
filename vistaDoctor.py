from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket
import re
import datetime
from vistaRecetas import Ui_vistaRecetas
from camasUI import Ui_Camas

from unidecode import unidecode

def remove_tildes(input_string):
    # Use unidecode to remove tildes and other diacritic marks
    return unidecode(input_string)


def format_chilean_rut(rut):
    if len (rut) == 0:
        return "Invalid Rut"
    
    rut = rut.replace(".", "").replace("-", "").upper()  # Remove separators and convert to uppercase
    
    if len(rut) < 2 or not rut[:-1].isdigit():
        return "Invalid Rut"

    rut_number = rut[:-1].zfill(8)  # Pad with zeros if there are only 8 digits
    verification_digit = rut[-1]

    calculated_verification = 0
    multiplier = 2
    for digit in reversed(rut_number):
        calculated_verification += int(digit) * multiplier
        multiplier += 1
        if multiplier > 7:
            multiplier = 2

    remainder = calculated_verification % 11
    computed_digit = 11 - remainder if remainder != 0 else 0

    if computed_digit == 10:
        computed_digit = 'K'

    if str(computed_digit) == verification_digit:
        formatted_rut = f"{rut_number}-{computed_digit}"
        return formatted_rut
    else:
        return "Invalid Rut"

class Ui_MainWindowDoc(object):

    lastRut = "Invalid Rut"
    usuario = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print('Connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    print('Connected successfully')
    

    
    def openRecetas(self):


        if self.lastRut != "Invalid Rut":
            self.window = QtWidgets.QMainWindow()
            self.UI = Ui_vistaRecetas()
            self.UI.setupUi(self.window)
            self.UI.label_2.setText("Rut: " + self.lastRut)
            self.UI.label.setText(self.nombrePaciente.text())
            self.window.show()
        else: self.popUpCritical("Ingrese un rut valido antes de visualizar recetas")

    def openCamas(self):



        if self.lastRut != "Invalid Rut":

            self.window = QtWidgets.QMainWindow()
            self.UI2 = Ui_Camas()
            self.UI2.setupUi(self.window)
            self.UI2.rutLabel.setText("Rut: " + self.lastRut)
            self.UI2.salaPaciente.setText(self.label.text())
            self.UI2.nombrePaciente.setText(self.nombrePaciente.text())
            
            self.window.show()

        else: self.popUpCritical("Ingrese un rut valido antes de visualizar el menú de hospitalizacion")







    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 20, 20, 15)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rutLabel = QtWidgets.QLabel(self.centralwidget)
        self.rutLabel.setObjectName("rutLabel")
        self.horizontalLayout.addWidget(self.rutLabel)
        self.inputRutPaciente = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRutPaciente.setObjectName("inputRutPaciente")
        self.horizontalLayout.addWidget(self.inputRutPaciente)
        self.buscarFicha = QtWidgets.QPushButton(self.centralwidget)
        self.buscarFicha.setObjectName("buscarFicha")
        self.horizontalLayout.addWidget(self.buscarFicha)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nombrePaciente = QtWidgets.QLabel(self.centralwidget)
        self.nombrePaciente.setObjectName("nombrePaciente")
        self.horizontalLayout_2.addWidget(self.nombrePaciente)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tablaFichas = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaFichas.setObjectName("tablaFichas")
        self.tablaFichas.setColumnCount(2)
        self.tablaFichas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaFichas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaFichas.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tablaFichas)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.textoObservaciones = QtWidgets.QTextEdit(self.centralwidget)
        self.textoObservaciones.setObjectName("textoObservaciones")
        self.verticalLayout.addWidget(self.textoObservaciones)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.botonAgregarObservaciones = QtWidgets.QPushButton(self.centralwidget)
        self.botonAgregarObservaciones.setObjectName("botonAgregarObservaciones")
        self.horizontalLayout_3.addWidget(self.botonAgregarObservaciones)
        self.botonAbrirRecetas = QtWidgets.QPushButton(self.centralwidget)
        self.botonAbrirRecetas.setObjectName("botonAbrirRecetas")
        self.horizontalLayout_3.addWidget(self.botonAbrirRecetas)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
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
        self.rutLabel.setText(_translate("MainWindow", "Rut: "))
        self.inputRutPaciente.setPlaceholderText(_translate("MainWindow", "12345678-9"))
        self.buscarFicha.setText(_translate("MainWindow", "Buscar"))
        self.nombrePaciente.setText(_translate("MainWindow", "Nombre: "))
        self.label.setText(_translate("MainWindow", "Sala: "))
        self.label_5.setText(_translate("MainWindow", "Ficha Medica:"))
        item = self.tablaFichas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tablaFichas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Texto"))
        self.label_6.setText(_translate("MainWindow", "Agregar Observaciones:"))
        self.botonAgregarObservaciones.setText(_translate("MainWindow", "Agregar"))
        self.botonAbrirRecetas.setText(_translate("MainWindow", "Ver Recetas"))
        self.pushButton.setText(_translate("MainWindow", "Hospitalización"))

        self.buscarFicha.clicked.connect(self.buscarFichaFunc)
        self.botonAgregarObservaciones.clicked.connect(self.agregarObsFunc)
        self.botonAbrirRecetas.clicked.connect(self.openRecetas)
        self.pushButton.clicked.connect(self.openCamas)

    def popUpAlert(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
    
    def popUpInfo(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


    
    def popUpCritical(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()


    def dataPacienteFunc(self):
        sock = self.sock
        rut = self.inputRutPaciente.text()
        rut = format_chilean_rut(rut)
        self.lastRut = rut
        input1 = "DP" + rut
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'ficha' + input1

        # Convert the message string to bytes just before sending
        message_bytes = message.encode('utf-8')

        print(message)

        sock.sendall(message_bytes)

        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)

        print("Processing ...")
        resp = '{:05d}'.format(len(data)) + data.decode('utf-8')

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[10:12]

        print(resp[12:len(resp)])
        print("\n")

        if respCode == 'OK':
             
            if len(resp[12:len(resp)]) == 0:
                    self.popUpAlert("No se encuentran fichas para este paciente")

            else:
                    split_values = resp[12:len(resp)].split('/')
                    self.nombrePaciente.setText("Nombre Paciente: " + split_values[0] + " " + split_values[1] + " " + split_values[2]) 
                    print(split_values[3])
                    print(str(split_values[3]))

                    if str(split_values[3]) == "0":
                        self.label.setText("Sala: No internado")
                    
                    else: self.label.setText("Sala: " + split_values[4] + ", Cama:" + split_values[3])
        else:

            print(f"{rut} no es valido.")
            self.popUpCritical("El Rut ingresado no es valido")


                        
                

    def buscarFichaFunc(self):
        sock = self.sock
        rut = self.inputRutPaciente.text()
        print(rut)
        rut = format_chilean_rut(rut)
        self.lastRut = rut
    



        if rut != "Invalid Rut":

            print(f"{rut} Valido.")

            input1 = "FP" + rut
            inputLen = len(input1)

            # Format the length with leading zeros to make it 5 digits
            inputLenStr = '{:05d}'.format(inputLen)

            message = inputLenStr + 'ficha' + input1

            # Convert the message string to bytes just before sending
            message_bytes = message.encode('utf-8')

            print(message)

            sock.sendall(message_bytes)

            amount_received = 0
            amount_expected = int(sock.recv(5))

            while amount_received < amount_expected:
                data = sock.recv(amount_expected - amount_received)
                amount_received += len(data)

            print("Processing ...")
            print(data)
            resp = '{:05d}'.format(len(data)) + data.decode('utf-8')

            respSize = resp[0:5]
            respSizeInt = int(respSize)
            respCode = resp[10:12]

            print(resp[12:len(resp)])
            print("\n")

            if respCode == 'OK':


                if len(resp[12:len(resp)]) == 0:
                    self.popUpAlert("No se encuentran fichas para este paciente")

                else:
                    self.dataPacienteFunc()
                    split_values = resp[12:len(resp)].split('/')

                    print (split_values)

                    # Process individual strings
                    array_of_arrays = []

                    for value in split_values:

                        valueSplit = value[1:len(value)-1].split("), ")

                        print(value)

                        fecha = valueSplit[0] + ")"
                        print(fecha)
                        fecha = eval(fecha)
                        print(fecha)

                        formatted_date = fecha.strftime("%Y-%m-%d %H:%M:%S")
                        print(formatted_date)
                        texto = valueSplit[1]
                        print(texto)

                        array_of_arrays.append([formatted_date,texto])

                    self.tablaFichas.setRowCount(0)
                    for row_number, row_data in enumerate(array_of_arrays):
                        self.tablaFichas.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            item = QtWidgets.QTableWidgetItem(str(data))
                            self.tablaFichas.setItem(row_number, column_number, item)
                            if column_number == 1:  # Assuming the second column needs to stretch
                                item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)  # Align text left
                                width = len(str(data)) * 10  # Adjust the multiplier to your preference
                                if width > self.tablaFichas.columnWidth(column_number):
                                    self.tablaFichas.setColumnWidth(column_number, width)
            else:
                self.popUpCritical("Ocurrio un error al procesar la solicitud, porfavor intente nuevamente")

        else:
            print(f"{rut} no es valido.")
            self.popUpCritical("Rut no valido")


    def agregarReceta(self):
        sock = self.sock
        rut = self.inputRutPaciente.text()
        print(rut)
        rut = format_chilean_rut(rut)
        self.lastRut = rut

        texto = self.textoObservaciones.toPlainText()
        texto = remove_tildes(texto)
        print(texto)

        texto = texto.replace('/', '|')
        texto = texto.replace('\n', ' ')
        texto = texto.replace(', ', ",")

        print(texto)

        if len(texto) == 0:
            self.popUpAlert("No puede ingresarse una observación vacia")



        elif rut != "Invalid Rut":
            print("Rut Valido")
            input1 = "CF" + rut + "/" + texto
            inputLen = len(input1)

            inputLenStr = '{:05d}'.format(inputLen)

            message = inputLenStr + 'ficha' + input1

            # Convert the message string to bytes just before sending
            message_bytes = message.encode('utf-8')

            print(message)

            sock.sendall(message_bytes)

            amount_received = 0
            amount_expected = int(sock.recv(5))

            while amount_received < amount_expected:
                data = sock.recv(amount_expected - amount_received)
                amount_received += len(data)

            print("Processing ...")
            resp = '{:05d}'.format(len(data)) + data.decode('utf-8')

            respSize = resp[0:5]
            respSizeInt = int(respSize)
            respCode = resp[10:12]

            if respCode == 'OK':


                # Format the current date and time as a string

                current_date = datetime.datetime.now()
                current_date_string = current_date.strftime("%Y-%m-%d %H:%M:%S")

                self.buscarFichaFunc()

                row_position = self.tablaFichas.rowCount()  # Get the current row count
                self.tablaFichas.insertRow(row_position)  # Insert a new row at the end

                # Fill the cells in the newly inserted row (optional)
                self.tablaFichas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(current_date_string))
                self.tablaFichas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(texto))
                
                self.popUpInfo("Entrada agregada exitosamente")
            
        else: self.popUpCritical("Ocurrio un error al ingresar la observación, intente nuevamente")



    def agregarObsFunc(self):
        sock = self.sock
        rut = self.inputRutPaciente.text()
        print(rut)
        rut = format_chilean_rut(rut)
        self.lastRut = rut

        texto = self.textoObservaciones.toPlainText()
        texto = remove_tildes(texto)
        print(texto)

        texto = texto.replace('/', '|')
        texto = texto.replace('\n', ' ')
        texto = texto.replace(', ', ",")

        print(texto)

        if len(texto) == 0:
            self.popUpAlert("No puede ingresarse una observación vacia")



        elif rut != "Invalid Rut":
            print("Rut Valido")
            input1 = "CF" + rut + "/" + texto
            inputLen = len(input1)

            inputLenStr = '{:05d}'.format(inputLen)

            message = inputLenStr + 'ficha' + input1

            # Convert the message string to bytes just before sending
            message_bytes = message.encode('utf-8')

            print(message)

            sock.sendall(message_bytes)

            amount_received = 0
            amount_expected = int(sock.recv(5))

            while amount_received < amount_expected:
                data = sock.recv(amount_expected - amount_received)
                amount_received += len(data)

            print("Processing ...")
            resp = '{:05d}'.format(len(data)) + data.decode('utf-8')

            respSize = resp[0:5]
            respSizeInt = int(respSize)
            respCode = resp[10:12]

            if respCode == 'OK':


                # Format the current date and time as a string

                current_date = datetime.datetime.now()
                current_date_string = current_date.strftime("%Y-%m-%d %H:%M:%S")

                self.buscarFichaFunc()

                row_position = self.tablaFichas.rowCount()  # Get the current row count
                self.tablaFichas.insertRow(row_position)  # Insert a new row at the end

                # Fill the cells in the newly inserted row (optional)
                self.tablaFichas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(current_date_string))
                self.tablaFichas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(texto))
                
                self.popUpInfo("Entrada agregada exitosamente")
            
        else: self.popUpCritical("Ocurrio un error al ingresar la observación, intente nuevamente")


if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowDoc()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
