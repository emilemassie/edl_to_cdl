# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/emile/Python/EDLtoCDL.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EDL_TO_CDL(object):
    def setupUi(self, EDL_TO_CDL):
        EDL_TO_CDL.setObjectName("EDL_TO_CDL")
        EDL_TO_CDL.resize(468, 154)
        self.verticalLayout = QtWidgets.QVBoxLayout(EDL_TO_CDL)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(EDL_TO_CDL)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(EDL_TO_CDL)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(EDL_TO_CDL)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(EDL_TO_CDL)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(EDL_TO_CDL)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.toolButton_3 = QtWidgets.QToolButton(EDL_TO_CDL)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.comboBox = QtWidgets.QComboBox(EDL_TO_CDL)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(EDL_TO_CDL)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(EDL_TO_CDL)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EDL_TO_CDL)
        QtCore.QMetaObject.connectSlotsByName(EDL_TO_CDL)

    def retranslateUi(self, EDL_TO_CDL):
        _translate = QtCore.QCoreApplication.translate
        EDL_TO_CDL.setWindowTitle(_translate("EDL_TO_CDL", "Form"))
        self.toolButton.setText(_translate("EDL_TO_CDL", "..."))
        self.label.setText(_translate("EDL_TO_CDL", "EDL FILE"))
        self.label_2.setText(_translate("EDL_TO_CDL", "OUTPUT DIRECTORY"))
        self.toolButton_3.setText(_translate("EDL_TO_CDL", "..."))
        self.comboBox.setItemText(0, _translate("EDL_TO_CDL", "CDL"))
        self.comboBox.setItemText(1, _translate("EDL_TO_CDL", "CC"))
        self.comboBox.setItemText(2, _translate("EDL_TO_CDL", "CCC"))
        self.label_5.setText(_translate("EDL_TO_CDL", "EXPORT TYPE"))

