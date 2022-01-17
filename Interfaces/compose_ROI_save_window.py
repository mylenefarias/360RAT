# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_multiple_ROI_dark.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaveComposeROI(object):
    def setupUi(self, SaveComposeROI):
        SaveComposeROI.setObjectName("SaveComposeROI")
        SaveComposeROI.resize(553, 611)
        SaveComposeROI.setStyleSheet("background-color: rgb(28, 29, 73);\n"
"color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(SaveComposeROI)
        self.label.setGeometry(QtCore.QRect(110, 40, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.button_save_compose_ROI = QtWidgets.QPushButton(SaveComposeROI)
        self.button_save_compose_ROI.setGeometry(QtCore.QRect(220, 560, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_compose_ROI.setFont(font)
        self.button_save_compose_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_compose_ROI.setObjectName("button_save_compose_ROI")
        self.label_2 = QtWidgets.QLabel(SaveComposeROI)
        self.label_2.setGeometry(QtCore.QRect(210, 400, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(SaveComposeROI)
        self.scrollArea.setGeometry(QtCore.QRect(70, 100, 441, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 279))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.groupBox = QtWidgets.QGroupBox(SaveComposeROI)
        self.groupBox.setGeometry(QtCore.QRect(140, 430, 301, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.button_yes = QtWidgets.QPushButton(self.groupBox)
        self.button_yes.setGeometry(QtCore.QRect(30, 40, 93, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button_yes.setFont(font)
        self.button_yes.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_yes.setCheckable(False)
        self.button_yes.setObjectName("button_yes")
        self.button_no = QtWidgets.QPushButton(self.groupBox)
        self.button_no.setGeometry(QtCore.QRect(170, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button_no.setFont(font)
        self.button_no.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_no.setObjectName("button_no")

        self.retranslateUi(SaveComposeROI)
        QtCore.QMetaObject.connectSlotsByName(SaveComposeROI)

    def retranslateUi(self, SaveComposeROI):
        _translate = QtCore.QCoreApplication.translate
        SaveComposeROI.setWindowTitle(_translate("SaveComposeROI", "Dialog"))
        self.label.setText(_translate("SaveComposeROI", "Choose the label of Compose ROI:"))
        self.button_save_compose_ROI.setText(_translate("SaveComposeROI", "Ok"))
        self.label_2.setText(_translate("SaveComposeROI", "Roi is moving?"))
        self.button_yes.setText(_translate("SaveComposeROI", "Yes"))
        self.button_no.setText(_translate("SaveComposeROI", "NO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaveComposeROI = QtWidgets.QDialog()
    ui = Ui_SaveComposeROI()
    ui.setupUi(SaveComposeROI)
    SaveComposeROI.show()
    sys.exit(app.exec_())