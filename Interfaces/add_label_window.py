# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ROI_add_label_window_dark.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddLabel(object):
    def setupUi(self, AddLabel):
        AddLabel.setObjectName("AddLabel")
        AddLabel.resize(296, 160)
        AddLabel.setStyleSheet("background-color: rgb(28, 29, 73);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(AddLabel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_result = QtWidgets.QLabel(AddLabel)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.text_result.setFont(font)
        self.text_result.setText("")
        self.text_result.setAlignment(QtCore.Qt.AlignCenter)
        self.text_result.setObjectName("text_result")
        self.verticalLayout.addWidget(self.text_result)
        self.pushButton_OK = QtWidgets.QPushButton(AddLabel)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.verticalLayout.addWidget(self.pushButton_OK)

        self.retranslateUi(AddLabel)
        QtCore.QMetaObject.connectSlotsByName(AddLabel)

    def retranslateUi(self, AddLabel):
        _translate = QtCore.QCoreApplication.translate
        AddLabel.setWindowTitle(_translate("AddLabel", "Dialog"))
        self.pushButton_OK.setText(_translate("AddLabel", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddLabel = QtWidgets.QDialog()
    ui = Ui_AddLabel()
    ui.setupUi(AddLabel)
    AddLabel.show()
    sys.exit(app.exec_())
