
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


import socket
import re

def format_chilean_rut(rut):
        if len (rut) == 0:
            return "Invalid Rut"
        
        rut = rut.replace(".", "").replace("-", "").upper()  # Remove separators and convert to uppercase
        
        if len(rut) < 2 or not rut[:-1].isdigit():
            return "Invalid RUT"

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
            return "Invalid RUT"
        


remedios = ["Paracetamol 500mg",
            "Ibuprofeno 400mg",
            "Aspirina 500mg",
            "Loratadina 10mg",
            "Amoxicilina 500mg",
            "Cetirizina 5mg",
            "Diclofenaco 50mg",
            "Ranitidina 150mg",
            "Metformina 850mg",
            "Clonazepam 0.5mg",
            "Atorvastatina 20mg",
            "Prednisona 5mg",
            "Losartán 50mg",
            "Sildenafil 50mg",
            "Metoclopramida 10mg",
            "Levotiroxina 100mcg",
            "Codeína 30mg",
            "Sertralina 50mg",
            "Enalapril 10mg"]

sintomas = ["Dificultad respiratoria severa",
            "Coloracion azul en piel",
            "Frialdad generalizada",
            "Traumatismo severos multiples",
            "Quemaduras en todo el cuerpo",
            "Perdida de miembro u organo",
            "Hemorragia masiva",
            "Trabajo de parte expulsivo",
            "Abuso sexual",
            "Alteracion aguda de signos vitales",
            "Estado convulsivo",
            "Deficiencia respiratoria moderada",
            "Crisis hipertensiva",
            "Diabetes descompesada",
            "Dolor toracico",
            "Trauma severo",
            "Quemadura de tercer grado",
            "Riesgo de perdida de miembro u organo",
            "Fractura",
            "Hemorragia digestiva",
            "Sangrado vaginal en embarazadas",
            "Trabajo de parto",
            "Abuso sexual antiguo",
            "Agitacion psicomotora",
            "Ingestion de sustancias toxicas o envenenamiento",
            "Dolor agudo",
            "Fiebre mayor a 38.5",
            "Vertigo severo",
            "Dificultad respiratoria leve",
            "Vomito y diarrea con deshidratación",
            "Sintomas asociados o dialisis",
            "Dolor moderado de menos de 24 horas",
            "Trauma moderado",
            "Quemadura segundo o primer grado",
            "Sangrado moderado",
            "Reaccion alergica con brote generalizado",
            "Fiebre menor a 38.5",
            "Tos y congestion",
            "Faringitis",
            "Amigdalitis",
            "Vomito",
            "Diarrea sin deshidratacion",
            "Dolor leve",
            "Dolor moderado de mas de 24 horas",
            "Trauma leve",
            "Signos de infeccion local",
            "Ardor al orinar",
            "Enfermedad venerea aguda",
            "Ansiedad y depresion",
            "Colico menstrual",
            "Dolor de cabeza cronico",
            "Tos cronica",
            "Inapetencia",
            "Dolor abdominal cronico",
            "Dolor postraumatico leve",
            "Dermatitis",
            "Estres emocional",
            "Enfermedades cronicas",
            "Formulacion de medicamentos",
            "Lectura de examenes",
            "Diarrea cronica",
            "Estreñimiento"]

class CapitalizeComboBox(QtWidgets.QComboBox):
    def keyPressEvent(self, event):
        # Check if a key press event has occurred
        if event.key() != QtCore.Qt.Key.Key_Return:
            current_text = self.currentText()
            if not current_text:
                # Capitalize the first letter of the typed text
                current_text = event.text().capitalize()
            else:
                # Update the text to maintain capitalization
                current_text = current_text[:self.lineEdit().cursorPosition()] + event.text()
            self.lineEdit().setText(current_text)


class Ui_MainWindow2(object):

    usuario = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print('Connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    print('Connected successfully via funcion temp4')
    
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



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tab_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setStyleSheet("")
        self.tab_2.setObjectName("tab_2")
        self.triage = QtWidgets.QWidget()
        self.triage.setStyleSheet("")
        self.triage.setObjectName("triage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.triage)
        self.verticalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelTriage = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTriage.setFont(font)
        self.labelTriage.setObjectName("labelTriage")
        self.verticalLayout.addWidget(self.labelTriage)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelSintoma1 = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSintoma1.setFont(font)
        self.labelSintoma1.setObjectName("labelSintoma1")
        self.horizontalLayout_4.addWidget(self.labelSintoma1)
        self.boxSintoma1 = QtWidgets.QComboBox(self.triage)
        self.boxSintoma1.setObjectName("boxSintoma1")
        self.horizontalLayout_4.addWidget(self.boxSintoma1)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelSintoma2 = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSintoma2.setFont(font)
        self.labelSintoma2.setObjectName("labelSintoma2")
        self.horizontalLayout_8.addWidget(self.labelSintoma2)
        self.boxSintoma2 = QtWidgets.QComboBox(self.triage)
        self.boxSintoma2.setObjectName("boxSintoma2")
        self.horizontalLayout_8.addWidget(self.boxSintoma2)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelSintoma3 = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSintoma3.setFont(font)
        self.labelSintoma3.setObjectName("labelSintoma3")
        self.horizontalLayout_12.addWidget(self.labelSintoma3)
        self.boxSintoma3 = QtWidgets.QComboBox(self.triage)
        self.boxSintoma3.setObjectName("boxSintoma3")
        self.horizontalLayout_12.addWidget(self.boxSintoma3)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelSintoma4 = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSintoma4.setFont(font)
        self.labelSintoma4.setObjectName("labelSintoma4")
        self.horizontalLayout_11.addWidget(self.labelSintoma4)
        self.boxSintoma3_2 = QtWidgets.QComboBox(self.triage)
        self.boxSintoma3_2.setObjectName("boxSintoma3_2")
        self.horizontalLayout_11.addWidget(self.boxSintoma3_2)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.labelSintoma5 = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSintoma5.setFont(font)
        self.labelSintoma5.setObjectName("labelSintoma5")
        self.horizontalLayout_21.addWidget(self.labelSintoma5)
        self.comboBox_5 = QtWidgets.QComboBox(self.triage)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_21.addWidget(self.comboBox_5)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_29.addLayout(self.verticalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_29.addItem(spacerItem10)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem11)
        self.labelResultadoTriage = QtWidgets.QLabel(self.triage)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelResultadoTriage.setFont(font)
        self.labelResultadoTriage.setObjectName("labelResultadoTriage")
        self.verticalLayout_17.addWidget(self.labelResultadoTriage)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem12)
        self.botonCalcularTriage = QtWidgets.QPushButton(self.triage)
        self.botonCalcularTriage.setObjectName("botonCalcularTriage")
        self.verticalLayout_17.addWidget(self.botonCalcularTriage)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem14)
        self.horizontalLayout_29.addLayout(self.verticalLayout_17)
        self.horizontalLayout_29.setStretch(0, 2)
        self.horizontalLayout_29.setStretch(2, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_29)
        self.tab_2.addTab(self.triage, "")
        self.Agenda = QtWidgets.QWidget()
        self.Agenda.setObjectName("Agenda")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Agenda)
        self.verticalLayout_6.setContentsMargins(25, -1, 25, 12)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBoxHoras = QtWidgets.QToolBox(self.Agenda)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.toolBoxHoras.setFont(font)
        self.toolBoxHoras.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBoxHoras.setStyleSheet("")
        self.toolBoxHoras.setObjectName("toolBoxHoras")
        self.confirmarLlegadaItem = QtWidgets.QWidget()
        self.confirmarLlegadaItem.setGeometry(QtCore.QRect(0, 0, 794, 442))
        self.confirmarLlegadaItem.setStyleSheet("")
        self.confirmarLlegadaItem.setObjectName("confirmarLlegadaItem")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.confirmarLlegadaItem)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelReservas = QtWidgets.QLabel(self.confirmarLlegadaItem)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelReservas.setFont(font)
        self.labelReservas.setObjectName("labelReservas")
        self.horizontalLayout_5.addWidget(self.labelReservas)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.labelRUT = QtWidgets.QLabel(self.confirmarLlegadaItem)
        self.labelRUT.setObjectName("labelRUT")
        self.horizontalLayout_5.addWidget(self.labelRUT)
        self.rutReservas = QtWidgets.QLineEdit(self.confirmarLlegadaItem)
        self.rutReservas.setStyleSheet("background-color: white\n"
"")
        self.rutReservas.setObjectName("rutReservas")
        self.horizontalLayout_5.addWidget(self.rutReservas)
        self.buscarReservas = QtWidgets.QPushButton(self.confirmarLlegadaItem)
        self.buscarReservas.setAutoFillBackground(False)
        self.buscarReservas.setStyleSheet("")
        self.buscarReservas.setObjectName("buscarReservas")
        self.horizontalLayout_5.addWidget(self.buscarReservas)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.tablaReservas = QtWidgets.QTableWidget(self.confirmarLlegadaItem)
        self.tablaReservas.setStyleSheet("background-color: white\n"
"")
        self.tablaReservas.setRowCount(10)
        self.tablaReservas.setColumnCount(6)
        self.tablaReservas.setObjectName("tablaReservas")
        self.horizontalLayout_2.addWidget(self.tablaReservas)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem18)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")


        self.confirmarCita = QtWidgets.QPushButton(self.confirmarLlegadaItem)
        self.confirmarCita.setAutoFillBackground(False)
        self.confirmarCita.setStyleSheet("")
        self.confirmarCita.setObjectName("confirmarCita")
       
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem21New = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem20New = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.horizontalLayout_7.addItem(spacerItem20New)
        self.horizontalLayout_7.addItem(spacerItem21New)
        

        self.horizontalLayout_7.addWidget(self.confirmarCita)
        self.buttonActualzarReservas = QtWidgets.QPushButton(self.confirmarLlegadaItem)
        self.buttonActualzarReservas.setAutoFillBackground(False)
        self.buttonActualzarReservas.setStyleSheet("")
        self.buttonActualzarReservas.setObjectName("buttonActualzarReservas")
        self.horizontalLayout_7.addWidget(self.buttonActualzarReservas)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem21)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem22)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.toolBoxHoras.addItem(self.confirmarLlegadaItem, "")
        self.agendarHoraItem = QtWidgets.QWidget()
        self.agendarHoraItem.setGeometry(QtCore.QRect(0, 0, 794, 442))
        self.agendarHoraItem.setObjectName("agendarHoraItem")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.agendarHoraItem)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.agendarHoraItem)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem24)
        self.calendarioAgenda = QtWidgets.QCalendarWidget(self.agendarHoraItem)
        self.calendarioAgenda.setStyleSheet("QCalendarWidget QWidget{\n"
"\n"
"color: black;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"background-color: rgb(181, 181, 181);\n"
"}\n"
"\n"
"#qt_calendar_monthbutton{\n"
"background-color: rgb(181, 181, 181);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton{\n"
"background-color: rgb(181, 181, 181);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:white;\n"
"color: black;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"background-color: black;\n"
"color: grey;\n"
"}\n"
"#qt_calendar_prevmonth{\n"
"background-color: rgb(181, 181, 181);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"background-color: rgb(181, 181, 181);\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"    background-color: rgb(255, 46, 221);\n"
"}\n"
"\n"
"")
        self.calendarioAgenda.setObjectName("calendarioAgenda")
        self.horizontalLayout_16.addWidget(self.calendarioAgenda)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem25)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(20, 10, 20, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_23 = QtWidgets.QLabel(self.agendarHoraItem)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_14.addWidget(self.label_23)
        self.especialidadAgendarHora = QtWidgets.QComboBox(self.agendarHoraItem)
        self.especialidadAgendarHora.setStyleSheet("background-color: white")
        self.especialidadAgendarHora.setObjectName("especialidadAgendarHora")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.especialidadAgendarHora.addItem("")
        self.horizontalLayout_14.addWidget(self.especialidadAgendarHora)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_new = QtWidgets.QHBoxLayout()
        self.horizontalLayout_new.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_new.setObjectName("horizontalLayout_new")
        self.label_8 = QtWidgets.QLabel(self.agendarHoraItem)
        self.label_8.setObjectName("label_8")
        self.labelRutPacienteAgenda = QtWidgets.QLabel(self.agendarHoraItem)
        self.labelRutPacienteAgenda.setObjectName("label_rut_paciente_agenda")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.horizontalLayout_new.addWidget(self.labelRutPacienteAgenda)
        self.horaAgenda = QtWidgets.QComboBox(self.agendarHoraItem)
        self.horaAgenda.setStyleSheet("background-color: white\n"
"")
        self.horaAgenda.setObjectName("horaAgenda")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.horaAgenda.addItem("")
        self.rutPacienteAgenda = QtWidgets.QLineEdit(self.agendarHoraItem)
        self.rutPacienteAgenda.setStyleSheet("background-color: white\n"
"")
        self.horizontalLayout_13.addWidget(self.horaAgenda)
        self.horizontalLayout_new.addWidget(self.rutPacienteAgenda)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_new)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verDoctoresAgenda = QtWidgets.QPushButton(self.agendarHoraItem)
        self.verDoctoresAgenda.setStyleSheet("")
        self.verDoctoresAgenda.setObjectName("verDoctoresAgenda")
        self.horizontalLayout_15.addWidget(self.verDoctoresAgenda)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16.addLayout(self.verticalLayout_11)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        spacerItem27 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem27)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem28)
        self.tablaAgendarHora = QtWidgets.QTableWidget(self.agendarHoraItem)
        self.tablaAgendarHora.setStyleSheet("background-color: white\n"
"")
        self.tablaAgendarHora.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaAgendarHora.setAlternatingRowColors(True)
        self.tablaAgendarHora.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablaAgendarHora.setRowCount(10)
        self.tablaAgendarHora.setColumnCount(2)
        self.tablaAgendarHora.setObjectName("tablaAgendarHora")
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora.setItem(0, 1, item)
        self.tablaAgendarHora.horizontalHeader().setDefaultSectionSize(135)
        self.tablaAgendarHora.horizontalHeader().setMinimumSectionSize(40)
        self.tablaAgendarHora.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_4.addWidget(self.tablaAgendarHora)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem29)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem30)
        self.botonAgendarHora = QtWidgets.QPushButton(self.agendarHoraItem)
        self.botonAgendarHora.setStyleSheet("")
        self.botonAgendarHora.setObjectName("botonAgendarHora")
        self.horizontalLayout_17.addWidget(self.botonAgendarHora)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem31)
        self.toolBoxHoras.addItem(self.agendarHoraItem, "")
        self.verticalLayout_6.addWidget(self.toolBoxHoras)
        self.tab_2.addTab(self.Agenda, "")
        self.HorarioDoctores = QtWidgets.QWidget()
        self.HorarioDoctores.setObjectName("HorarioDoctores")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.HorarioDoctores)
        self.verticalLayout_12.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_12.setSpacing(16)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_21 = QtWidgets.QLabel(self.HorarioDoctores)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_12.addWidget(self.label_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.HorarioDoctores)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.nombreDoctor = QtWidgets.QLineEdit(self.HorarioDoctores)
        self.nombreDoctor.setStyleSheet("background-color: white\n"
"")
        self.nombreDoctor.setObjectName("nombreDoctor")
        self.horizontalLayout_19.addWidget(self.nombreDoctor)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem32)
        self.buttonFiltrarTablaDoctores = QtWidgets.QPushButton(self.HorarioDoctores)
        self.buttonFiltrarTablaDoctores.setAutoFillBackground(False)
        self.buttonFiltrarTablaDoctores.setStyleSheet("")
        self.buttonFiltrarTablaDoctores.setObjectName("buttonFiltrarTablaDoctores")
        self.horizontalLayout_19.addWidget(self.buttonFiltrarTablaDoctores)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.tablaEspecialistas_3 = QtWidgets.QTableWidget(self.HorarioDoctores)
        self.tablaEspecialistas_3.setStyleSheet("background-color: white\n"
"")
        self.tablaEspecialistas_3.setRowCount(10)
        self.tablaEspecialistas_3.setColumnCount(8)
        self.tablaEspecialistas_3.setObjectName("tablaEspecialistas_3")
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas_3.setHorizontalHeaderItem(7, item)
        self.verticalLayout_12.addWidget(self.tablaEspecialistas_3)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem33)
        self.buttonActualizarDoctores = QtWidgets.QPushButton(self.HorarioDoctores)
        self.buttonActualizarDoctores.setAutoFillBackground(False)
        self.buttonActualizarDoctores.setStyleSheet("")
        self.buttonActualizarDoctores.setObjectName("buttonActualizarDoctores")
        self.horizontalLayout_18.addWidget(self.buttonActualizarDoctores)
        self.verticalLayout_12.addLayout(self.horizontalLayout_18)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem34)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem35)
        self.tab_2.addTab(self.HorarioDoctores, "")
        self.Especialistas = QtWidgets.QWidget()
        self.Especialistas.setObjectName("Especialistas")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Especialistas)
        self.verticalLayout_13.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.Especialistas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_10 = QtWidgets.QLabel(self.Especialistas)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_20.addWidget(self.label_10)
        self.especialidad = QtWidgets.QLineEdit(self.Especialistas)
        self.especialidad.setStyleSheet("background-color: white\n"
"")
        self.especialidad.setObjectName("especialidad")
        self.horizontalLayout_20.addWidget(self.especialidad)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem36)
        self.buscarEspecialistas = QtWidgets.QPushButton(self.Especialistas)
        self.buscarEspecialistas.setAutoFillBackground(False)
        self.buscarEspecialistas.setStyleSheet("")
        self.buscarEspecialistas.setObjectName("buscarEspecialistas")
        self.horizontalLayout_20.addWidget(self.buscarEspecialistas)
        self.verticalLayout_13.addLayout(self.horizontalLayout_20)
        self.tablaEspecialistas = QtWidgets.QTableWidget(self.Especialistas)
        self.tablaEspecialistas.setStyleSheet("background-color: white\n"
"")
        self.tablaEspecialistas.setRowCount(10)
        self.tablaEspecialistas.setColumnCount(3)
        self.tablaEspecialistas.setObjectName("tablaEspecialistas")
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEspecialistas.setHorizontalHeaderItem(2, item)
        self.verticalLayout_13.addWidget(self.tablaEspecialistas)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem37)
        self.actualizarEspecialistas = QtWidgets.QPushButton(self.Especialistas)
        self.actualizarEspecialistas.setAutoFillBackground(False)
        self.actualizarEspecialistas.setStyleSheet("")
        self.actualizarEspecialistas.setObjectName("actualizarEspecialistas")
        self.horizontalLayout_22.addWidget(self.actualizarEspecialistas)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem38)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem39)
        self.tab_2.addTab(self.Especialistas, "")
        self.Visitas = QtWidgets.QWidget()
        self.Visitas.setObjectName("Visitas")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Visitas)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem40)
        self.label_14 = QtWidgets.QLabel(self.Visitas)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem41)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.Visitas)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.label_24 = QtWidgets.QLabel(self.Visitas)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_9.addWidget(self.label_24)
        self.label_17 = QtWidgets.QLabel(self.Visitas)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.horizontalLayout_28.addLayout(self.verticalLayout_9)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.lineEdit = QtWidgets.QLineEdit(self.Visitas)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_18.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Visitas)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_18.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Visitas)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_18.addWidget(self.lineEdit_3)
        self.horizontalLayout_28.addLayout(self.verticalLayout_18)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem42)
        self.verticalLayout_14.addLayout(self.horizontalLayout_28)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem43)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_14.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem44)
        self.pushButton_3 = QtWidgets.QPushButton(self.Visitas)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_26.addWidget(self.pushButton_3)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem45)
        self.verticalLayout_14.addLayout(self.horizontalLayout_26)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem46)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_3 = QtWidgets.QLabel(self.Visitas)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_25.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Visitas)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.buttonBuscarVisitas = QtWidgets.QPushButton(self.Visitas)
        self.buttonBuscarVisitas.setObjectName("pushButton_3")
        self.buttonBuscarVisitas.setText("Filtrar")
        self.horizontalLayout_25.addWidget(self.lineEdit_4)
        self.horizontalLayout_25.addWidget(self.buttonBuscarVisitas)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem47)
        self.pushButton_4 = QtWidgets.QPushButton(self.Visitas)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_25.addWidget(self.pushButton_4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_14.addLayout(self.horizontalLayout_24)
        self.tablaAgendarHora_2 = QtWidgets.QTableWidget(self.Visitas)
        self.tablaAgendarHora_2.setStyleSheet("background-color: white\n"
"")
        self.tablaAgendarHora_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaAgendarHora_2.setAlternatingRowColors(True)
        self.tablaAgendarHora_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablaAgendarHora_2.setRowCount(10)
        self.tablaAgendarHora_2.setColumnCount(6)
        self.tablaAgendarHora_2.setObjectName("tablaAgendarHora_2")
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAgendarHora_2.setItem(0, 1, item)
        self.tablaAgendarHora_2.horizontalHeader().setDefaultSectionSize(135)
        self.tablaAgendarHora_2.horizontalHeader().setMinimumSectionSize(40)
        self.tablaAgendarHora_2.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_14.addWidget(self.tablaAgendarHora_2)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem48)
        self.botonAgendarHora_2 = QtWidgets.QPushButton(self.Visitas)
        self.botonAgendarHora_2.setStyleSheet("")
        self.botonAgendarHora_2.setObjectName("botonAgendarHora_2")
        self.horizontalLayout_32.addWidget(self.botonAgendarHora_2)
        self.verticalLayout_14.addLayout(self.horizontalLayout_32)
        self.tab_2.addTab(self.Visitas, "")
        self.ingresoTab = QtWidgets.QWidget()
        self.ingresoTab.setObjectName("ingresoTab")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.ingresoTab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalIngreso1 = QtWidgets.QVBoxLayout()
        self.verticalIngreso1.setContentsMargins(-1, 10, -1, 20)
        self.verticalIngreso1.setObjectName("verticalIngreso1")
        self.horizontalIngreso4 = QtWidgets.QHBoxLayout()
        self.horizontalIngreso4.setObjectName("horizontalIngreso4")
        self.labelIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelIngresoPaciente.sizePolicy().hasHeightForWidth())
        self.labelIngresoPaciente.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelIngresoPaciente.setFont(font)
        self.labelIngresoPaciente.setObjectName("labelIngresoPaciente")
        self.horizontalIngreso4.addWidget(self.labelIngresoPaciente)
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalIngreso4.addItem(spacerItem49)
        self.verticalIngreso1.addLayout(self.horizontalIngreso4)
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalIngreso1.addItem(spacerItem50)
        self.horizontalIngreso1 = QtWidgets.QHBoxLayout()
        self.horizontalIngreso1.setContentsMargins(35, -1, 35, -1)
        self.horizontalIngreso1.setObjectName("horizontalIngreso1")
        self.verticalIngreso2 = QtWidgets.QVBoxLayout()
        self.verticalIngreso2.setObjectName("verticalIngreso2")
        self.labelRutIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        self.labelRutIngresoPaciente.setObjectName("labelRutIngresoPaciente")
        self.verticalIngreso2.addWidget(self.labelRutIngresoPaciente)
        self.labelNombreIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNombreIngresoPaciente.sizePolicy().hasHeightForWidth())
        self.labelNombreIngresoPaciente.setSizePolicy(sizePolicy)
        self.labelNombreIngresoPaciente.setObjectName("labelNombreIngresoPaciente")
        self.verticalIngreso2.addWidget(self.labelNombreIngresoPaciente)
        self.labelApatIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelApatIngresoPaciente.sizePolicy().hasHeightForWidth())
        self.labelApatIngresoPaciente.setSizePolicy(sizePolicy)
        self.labelApatIngresoPaciente.setObjectName("labelApatIngresoPaciente")
        self.verticalIngreso2.addWidget(self.labelApatIngresoPaciente)
        self.labelAmatIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAmatIngresoPaciente.sizePolicy().hasHeightForWidth())
        self.labelAmatIngresoPaciente.setSizePolicy(sizePolicy)
        self.labelAmatIngresoPaciente.setObjectName("labelAmatIngresoPaciente")
        self.verticalIngreso2.addWidget(self.labelAmatIngresoPaciente)
        self.labelSexoIngresoPaciente = QtWidgets.QLabel(self.ingresoTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSexoIngresoPaciente.sizePolicy().hasHeightForWidth())
        self.labelSexoIngresoPaciente.setSizePolicy(sizePolicy)
        self.labelSexoIngresoPaciente.setObjectName("labelSexoIngresoPaciente")
        self.verticalIngreso2.addWidget(self.labelSexoIngresoPaciente)
        self.horizontalIngreso1.addLayout(self.verticalIngreso2)
        self.verticalIngreso3 = QtWidgets.QVBoxLayout()
        self.verticalIngreso3.setObjectName("verticalIngreso3")
        self.editRutIngresoPaciente = QtWidgets.QLineEdit(self.ingresoTab)
        self.editRutIngresoPaciente.setObjectName("editRutIngresoPaciente")
        self.verticalIngreso3.addWidget(self.editRutIngresoPaciente)
        self.editNombreIngresoPaciente = QtWidgets.QLineEdit(self.ingresoTab)
        self.editNombreIngresoPaciente.setObjectName("editNombreIngresoPaciente")
        self.verticalIngreso3.addWidget(self.editNombreIngresoPaciente)
        self.editApatIngresoPaciente = QtWidgets.QLineEdit(self.ingresoTab)
        self.editApatIngresoPaciente.setObjectName("editApatIngresoPaciente")
        self.verticalIngreso3.addWidget(self.editApatIngresoPaciente)
        self.editAmatIngresoPaciente = QtWidgets.QLineEdit(self.ingresoTab)
        self.editAmatIngresoPaciente.setObjectName("editAmatIngresoPaciente")
        self.verticalIngreso3.addWidget(self.editAmatIngresoPaciente)
        self.comboBoxSexoIngresoPaciente = QtWidgets.QComboBox(self.ingresoTab)
        self.comboBoxSexoIngresoPaciente.setObjectName("comboBoxSexoIngresoPaciente")
        self.comboBoxSexoIngresoPaciente.addItem("")
        self.comboBoxSexoIngresoPaciente.addItem("")
        self.verticalIngreso3.addWidget(self.comboBoxSexoIngresoPaciente)
        self.horizontalIngreso1.addLayout(self.verticalIngreso3)
        self.verticalIngreso1.addLayout(self.horizontalIngreso1)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalIngreso1.addItem(spacerItem51)
        self.horizontalIngreso3 = QtWidgets.QHBoxLayout()
        self.horizontalIngreso3.setObjectName("horizontalIngreso3")
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalIngreso3.addItem(spacerItem52)
        self.buttonIngresarIngresoPaciente = QtWidgets.QPushButton(self.ingresoTab)
        self.buttonIngresarIngresoPaciente.setObjectName("buttonIngresarIngresoPaciente")
        self.horizontalIngreso3.addWidget(self.buttonIngresarIngresoPaciente)
        self.verticalIngreso1.addLayout(self.horizontalIngreso3)
        spacerItem53 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalIngreso1.addItem(spacerItem53)
        self.verticalIngreso1.setStretch(2, 10)
        self.verticalIngreso1.setStretch(4, 1)
        self.verticalLayout_19.addLayout(self.verticalIngreso1)
        self.tab_2.addTab(self.ingresoTab, "")
        self.testtab = QtWidgets.QWidget()
        self.testtab.setObjectName("testtab")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.testtab)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.label_41 = QtWidgets.QLabel(self.testtab)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_64.addWidget(self.label_41)
        self.comboBox_17 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_17.setStyleSheet("background-color:white\n"
"")
        self.comboBox_17.setObjectName("comboBox_17")
        self.horizontalLayout_64.addWidget(self.comboBox_17)
        self.verticalLayout_33.addLayout(self.horizontalLayout_64)
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.label_37 = QtWidgets.QLabel(self.testtab)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_59.addWidget(self.label_37)
        self.comboBox_13 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_13.setStyleSheet("background-color:white\n"
"")
        self.comboBox_13.setObjectName("comboBox_13")
        self.horizontalLayout_59.addWidget(self.comboBox_13)
        self.verticalLayout_33.addLayout(self.horizontalLayout_59)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.label_39 = QtWidgets.QLabel(self.testtab)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_61.addWidget(self.label_39)
        self.comboBox_15 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_15.setStyleSheet("background-color:white\n"
"")
        self.comboBox_15.setObjectName("comboBox_15")
        self.horizontalLayout_61.addWidget(self.comboBox_15)
        self.verticalLayout_33.addLayout(self.horizontalLayout_61)
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.label_40 = QtWidgets.QLabel(self.testtab)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_63.addWidget(self.label_40)
        self.comboBox_16 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_16.setStyleSheet("background-color:white\n"
"")
        self.comboBox_16.setObjectName("comboBox_16")
        self.horizontalLayout_63.addWidget(self.comboBox_16)
        self.verticalLayout_33.addLayout(self.horizontalLayout_63)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.label_2 = QtWidgets.QLabel(self.testtab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_58.addWidget(self.label_2)
        self.comboBox_12 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_12.setStyleSheet("background-color:white\n"
"")
        self.comboBox_12.setObjectName("comboBox_12")
        self.horizontalLayout_58.addWidget(self.comboBox_12)
        self.verticalLayout_33.addLayout(self.horizontalLayout_58)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.label_38 = QtWidgets.QLabel(self.testtab)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_60.addWidget(self.label_38)
        self.comboBox_14 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_14.setStyleSheet("background-color:white\n"
"")
        self.comboBox_14.setObjectName("comboBox_14")
        self.horizontalLayout_60.addWidget(self.comboBox_14)
        self.verticalLayout_33.addLayout(self.horizontalLayout_60)
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.label_42 = QtWidgets.QLabel(self.testtab)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_65.addWidget(self.label_42)
        self.comboBox_18 = QtWidgets.QComboBox(self.testtab)
        self.comboBox_18.setStyleSheet("background-color:white\n"
"")
        self.comboBox_18.setObjectName("comboBox_18")
        self.horizontalLayout_65.addWidget(self.comboBox_18)
        self.verticalLayout_33.addLayout(self.horizontalLayout_65)
        self.horizontalLayout_57.addLayout(self.verticalLayout_33)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_57.addItem(spacerItem49)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.testtab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.testtab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(117)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem50)
        self.pushButton_2 = QtWidgets.QPushButton(self.testtab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.testtab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_16 = QtWidgets.QLabel(self.testtab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.tableWidget = QtWidgets.QTableWidget(self.testtab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_57.addLayout(self.verticalLayout_2)
        self.horizontalLayout_57.setStretch(0, 1)
        self.horizontalLayout_57.setStretch(2, 2)
        self.verticalLayout_32.addLayout(self.horizontalLayout_57)
        self.tab_2.addTab(self.testtab, "")
        self.verticalLayout_10.addWidget(self.tab_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_2.setCurrentIndex(4)
        self.toolBoxHoras.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTriage.setText(_translate("MainWindow", "Triage:"))
        self.labelSintoma1.setText(_translate("MainWindow", "Sintoma 1:"))
        self.labelSintoma2.setText(_translate("MainWindow", "Sintoma 2:"))
        self.labelSintoma3.setText(_translate("MainWindow", "Sintoma 3:"))
        self.labelSintoma4.setText(_translate("MainWindow", "Sintoma 4:"))
        self.labelSintoma5.setText(_translate("MainWindow", "Sintoma 5:"))
        self.labelResultadoTriage.setText(_translate("MainWindow", "Nivel de Urgencia:"))
        self.botonCalcularTriage.setText(_translate("MainWindow", "Calcular Triage"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.triage), _translate("MainWindow", "Triage"))
        self.labelReservas.setText(_translate("MainWindow", "Reservas:"))
        self.labelRUT.setText(_translate("MainWindow", "RUT Paciente:"))
        self.buscarReservas.setText(_translate("MainWindow", "Filtrar"))

        self.confirmarCita.setText(_translate("MainWindow", "Confirmar"))
        self.buttonActualzarReservas.setText(_translate("MainWindow", "Actualizar"))
        self.toolBoxHoras.setItemText(self.toolBoxHoras.indexOf(self.confirmarLlegadaItem), _translate("MainWindow", "Confirmar Llegada"))
        self.label_11.setText(_translate("MainWindow", "Agendar Hora:"))
        self.label_23.setText(_translate("MainWindow", "Especialidad:"))
        self.especialidadAgendarHora.setItemText(0, _translate("MainWindow", "Cardiologia"))
        self.especialidadAgendarHora.setItemText(1, _translate("MainWindow", "Dermatologia"))
        self.especialidadAgendarHora.setItemText(2, _translate("MainWindow", "Pediatria"))
        self.especialidadAgendarHora.setItemText(3, _translate("MainWindow", "Gastroenterologia"))
        self.especialidadAgendarHora.setItemText(4, _translate("MainWindow", "Neurologia"))
        self.especialidadAgendarHora.setItemText(5, _translate("MainWindow", "Oftalmologia"))
        self.especialidadAgendarHora.setItemText(6, _translate("MainWindow", "Ginecologia"))
        self.especialidadAgendarHora.setItemText(7, _translate("MainWindow", "Ortopedia"))
        self.especialidadAgendarHora.setItemText(8, _translate("MainWindow", "Urologia"))
        self.especialidadAgendarHora.setItemText(9, _translate("MainWindow", "Endocrinologia"))
        self.especialidadAgendarHora.setItemText(10, _translate("MainWindow", "Oncologia"))
        self.especialidadAgendarHora.setItemText(11, _translate("MainWindow", "Hematologia"))
        self.especialidadAgendarHora.setItemText(12, _translate("MainWindow", "Nefrologia"))
        self.especialidadAgendarHora.setItemText(13, _translate("MainWindow", "Psiquiatria"))
        self.especialidadAgendarHora.setItemText(14, _translate("MainWindow", "Radiologia"))
        self.especialidadAgendarHora.setItemText(15, _translate("MainWindow", "Neumologia"))
        self.especialidadAgendarHora.setItemText(16, _translate("MainWindow", "Geriatria"))
        self.especialidadAgendarHora.setItemText(17, _translate("MainWindow", "Reumatologia"))
        self.label_8.setText(_translate("MainWindow", "Hora:"))
        self.labelRutPacienteAgenda.setText(_translate("MainWindow", "Rut Paciente:"))
        self.horaAgenda.setItemText(0, _translate("MainWindow", "08:00"))
        self.horaAgenda.setItemText(1, _translate("MainWindow", "10:00"))
        self.horaAgenda.setItemText(2, _translate("MainWindow", "12:00"))
        self.horaAgenda.setItemText(3, _translate("MainWindow", "14:00"))
        self.horaAgenda.setItemText(4, _translate("MainWindow", "16:00"))
        self.horaAgenda.setItemText(5, _translate("MainWindow", "18:00"))
        self.horaAgenda.setItemText(6, _translate("MainWindow", "20:00"))
        self.verDoctoresAgenda.setText(_translate("MainWindow", "Ver Doctores Disponibles"))
        item = self.tablaAgendarHora.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Doctor"))
        item = self.tablaAgendarHora.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Especialidad"))
        __sortingEnabled = self.tablaAgendarHora.isSortingEnabled()
        self.tablaAgendarHora.setSortingEnabled(False)
        self.tablaAgendarHora.setSortingEnabled(__sortingEnabled)
        self.botonAgendarHora.setText(_translate("MainWindow", "Agendar"))
        self.toolBoxHoras.setItemText(self.toolBoxHoras.indexOf(self.agendarHoraItem), _translate("MainWindow", "Agendar Hora"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.Agenda), _translate("MainWindow", "Agenda"))
        self.label_21.setText(_translate("MainWindow", "Doctores"))
        self.label_22.setText(_translate("MainWindow", "Nombre"))
        self.buttonFiltrarTablaDoctores.setText(_translate("MainWindow", "Filtrar"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Doctor"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lunes"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Martes"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Miercoles"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Jueves"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Viernes"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sabado"))
        item = self.tablaEspecialistas_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Domingo"))
        self.buttonActualizarDoctores.setText(_translate("MainWindow", "Actualizar"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.HorarioDoctores), _translate("MainWindow", "Horario Doctores"))
        self.label_9.setText(_translate("MainWindow", "Especialistas:"))
        self.label_10.setText(_translate("MainWindow", "Especialidad:"))
        self.buscarEspecialistas.setText(_translate("MainWindow", "Filtrar"))
        item = self.tablaEspecialistas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tablaEspecialistas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tablaEspecialistas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Numero"))
        self.actualizarEspecialistas.setText(_translate("MainWindow", "Actualizar"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.Especialistas), _translate("MainWindow", "Especialistas"))
        self.label_14.setText(_translate("MainWindow", "Registrar Visita:"))
        self.label_15.setText(_translate("MainWindow", "Rut Paciente:"))
        self.label_24.setText(_translate("MainWindow", "Nombre Visitante:"))
        self.label_17.setText(_translate("MainWindow", "Rut Visitante"))
        self.pushButton_3.setText(_translate("MainWindow", "Registrar Visita"))
        self.label_3.setText(_translate("MainWindow", "Buscar Nombre Visita: "))
        self.pushButton_4.setText(_translate("MainWindow", "Buscar"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre Visitante"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rut Visitante"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hora Ingreso"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora Salida"))
        item = self.tablaAgendarHora_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Salida"))
        __sortingEnabled = self.tablaAgendarHora_2.isSortingEnabled()
        self.tablaAgendarHora_2.setSortingEnabled(False)
        self.tablaAgendarHora_2.setSortingEnabled(__sortingEnabled)
        self.botonAgendarHora_2.setText(_translate("MainWindow", "Confirmar Salida"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.Visitas), _translate("MainWindow", "Visitas"))
        self.labelIngresoPaciente.setText(_translate("MainWindow", "Ingreso Pacientes:"))
        self.labelRutIngresoPaciente.setText(_translate("MainWindow", "Rut:"))
        self.labelNombreIngresoPaciente.setText(_translate("MainWindow", "Nombre:"))
        self.labelApatIngresoPaciente.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.labelAmatIngresoPaciente.setText(_translate("MainWindow", "Apellido Materno:"))
        self.labelSexoIngresoPaciente.setText(_translate("MainWindow", "Sexo:"))
        self.comboBoxSexoIngresoPaciente.setItemText(0, _translate("MainWindow", "Masculino"))
        self.comboBoxSexoIngresoPaciente.setItemText(1, _translate("MainWindow", "Femenino"))
        self.buttonIngresarIngresoPaciente.setText(_translate("MainWindow", "Ingresar"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.ingresoTab), _translate("MainWindow", "Ingreso Pacientes"))
        self.label_41.setText(_translate("MainWindow", "Medicamento 1:"))
        self.label_37.setText(_translate("MainWindow", "Medicamento 2:"))
        self.label_39.setText(_translate("MainWindow", "Medicamento 3:"))
        self.label_40.setText(_translate("MainWindow", "Medicamento 4:"))
        self.label_2.setText(_translate("MainWindow", "Medicamento 5:"))
        self.label_38.setText(_translate("MainWindow", "Medicamento 6:"))
        self.label_42.setText(_translate("MainWindow", "Medicamento 7:"))
        self.label.setText(_translate("MainWindow", "Disponibles"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cantidad Disponible"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar"))
        self.pushButton.setText(_translate("MainWindow", "Entregar Marcados"))
        self.label_16.setText(_translate("MainWindow", "No Disponibles"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Precio"))
        self.tab_2.setTabText(self.tab_2.indexOf(self.testtab), _translate("MainWindow", "Medicamentos"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))


        self.botonCalcularTriage.clicked.connect(self.clickTriage)
        self.actualizarEspecialistas.clicked.connect(self.clickEspecialistas)
        self.buscarEspecialistas.clicked.connect(self.filter_table)
        self.buttonActualzarReservas.clicked.connect(self.clickHoras)
        self.buscarReservas.clicked.connect(self.filter_table2)
        self.confirmarCita.clicked.connect(self.clickConfi)
        self.verDoctoresAgenda.clicked.connect(self.clickVerDoctoresAgenda)
        self.botonAgendarHora.clicked.connect(self.agendarHoraFunc)
        self.pushButton_3.clicked.connect(self.registrarVisita)
        self.pushButton_4.clicked.connect(self.actualizarVisitas)
        self.buttonBuscarVisitas.clicked.connect(self.filter_table3)
        self.botonAgendarHora_2.clicked.connect(self.clickConfiVisitas)

        self.pushButton_2.clicked.connect(self.buscar_remedios)
        self.pushButton.clicked.connect(self.entregarMedicamento)
        self.buttonActualizarDoctores.clicked.connect(self.horariosDoc)
        self.buttonIngresarIngresoPaciente.clicked.connect(self.clickIngresarPaciente)

        
        for sintoma in sintomas:
                self.boxSintoma1.addItem(sintoma)
                self.boxSintoma2.addItem(sintoma)
                self.boxSintoma3_2.addItem(sintoma)
                self.boxSintoma3.addItem(sintoma)
                self.comboBox_5.addItem(sintoma)

        self.boxSintoma1.setCurrentIndex(-1)
        self.boxSintoma2.setCurrentIndex(-1)
        self.boxSintoma3.setCurrentIndex(-1)
        self.boxSintoma3_2.setCurrentIndex(-1)
        self.comboBox_5.setCurrentIndex(-1)

        for remedio in remedios:
                self.comboBox_12.addItem(remedio)
                self.comboBox_13.addItem(remedio)
                self.comboBox_14.addItem(remedio)
                self.comboBox_15.addItem(remedio)
                self.comboBox_16.addItem(remedio)
                self.comboBox_17.addItem(remedio)
                self.comboBox_18.addItem(remedio)



        self.comboBox_12.setCurrentIndex(-1)
        self.comboBox_13.setCurrentIndex(-1)
        self.comboBox_14.setCurrentIndex(-1)
        self.comboBox_15.setCurrentIndex(-1)
        self.comboBox_16.setCurrentIndex(-1)
        self.comboBox_17.setCurrentIndex(-1)
        self.comboBox_18.setCurrentIndex(-1)

    def clickIngresarPaciente(self):
         sock = self.sock
         rut = self.editRutIngresoPaciente.text()
         rut = format_chilean_rut(rut)

         if rut != "Invalid RUT":
              nombre = self.editNombreIngresoPaciente.text()
              apat = self.editApatIngresoPaciente.text()
              amat = self.editAmatIngresoPaciente.text()
              sexo = ""
              if self.comboBoxSexoIngresoPaciente.currentText() == "Masculino":
                   sexo = "M"
              elif self.comboBoxSexoIngresoPaciente.currentText() == "Femenino":
                   sexo = "F"
              if len(nombre) > 0 and len(apat) > 0 and len(amat) > 0 and len(sexo) > 0:
                        inp = "AP" + rut + "/" + nombre + "/" + apat + "/" + amat + "/" + sexo
                        inputLenStr = '{:05d}'.format(len(inp))
                        message = inputLenStr + 'regis' + inp
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
                        print(resp)

                        doctor = resp[12:len(resp) - 1].split('/')


                        respSize = resp[0:5]
                        respSizeInt = int(respSize)
                        respCode = resp[10:12]
                        respCode2 = resp[12:14]
                        # No disp = tableWidget
                        if respCode == 'OK':
                             if respCode2 == 'SC':
                                  self.popUpInfo("Paciente Ingresado Exitosamente")
                             elif respCode2 == 'ER':
                                  self.popUpAlert("El Paciente ya se encuentra en la base de datos")
                             else: self.popUpCritical("A ocurrido un error inesperado")

                        else:
                                self.popUpCritical("A ocurrido un error inesperado")
                                
              else: self.popUpAlert("Un campo no se ha rellenado, favor verifique los datos ingresados")

         else: self.popUpCritical("Rut Invalido")

    def getCheckedValuesMedicamento(self):
        checked_values = []
        for row in range(self.tableWidget_2.rowCount()):
                item = self.tableWidget_2.item(row, 0)  # Assuming the checkboxes are in the first column
                if item is not None and item.checkState() == QtCore.Qt.Checked:
                # Get the value from the respective column for the checked row
                 value = self.tableWidget_2.item(row, 0).text()  # Replace YOUR_DESIRED_COLUMN_NUMBER with the column number you want to retrieve
                 checked_values.append(value)
        return checked_values
    
    def horariosDoc(self):
        sock = self.sock

        inp = "a"
        inputLenStr = '{:05d}'.format(len(inp))
        message = inputLenStr + 'docto' + inp
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
        print(resp)

        doctor = resp[12:len(resp) - 1].split('/')


        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[10:12]
        # No disp = tableWidget
        if respCode == 'OK':
            array_of_arrays = []
            for doc in doctor:
                aux = doc[1:-1].split(",")
                aux2 = []
                for dat in aux:
                    temp = dat.replace("'","")
                    aux2.append(temp)
                array_of_arrays.append(aux2)
            print(array_of_arrays)



            header_titles = ["Nombre", "Lunes", "Martes", "Miércoles", "Jueves","Viernes","Sábado","Domingo"]
            self.tablaEspecialistas_3.setColumnCount(len(header_titles))
            self.tablaEspecialistas_3.setHorizontalHeaderLabels(header_titles)

            # Assuming array_of_arrays contains the data as per the structure in your response
            self.tablaEspecialistas_3.setRowCount(len(array_of_arrays))

            for row_number, row_data in enumerate(array_of_arrays):
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tablaEspecialistas_3.setItem(row_number, column_number, item)

        else:
                print('error')



    def buscar_remedios(self):
        sock = self.sock

        remedio = self.comboBox_12.currentText() + "-" + self.comboBox_13.currentText() + "-" + self.comboBox_14.currentText() + "-" + self.comboBox_15.currentText() + "-" + self.comboBox_16.currentText() + "-" + self.comboBox_17.currentText() + "-" + self.comboBox_18.currentText()

        inputLenStr = '{:05d}'.format(len(remedio))
        message = inputLenStr + 'medic' + remedio
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
        print(resp)
        remedios = resp[12:len(resp) - 1].split('-')
        disp = remedios[0]
        if len(remedios)>1:
            Ndisp = remedios[1]

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[10:12]
        # No disp = tableWidget
        if respCode == 'OK':
            rows = disp.split('],[')
            rowsaux = []
            for row in rows:
                row = row.replace("[","")
                row = row.replace("]","")
                row = row.replace("'","")
                rowsaux.append(row)

            array_of_arrays = [re.split(r',\s*', row) for row in rowsaux]  # Remove parentheses


            header_titles = ["Nombre", "Cantidad disponible", "Cantidad a entregar"]
            self.tableWidget_2.setColumnCount(len(header_titles))
            self.tableWidget_2.setHorizontalHeaderLabels(header_titles)

            # Assuming array_of_arrays contains the data as per the structure in your response
            self.tableWidget_2.setRowCount(len(array_of_arrays))

            for row_number, row_data in enumerate(array_of_arrays):
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    if column_number == 0:
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                    if column_number == 2:
                        item.setFlags()
                    self.tableWidget_2.setItem(row_number, column_number, item)

            if len(remedios)>1:
                rows2 = Ndisp.split('],[')
                rowsaux2 = []
                for row in rows2:
                    row = row.replace("[","")
                    row = row.replace("]","")
                    row = row.replace("'","")
                    rowsaux2.append(row)
                array_of_arrays2 = [re.split(r',\s*', row) for row in rowsaux2]  # Remove parentheses

                header_titles2 = ["Nombre", "Precio"]
                self.tableWidget.setColumnCount(len(header_titles2))
                self.tableWidget.setHorizontalHeaderLabels(header_titles2)

                # Assuming array_of_arrays contains the data as per the structure in your response
                self.tableWidget.setRowCount(len(array_of_arrays2))

                for row_number, row_data in enumerate(array_of_arrays2):
                    for column_number, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget.setItem(row_number, column_number, item)
        else:
                print('error')


    def entregarMedicamento(self):
        sock = self.sock


        column_index = 1  # Replace with the index of the column you want to retrieve values from
        column_values = []

        for row in range(self.tableWidget_2.rowCount()):
            item = self.tableWidget_2.item(row, column_index)
            if item is not None:
                column_values.append(item.text())

        column_index2 = 2  # Replace with the index of the column you want to retrieve values from
        column_values2 = []

        for row in range(self.tableWidget_2.rowCount()):
            item = self.tableWidget_2.item(row, column_index2)
            if item is not None:
                column_values2.append(item.text())
        print(column_values)
        print(column_values2)

        new_num = []       
        AG = True

        for x in range(len(column_values)):
            num = int(column_values[x])-int(column_values2[x])
            if num < 0:
                self.popUpAlert("No existe esa cantidad de medicamentos")
                AG = False
            else:
                new_num.append(num)
            
        if AG == True:
            for x in range(len(column_values)):
                values = self.getCheckedValuesMedicamento()
                print(values)
                input = ""

                for x in range(len(values)):
                    input = input + values[x] + "," + str(new_num[x]) + "-"
                print(input)

                inputLenStr = '{:05d}'.format(len(input))
                message = inputLenStr + 'extra' + input
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

                self.buscar_remedios()  

    def actualizarVisitas(self):
        sock = self.sock


        input1 = "a"
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'visit' + "AV"

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
        print(resp)

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[10:12]

        if respCode == 'OK':

            for row in range(self.tablaAgendarHora_2.rowCount()):
                    self.tablaAgendarHora_2.showRow(row)

            resp = resp[12:]

            rows = resp.split('/')

            array_of_arrays = [re.split(r',\s*', row[1:-1]) for row in rows]  # Remove parentheses
            print(array_of_arrays)

            header_titles = ["ID Visita", "Nombre Paciente", "Hora Ingreso", "Hora Salida", "Fecha", "Nombre Visitante", "Rut", "Confirmado"]
            self.tablaAgendarHora_2.setColumnCount(len(header_titles))
            self.tablaAgendarHora_2.setHorizontalHeaderLabels(header_titles)

            self.tablaAgendarHora_2.setRowCount(len(rows))

            for row_number, row_data in enumerate(rows):
                # Remove '[' and ']' and split the row into individual values
                data = row_data.replace('[', '').replace(']', '').split(', ')

                for column_number, value in enumerate(data):
                    item = None

                    if column_number == 0:  # Checkable column (assuming it's the first column)
                        item = QtWidgets.QTableWidgetItem(value.strip("'"))  # Remove single quotes from values
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)  # Set checkable flag
                        item.setCheckState(QtCore.Qt.Unchecked)  # Set initial check state
                    else:
                        item = QtWidgets.QTableWidgetItem(value.strip("'"))  # Non-checkable column

                    self.tablaAgendarHora_2.setItem(row_number, column_number, item)

    def registrarVisita(self):
         sock = self.sock
         
         rutPaciente = self.lineEdit.text()


         nombreVisitante = self.lineEdit_2.text()
         rutVisitante = self.lineEdit_3.text()
         print(rutPaciente + " " + nombreVisitante + " " + rutVisitante)


         rutVisitante = format_chilean_rut(rutVisitante)
         rutPaciente = format_chilean_rut(rutPaciente)

         if rutVisitante != "Invalid RUT" and  rutPaciente != "Invalid RUT":
                input1 = rutPaciente + "/" + nombreVisitante + "/"+ rutVisitante
                inputLen = len(input1)

                # Format the length with leading zeros to make it 5 digits
                inputLenStr = '{:05d}'.format(inputLen)

                message = inputLenStr + 'visit' + "RV" + input1

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
                print(respCode)
                norut = resp[12:17]
                print(norut)
                hora = resp[len(resp)-5:len(resp)]
                print(hora)


                if respCode == 'OK':
                    if norut == "NORUT":
                         self.popUpAlert("No se encuentra el rut del paciente en la base de datos")
                    
                    else:
                        self.popUpInfo(f"Visita Registrada Correctamente, Hora de Salida: {hora}")
                        print(resp)
                        self.clickVerDoctoresAgenda()
                
                else:
                    self.popUpCritical("Ocurrio un error al registrar la hora")
                    print('error')
                    self.clickVerDoctoresAgenda()
         else:
              
                if (rutPaciente == "Invalid RUT"):
                     self.popUpCritical("El Rut del paciente ingresado no es valido")

                else: self.popUpCritical("El Rut del visitante ingresado no es valido")

    


    def agendarHoraFunc(self):
        sock = self.sock


        selected_rows = set()
        for item in self.tablaAgendarHora.selectedItems():
                selected_rows.add(item.row())

                selected_data = []
        if len(selected_rows) == 0:
            self.popUpAlert("No se ha elegido ningun doctor")
        
        elif len(selected_rows) > 1:
             self.popUpAlert("Porfavor eliga solo un doctor")

        else:
            for row in selected_rows:
                    row_data = []
                    for column in range(self.tablaAgendarHora.columnCount()):
                            item = self.tablaAgendarHora.item(row, column)
                            if item is not None:
                                    row_data.append(item.text())
                            else:
                                    row_data.append('')
                    selected_data.append(row_data)

            # Print the data of selected rows
            for row_data in selected_data:
                print(row_data)

                print(selected_data)

            idDoctor = selected_data[0][0]
            print(idDoctor)
            fecha = self.calendarioAgenda.selectedDate().toString("yyyy-MM-dd")
            hora = self.horaAgenda.currentText()
            rut = self.rutPacienteAgenda.text()
            print(rut)
            rut = format_chilean_rut(rut)

            if rut != "Invalid RUT" and fecha != "" and idDoctor != "":
                input1 = rut + "/" + idDoctor + "/"+ hora + "/" + fecha
                inputLen = len(input1)

                # Format the length with leading zeros to make it 5 digits
                inputLenStr = '{:05d}'.format(inputLen)

                message = inputLenStr + 'citas' + "AG" + input1

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
                print (resp)

                respSize = resp[0:5]
                respSizeInt = int(respSize)
                respCode = resp[10:12]
                respCode2 = resp[12:14]
                print(respCode)
                print(respCode2)

                if respCode == 'OK':
                    if respCode2 == 'NE':
                     self.popUpAlert("El Paciente no se encuentra registrado en la base de datos, porfavor realize el ingreso de paciente primero")
   
                    else:
                        self.popUpInfo("Hora Registrada Correctamente")
                        self.clickVerDoctoresAgenda()

                else:
                    self.popUpCritical("Ocurrio un error al registrar la hora")
                    print('error')
                    self.clickVerDoctoresAgenda()
            else:
                    print(f"{rut} no es valido.")
                    self.popUpCritical("El Rut ingresado no es valido")   
                    self.clickVerDoctoresAgenda()






    def clickVerDoctoresAgenda(self):
        sock = self.sock

        fecha = self.calendarioAgenda.selectedDate().toString("yyyy-MM-dd")
        especialidad = self.especialidadAgendarHora.currentText()
        hora = self.horaAgenda.currentText()
        input1 = fecha + "," + hora + "," + especialidad
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'citas' + "AH" + input1

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
        print(respCode)

        if respCode == 'OK':
            
            rows = re.findall(r'\(\d+, .*?\)', resp[12:len(resp)])
            array_of_arrays = [re.split(r',\s*', row[1:-1]) for row in rows]  # Remove parentheses

            self.tablaAgendarHora.setRowCount(0)
            for row_number, row_data in enumerate(array_of_arrays):
                self.tablaAgendarHora.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tablaAgendarHora.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            print('error')





    def filter_table3(self):
        search_text = self.lineEdit_4.text().lower()
        for row in range(self.tablaAgendarHora_2.rowCount()):
            item = self.tablaAgendarHora_2.item(row, 5)
            if item is not None:
                cell_data = item.text().lower()
                if search_text in cell_data:
                    self.tablaAgendarHora_2.showRow(row)
                else:
                    self.tablaAgendarHora_2.hideRow(row)


    def filter_table2(self):
        search_text = self.rutReservas.text().lower()
        for row in range(self.tablaReservas.rowCount()):
            item = self.tablaReservas.item(row, 2)
            if item is not None:
                cell_data = item.text().lower()
                if search_text in cell_data:
                    self.tablaReservas.showRow(row)
                else:
                    self.tablaReservas.hideRow(row)




    def filter_table(self):
        search_text = self.especialidad.text().lower()
        for row in range(self.tablaEspecialistas.rowCount()):
            item = self.tablaEspecialistas.item(row, 2)
            if item is not None:
                cell_data = item.text().lower()
                if search_text in cell_data:
                    self.tablaEspecialistas.showRow(row)
                else:
                    self.tablaEspecialistas.hideRow(row)

    def clickEspecialistas(self):
        sock = self.sock
        input1 = "a"
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'espec' + input1

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
        print(resp)

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[10:12]

        if respCode == 'OK':
            rows = re.findall(r'\(\d+, .*?\)', resp[12:len(resp)])
            array_of_arrays = [re.split(r',\s*', row[1:-1]) for row in rows]  # Remove parentheses

            header_titles = ["ID", "Nombre", "Especialidad", "Hospital", "Celular"]
            self.tablaEspecialistas.setColumnCount(len(header_titles))
            self.tablaEspecialistas.setHorizontalHeaderLabels(header_titles)

            # Assuming array_of_arrays contains the data as per the structure in your response
            self.tablaEspecialistas.setRowCount(len(array_of_arrays))

            for row_number, row_data in enumerate(array_of_arrays):
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tablaEspecialistas.setItem(row_number, column_number, item)
        else:
                print('error')


    def getCheckedValues(self):
        checked_values = []
        for row in range(self.tablaReservas.rowCount()):
                item = self.tablaReservas.item(row, 0)  # Assuming the checkboxes are in the first column
                if item is not None and item.checkState() == QtCore.Qt.Checked:
                # Get the value from the respective column for the checked row
                 value = self.tablaReservas.item(row, 0).text()  # Replace YOUR_DESIRED_COLUMN_NUMBER with the column number you want to retrieve
                 checked_values.append(value)
        return checked_values
    
    def getCheckedValuesVisitas(self):
        checked_values = []
        for row in range(self.tablaAgendarHora_2.rowCount()):
                item = self.tablaAgendarHora_2.item(row, 0)  # Assuming the checkboxes are in the first column
                if item is not None and item.checkState() == QtCore.Qt.Checked:
                # Get the value from the respective column for the checked row
                 value = self.tablaAgendarHora_2.item(row, 0).text()  # Replace YOUR_DESIRED_COLUMN_NUMBER with the column number you want to retrieve
                 checked_values.append(value)
        return checked_values
    
    

    def clickHoras(self):
        sock = self.sock
        input1 = "a"
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'horas' + input1

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
                # Split the string into individual records and remove '[' and ']' characters
                records = resp[12:].replace('[', '').replace(']', '').split(',')

                column_titles = ["ID Cita", "Nombre Paciente", "RUT", "Fecha", "Doctor", "Hora", "Confirmada"]

                self.tablaReservas.setRowCount(0)
                self.tablaReservas.setColumnCount(len(column_titles))
                self.tablaReservas.setHorizontalHeaderLabels(column_titles)

                self.tablaReservas.setRowCount(0)
                self.tablaReservas.setColumnCount(7)

                for row_number in range(0, len(records), 7):
                        row_data = records[row_number:row_number + 7]
                                
                         # Create a new row in the QTableWidget
                        self.tablaReservas.insertRow(row_number // 7)
                                
                        
                        # Create rows of 7 elements each
                        for column_number, data in enumerate(row_data):
                                # Trim any leading/trailing spaces
                                data = data.strip()
                                if column_number == 5:  # Assuming the time is in the sixth column
                                        try:
                                                # Convert seconds to hours and minutes
                                                total_seconds = int(data.split('=')[1][:-1])  # Extract seconds from the format
                                                hours, remainder = divmod(total_seconds, 3600)
                                                minutes, _ = divmod(remainder, 60)
                                                formatted_time = f"{hours:02}:{minutes:02}"
                                                self.tablaReservas.setItem(row_number // 7, column_number, QtWidgets.QTableWidgetItem(formatted_time))
                                        except (ValueError, IndexError):
                                                # If conversion fails, simply use the original data
                                                self.tablaReservas.setItem(row_number // 7, column_number, QtWidgets.QTableWidgetItem(data))
                                else:
                                                item = QtWidgets.QTableWidgetItem(data)
                                                # For other columns, add data as it is
                                                if column_number == 0:  # Assuming the "Confirmada" column is the last one
                                                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                                                        item.setCheckState(QtCore.Qt.Unchecked)
                                                self.tablaReservas.setItem(row_number // 7, column_number, item)
        else:
                        print('error')


    def clickConfiVisitas(self):
        sock = self.sock

        values = self.getCheckedValuesVisitas()

        input2 = ""

        for value in values:
             input2 = input2 + value + ","
        print(input2)

   

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(len(input2))

        print(inputLenStr)

        message = inputLenStr + 'visit' + "CV" + input2
        
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
        print(resp)

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[14:16]
        print(respCode)

        if respCode == 'OK':
             self.actualizarVisitas()
             self.popUpInfo("Salida registrada exitosamente")
        else: self.popUpAlert("Ocurrió un error al registrar la salida")
    
    def clickConfi(self):
        sock = self.sock


        values = self.getCheckedValues()

        input2 = ""

        for value in values:
             input2 = input2 + value + ","
        print(input2)

   

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(len(input2))

        print(inputLenStr)

        message = inputLenStr + 'citas' + "CH" + input2
        
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
        print(resp)

        respSize = resp[0:5]
        respSizeInt = int(respSize)
        respCode = resp[12:14]
        print(respCode)

        if respCode == 'OK':
             self.clickHoras()
             self.popUpInfo("Hora Confirmada Exitosamente")
        else: self.popUpAlert("Ocurrió un error al confirmar la hora")


       
    def clickTriage(self):

        print(self.usuario)

        sock = self.sock

        input1 = self.boxSintoma1.currentText() + "-" + self.boxSintoma2.currentText() + "-" + self.boxSintoma3.currentText() + "-" + self.boxSintoma3_2.currentText() + "-" + self.comboBox_5.currentText()

        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)

        message = inputLenStr + 'triaj' + input1
        
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

        #print('size:', respSize)

        respSizeInt = int(respSize)
       # print('sizeInt:', respSizeInt)

        respCode = resp[10:12]
        #print('code:', respCode)

        if(respCode == 'OK'):
            print("Mensaje: " + resp[12:len(resp)])
            self.labelResultadoTriage.setText("Nivel de Urgencia: " + resp[12:len(resp)])
            self.update()



        else: 
            print('error')
            self.resultadoTriage.setText("Mensaje: " 'Hubo un error al procesar el mensaje')
            self.update()

    

    def clicked(self):
        sock = self.sock


        input1 = self.echoinput.text()
        inputLen = len(input1)

        # Format the length with leading zeros to make it 5 digits
        inputLenStr = '{:05d}'.format(inputLen)
        
        # Create the message as a regular string
        message = inputLenStr + 'servi' + input1
        
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

        respSize = resp[0:5]

        #print('size:', respSize)

        respSizeInt = int(respSize)
       # print('sizeInt:', respSizeInt)

        respCode = resp[10:12]
        #print('code:', respCode)

        if(respCode == 'OK'):
            print("Mensaje: " + resp[12:len(resp)])
            self.outputLabel.setText("Mensaje: " + resp[12:len(resp)])
            self.update()



        else: 
            print('error')
            self.outputLabel.setText("Mensaje: " 'Hubo un error al procesar el mensaje')
            self.update()


    def update(self):
        self.labelResultadoTriage.adjustSize()





if __name__ == "__main__":
    
    import sys

    # Connect the socket to the port where the server is listening



    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
