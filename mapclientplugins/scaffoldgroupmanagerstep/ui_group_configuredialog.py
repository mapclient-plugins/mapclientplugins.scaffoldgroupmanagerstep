# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MehGroupConfigureDialog(object):
    def setupUi(self, MehGroupConfigureDialog):
        if not MehGroupConfigureDialog.objectName():
            MehGroupConfigureDialog.setObjectName(u"MehGroupConfigureDialog")
        MehGroupConfigureDialog.resize(569, 361)
        self.gridLayout = QGridLayout(MehGroupConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(MehGroupConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(MehGroupConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.plainTextEdit = QPlainTextEdit(self.configGroupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.plainTextEdit)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(MehGroupConfigureDialog)
        self.buttonBox.accepted.connect(MehGroupConfigureDialog.accept)
        self.buttonBox.rejected.connect(MehGroupConfigureDialog.reject)

        QMetaObject.connectSlotsByName(MehGroupConfigureDialog)
    # setupUi

    def retranslateUi(self, MehGroupConfigureDialog):
        MehGroupConfigureDialog.setWindowTitle(QCoreApplication.translate("MehGroupConfigureDialog", u"Group Editor", None))
        self.configGroupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MehGroupConfigureDialog", u"<html><head/><body><p>Please enter the mesh groups below.</p><p>One group per line. Also specify the surface for each group.</p><p>Example:</p><p>- left pulmany vein, inner</p><p>- interatrial septum, outer</p><p><br/></p></body></html>", None))
        self.plainTextEdit.setPlainText("")
    # retranslateUi

