# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(597, 336)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setItalic(True)
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.gridLayout_2.addWidget(self.label0, 2, 0, 1, 1)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.configGroupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton_2, 11, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.pushButton = QPushButton(self.configGroupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pushButton, 9, 0, 1, 1)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 8, 0, 1, 1)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")
        sizePolicy.setHeightForWidth(self.lineEdit0.sizePolicy().hasHeightForWidth())
        self.lineEdit0.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineEdit0, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.label_5.setText(QCoreApplication.translate("ConfigureDialog", u"None", None))
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.label_3.setText(QCoreApplication.translate("ConfigureDialog", u"Or create a new one:", None))
        self.pushButton_2.setText(QCoreApplication.translate("ConfigureDialog", u"New config file", None))
        self.label_2.setText(QCoreApplication.translate("ConfigureDialog", u"This step converts the volume groups in the scaffold to surface xi3=0 as specified by the config file.", None))
        self.pushButton.setText(QCoreApplication.translate("ConfigureDialog", u"Load config file", None))
        self.label_4.setText(QCoreApplication.translate("ConfigureDialog", u"Saved config file from previous sessions: ", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Load a config file:", None))
    # retranslateUi

