from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from joblib import load
import numpy as np
import pandas as pd

# -*- coding: utf-8 -*-

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Predict apartments price")
        MainWindow.resize(900, 500)
        MainWindow.setStyleSheet("background-color: rgb(225,250,252)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.type_of_house = QtWidgets.QComboBox(self.centralwidget)
        self.type_of_house.setGeometry(QtCore.QRect(50, 90, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_house.setFont(font)
        self.type_of_house.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(232,255,255);\n"
                                         "selection-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "")
        self.type_of_house.setObjectName("type_of_house")
        self.type_of_house.addItem("")
        self.type_of_house.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.type_of_view = QtWidgets.QComboBox(self.centralwidget)
        self.type_of_view.setGeometry(QtCore.QRect(355, 90, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_view.setFont(font)
        self.type_of_view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "selection-background-color: rgb(232,255,255);\n"
                                        "selection-color: rgb(0, 0, 0);\n"
                                        "\n"
                                        "")
        self.type_of_view.setObjectName("type_of_view")
        self.type_of_view.addItem("")
        self.type_of_view.addItem("")
        self.type_of_view.addItem("")
        self.time_metro = QtWidgets.QSpinBox(self.centralwidget)
        self.time_metro.setGeometry(QtCore.QRect(650, 90, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_metro.setFont(font)
        self.time_metro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_metro.setAlignment(QtCore.Qt.AlignCenter)
        self.time_metro.setMinimum(1)
        self.time_metro.setMaximum(60)
        self.time_metro.setProperty("value", 5)
        self.time_metro.setObjectName("time_metro")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 40, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 140, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.number_of_rooms = QtWidgets.QComboBox(self.centralwidget)
        self.number_of_rooms.setGeometry(QtCore.QRect(50, 190, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_of_rooms.setFont(font)
        self.number_of_rooms.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "selection-background-color: rgb(232,255,255);\n"
                                           "selection-color: rgb(0, 0, 0);\n"
                                           "\n"
                                           "")
        self.number_of_rooms.setObjectName("number_of_rooms")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 140, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.area = QtWidgets.QSpinBox(self.centralwidget)
        self.area.setGeometry(QtCore.QRect(380, 190, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area.setFont(font)
        self.area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.area.setAlignment(QtCore.Qt.AlignCenter)
        self.area.setMinimum(10)
        self.area.setMaximum(1000)
        self.area.setProperty("value", 25)
        self.area.setObjectName("area")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.number_of_floors = QtWidgets.QSpinBox(self.centralwidget)
        self.number_of_floors.setGeometry(QtCore.QRect(160, 290, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_of_floors.setFont(font)
        self.number_of_floors.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number_of_floors.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_floors.setMinimum(1)
        self.number_of_floors.setMaximum(60)
        self.number_of_floors.setProperty("value", 10)
        self.number_of_floors.setObjectName("number_of_floors")
        self.floor = QtWidgets.QSpinBox(self.centralwidget)
        self.floor.setGeometry(QtCore.QRect(50, 290, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.floor.setFont(font)
        self.floor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.floor.setAlignment(QtCore.Qt.AlignCenter)
        self.floor.setMinimum(1)
        self.floor.setMaximum(60)
        self.floor.setProperty("value", 5)
        self.floor.setObjectName("floor")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(355, 240, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.year_of_construction = QtWidgets.QSpinBox(self.centralwidget)
        self.year_of_construction.setGeometry(QtCore.QRect(380, 290, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_of_construction.setFont(font)
        self.year_of_construction.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.year_of_construction.setAlignment(QtCore.Qt.AlignCenter)
        self.year_of_construction.setMinimum(1700)
        self.year_of_construction.setMaximum(5000)
        self.year_of_construction.setProperty("value", 2000)
        self.year_of_construction.setObjectName("year_of_construction")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 340, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.height_of_ceiling = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.height_of_ceiling.setGeometry(QtCore.QRect(50, 390, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.height_of_ceiling.setFont(font)
        self.height_of_ceiling.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.height_of_ceiling.setMinimum(1.0)
        self.height_of_ceiling.setObjectName("height_of_ceiling")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 340, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.number_of_bathrooms = QtWidgets.QSpinBox(self.centralwidget)
        self.number_of_bathrooms.setGeometry(QtCore.QRect(650, 390, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_of_bathrooms.setFont(font)
        self.number_of_bathrooms.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number_of_bathrooms.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_bathrooms.setMinimum(1)
        self.number_of_bathrooms.setMaximum(10)
        self.number_of_bathrooms.setProperty("value", 1)
        self.number_of_bathrooms.setObjectName("number_of_bathrooms")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 240, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.metro = QtWidgets.QLineEdit(self.centralwidget)
        self.metro.setGeometry(QtCore.QRect(650, 290, 200, 30))
        self.metro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.metro.setObjectName("metro")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(380, 375, 150, 50))
        self.btn_submit.setStyleSheet("background-color: rgb(255, 150, 150);\n"
                                      "")
        self.btn_submit.setObjectName("btn_submit")
        self.area_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.area_2.setGeometry(QtCore.QRect(650, 190, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area_2.setFont(font)
        self.area_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.area_2.setAlignment(QtCore.Qt.AlignCenter)
        self.area_2.setMinimum(10)
        self.area_2.setMaximum(1000)
        self.area_2.setProperty("value", 10)
        self.area_2.setObjectName("area_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(640, 150, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predict Moscow apartaments price"))
        self.type_of_house.setItemText(0, _translate("MainWindow", "Вторичка"))
        self.type_of_house.setItemText(1, _translate("MainWindow", "Новостройка"))
        self.label.setText(_translate("MainWindow", "Тип Жилья"))
        self.label_2.setText(_translate("MainWindow", "Вид из окна"))
        self.type_of_view.setItemText(0, _translate("MainWindow", "На улицу"))
        self.type_of_view.setItemText(1, _translate("MainWindow", "Во двор"))
        self.type_of_view.setItemText(2, _translate("MainWindow", "На улицу и двор"))
        self.label_3.setText(_translate("MainWindow", "Время до метро"))
        self.label_4.setText(_translate("MainWindow", "Комнат"))
        self.number_of_rooms.setItemText(0, _translate("MainWindow", "1 комната"))
        self.number_of_rooms.setItemText(1, _translate("MainWindow", "2 комнаты"))
        self.number_of_rooms.setItemText(2, _translate("MainWindow", "3 комнаты"))
        self.number_of_rooms.setItemText(3, _translate("MainWindow", "4 комнаты"))
        self.number_of_rooms.setItemText(4, _translate("MainWindow", "5 комнат"))
        self.number_of_rooms.setItemText(5, _translate("MainWindow", "Многокомнатная "))
        self.label_5.setText(_translate("MainWindow", "Общая площадь"))
        self.label_6.setText(_translate("MainWindow", "Этаж и этажность"))
        self.label_7.setText(_translate("MainWindow", "Год постройки"))
        self.label_8.setText(_translate("MainWindow", "Высота потолков"))
        self.label_9.setText(_translate("MainWindow", "Ванных"))
        self.label_10.setText(_translate("MainWindow", "Метро"))
        self.btn_submit.setText(_translate("MainWindow", "Готово"))
        self.label_11.setText(_translate("MainWindow", "Жилая площадь"))

    def add_func(self):
        self.btn_submit.clicked.connect(self.btn_submition)

    def btn_submition(self):

        LivingArea = self.area_2.value()
        TypeOfHouse = self.type_of_house.currentText()
        TypeOfView = self.type_of_view.currentText()
        TimeMetro = self.time_metro.value()
        NumberOfRooms = self.number_of_rooms.currentText()
        ValueArea = self.area.value()
        Floor = self.floor.value()
        NumberOfFloors = self.number_of_floors.value()
        YearOfConstruction = self.year_of_construction.value()
        Metro = self.metro.text()
        HeightOfCelling = self.height_of_ceiling.value()
        NumberOfBathrooms = self.number_of_bathrooms.value()

        data = [TimeMetro, NumberOfRooms, ValueArea, LivingArea, Floor, NumberOfFloors, YearOfConstruction, TypeOfHouse,
                HeightOfCelling, NumberOfBathrooms, TypeOfView]

        metro = pd.read_csv('https://raw.githubusercontent.com/yaroslav711/Predict_Price/main/gui/metro.csv', 
                            index_col = False).drop('ind', axis = 1)

        metro = pd.DataFrame({'Name' : metro['Russian name'], 
                      'Line' : metro['Line'],
                      'C1' : metro['Coordinates'],
                      'C2' : metro['Arts & Entertainment'],
                      'N_transfers' : np.ones(264)})

        ind = list(metro['Name']).index(Metro)
        data.append(metro['C1'][ind])
        data.append(metro['C2'][ind])
        data.append(int(metro['Line'][ind]))

        rooms = ['Студия', '1 комната', '2 комнаты', '3 комнаты',
                 '4 комнаты', '5 комнат', 'Многокомнатная ']

        if rooms.index(data[1]) > 0: data[1] = rooms.index(data[1])
        else: data[1] = 1

        type = ['Вторичка', 'Новостройка']
        data[7] = type.index(data[7])

        view = ['Во двор', 'На улицу', 'На улицу и двор', 'Нет информации']
        data[10] = view.index(data[10])

        for x in [0, 2, 3, 4, 5]:
            data[x] = np.log(data[x])

        clf = load('xboost.joblib')
        data = np.reshape(data, (1, -1))

        pred = str(int(np.round(clf.predict(data))))
        pred = pred[::-1]

        tabs = (len(pred)-1) // 3
        ost = len(pred) - 3*tabs
        ost = pred[-ost:]
        st = ''
        for tab in range(tabs):
            st += pred[3*tab:3*(tab+1)] + ' '
        pred = st + ost
        pred = pred[::-1]

        price = QMessageBox()
        price.setWindowTitle("Цена")
        price.setText(f'Приблизительная цена квартиры:\n   {pred}₽')
        price.setIcon(QMessageBox.Information)
        price.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        price.exec_()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())