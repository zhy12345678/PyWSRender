# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WSRender_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 9, 4, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 16, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 15, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 8, 0, 2, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 15, 0, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 12, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 16, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 13, 0, 2, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 9, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 13, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 12, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 16, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 5, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 2, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 13, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, 14, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 12, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 8, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 14, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 17, 0, 1, 2)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 17, 2, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label.setText(_translate("MainWindow", "WSRender "))
        self.label_2.setText(_translate("MainWindow", "A Workspace Analysis and Visualization Toolbox"))
        self.label_3.setText(_translate("MainWindow", "Analysis Type"))
        self.label_5.setText(_translate("MainWindow", "Select Robot"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.02"))
        self.radioButton.setText(_translate("MainWindow", "Mento Carlo"))
        self.label_10.setText(_translate("MainWindow", "Precision"))
        self.label_11.setText(_translate("MainWindow", "Evaluation Indics"))
        self.pushButton_8.setText(_translate("MainWindow", "Clear"))
        self.label_14.setText(_translate("MainWindow", "File Dir"))
        self.pushButton_3.setText(_translate("MainWindow", "Workspace Analysis"))
        self.pushButton_7.setText(_translate("MainWindow", "Save Results"))
        self.label_8.setText(_translate("MainWindow", "Sample Number"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Manipulability"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Inverse Condition Number"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Minimum Singlar Value"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Order-Independent Manipulability"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Harmonic Mean Manipulability Index"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Isotropic Index"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Condition Number"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Dynamic Manipulability"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "Dynamic Inverse Condition Number"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "Dynamic Minimum Singlar Value"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "Dynamic Order-Independent Manipulability"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "Dynamic Harmonic Mean Manipulability"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "Dynamic Isotropic Index"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "Dynamic Condition Number"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "Workspace Volume"))
        self.comboBox_4.setItemText(15, _translate("MainWindow", "Structure Length Index"))
        self.pushButton_9.setText(_translate("MainWindow", "Exit"))
        self.pushButton_6.setText(_translate("MainWindow", "Workspace Visualization"))
        self.lineEdit_3.setText(_translate("MainWindow", "0.0004"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dual-Arm Robot Analysis"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Single Robot Analysis"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Master-Slave Mapping"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Multi_Robots Interaction"))
        self.label_13.setText(_translate("MainWindow", "Visualization Mode"))
        self.pushButton_2.setText(_translate("MainWindow", "Robot Constrution"))
        self.label_9.setText(_translate("MainWindow", "Error"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "define"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "floor"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "table"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "frame"))
        self.label_12.setText(_translate("MainWindow", "Global Evaluation Results"))
        self.pushButton.setText(_translate("MainWindow", "Configure"))
        self.label_7.setText(_translate("MainWindow", "Select Environment              "))
        self.radioButton_3.setText(_translate("MainWindow", "Couple"))
        self.label_4.setText(_translate("MainWindow", "Status"))
        self.pushButton_4.setText(_translate("MainWindow", "Workspace Analysis"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "XSlice"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "YSlice"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "ZSlice"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Isovalue"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Alphavalue"))
        self.radioButton_2.setText(_translate("MainWindow", "Joint Limit"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Articulated"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Spherical"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SCARA"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Cartesian"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Cylinder"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Underactuated"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Redundant"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "dVRK"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Omni"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "MIS"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "HamlynCRM"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Puma560"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "ABB_Yumi"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Defined"))
        self.pushButton_5.setText(_translate("MainWindow", "Calculate"))
        self.lineEdit_2.setText(_translate("MainWindow", "50"))
        self.radioButton_4.setText(_translate("MainWindow", "Iteration Method        "))
        self.lineEdit.setText(_translate("MainWindow", "Finished Generate Volume Data"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Scatter Data"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Volume Data"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Convhull"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "IsoSurface"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Slice"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "TriSurf"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "AlphaSurface"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "Reachable Workspace"))