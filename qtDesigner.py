# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 552)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_convert = QtWidgets.QPushButton(Dialog)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.gridLayout.addWidget(self.pushButton_convert, 1, 0, 1, 1)
        self.label = ImageArea(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton_paste = QtWidgets.QPushButton(Dialog)
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.gridLayout.addWidget(self.pushButton_paste, 1, 1, 1, 1)
        self.pushButton_copy3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_copy3.setObjectName("pushButton_copy3")
        self.gridLayout.addWidget(self.pushButton_copy3, 5, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 1)
        self.pushButton_copy1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_copy1.setObjectName("pushButton_copy1")
        self.gridLayout.addWidget(self.pushButton_copy1, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.pushButton_copy2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_copy2.setObjectName("pushButton_copy2")
        self.gridLayout.addWidget(self.pushButton_copy2, 4, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMaximumSize(QtCore.QSize(16777215, 120))
        self.webEngineView.setAutoFillBackground(True)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_convert.setText(_translate("Dialog", "Convert"))
        self.label.setText(_translate("Dialog", "<Drag an image or Copy from the paste board>"))
        self.pushButton_paste.setText(_translate("Dialog", "PasteBoard"))
        self.pushButton_copy3.setText(_translate("Dialog", "Copy"))
        self.pushButton_copy1.setText(_translate("Dialog", "Copy"))
        self.pushButton_copy2.setText(_translate("Dialog", "Copy"))

from PyQt5 import QtWebEngineWidgets
from customClass import ImageArea
