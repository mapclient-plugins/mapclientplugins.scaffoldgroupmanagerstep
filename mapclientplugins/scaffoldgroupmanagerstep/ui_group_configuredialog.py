# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_configuredialog.ui'
#
# Created: Wed May 13 14:10:57 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MehGroupConfigureDialog(object):
    def setupUi(self, MehGroupConfigureDialog):
        MehGroupConfigureDialog.setObjectName("MehGroupConfigureDialog")
        MehGroupConfigureDialog.resize(539, 278)
        self.gridLayout = QtGui.QGridLayout(MehGroupConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(MehGroupConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.configGroupBox = QtGui.QGroupBox(MehGroupConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.configGroupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.configGroupBox)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.plainTextEdit)
        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)

        self.retranslateUi(MehGroupConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MehGroupConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MehGroupConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MehGroupConfigureDialog)

    def retranslateUi(self, MehGroupConfigureDialog):
        MehGroupConfigureDialog.setWindowTitle(QtGui.QApplication.translate("MehGroupConfigureDialog", "Group Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MehGroupConfigureDialog", "Please enter the mesh groups below.\n"
"One group per line.\n"
"", None, QtGui.QApplication.UnicodeUTF8))

