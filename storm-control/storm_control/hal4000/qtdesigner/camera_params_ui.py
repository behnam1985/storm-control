# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera-params.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(173, 175)
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupBox)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EMCCDLabel = QtWidgets.QLabel(GroupBox)
        self.EMCCDLabel.setObjectName("EMCCDLabel")
        self.horizontalLayout.addWidget(self.EMCCDLabel)
        self.EMCCDSlider = QtWidgets.QSlider(GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EMCCDSlider.sizePolicy().hasHeightForWidth())
        self.EMCCDSlider.setSizePolicy(sizePolicy)
        self.EMCCDSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.EMCCDSlider.setMaximum(100)
        self.EMCCDSlider.setProperty("value", 0)
        self.EMCCDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EMCCDSlider.setObjectName("EMCCDSlider")
        self.horizontalLayout.addWidget(self.EMCCDSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.preampGainLabel = QtWidgets.QLabel(GroupBox)
        self.preampGainLabel.setObjectName("preampGainLabel")
        self.horizontalLayout_2.addWidget(self.preampGainLabel)
        self.preampGainText = QtWidgets.QLabel(GroupBox)
        self.preampGainText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.preampGainText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.preampGainText.setObjectName("preampGainText")
        self.horizontalLayout_2.addWidget(self.preampGainText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pictureSizeLabel = QtWidgets.QLabel(GroupBox)
        self.pictureSizeLabel.setObjectName("pictureSizeLabel")
        self.horizontalLayout_3.addWidget(self.pictureSizeLabel)
        self.pictureSizeText = QtWidgets.QLabel(GroupBox)
        self.pictureSizeText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pictureSizeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pictureSizeText.setObjectName("pictureSizeText")
        self.horizontalLayout_3.addWidget(self.pictureSizeText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pictureStartLabel = QtWidgets.QLabel(GroupBox)
        self.pictureStartLabel.setObjectName("pictureStartLabel")
        self.horizontalLayout_7.addWidget(self.pictureStartLabel)
        self.pictureStartText = QtWidgets.QLabel(GroupBox)
        self.pictureStartText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pictureStartText.setObjectName("pictureStartText")
        self.horizontalLayout_7.addWidget(self.pictureStartText)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exposureTimeLabel = QtWidgets.QLabel(GroupBox)
        self.exposureTimeLabel.setObjectName("exposureTimeLabel")
        self.horizontalLayout_4.addWidget(self.exposureTimeLabel)
        self.exposureTimeText = QtWidgets.QLabel(GroupBox)
        self.exposureTimeText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exposureTimeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exposureTimeText.setObjectName("exposureTimeText")
        self.horizontalLayout_4.addWidget(self.exposureTimeText)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.FPSLabel = QtWidgets.QLabel(GroupBox)
        self.FPSLabel.setObjectName("FPSLabel")
        self.horizontalLayout_5.addWidget(self.FPSLabel)
        self.FPSText = QtWidgets.QLabel(GroupBox)
        self.FPSText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FPSText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FPSText.setObjectName("FPSText")
        self.horizontalLayout_5.addWidget(self.FPSText)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.temperatureLabel = QtWidgets.QLabel(GroupBox)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.horizontalLayout_6.addWidget(self.temperatureLabel)
        self.temperatureText = QtWidgets.QLabel(GroupBox)
        self.temperatureText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temperatureText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperatureText.setObjectName("temperatureText")
        self.horizontalLayout_6.addWidget(self.temperatureText)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "Camera"))
        self.EMCCDLabel.setText(_translate("GroupBox", "EMCCD Gain: 0"))
        self.preampGainLabel.setText(_translate("GroupBox", "Preamp Gain:"))
        self.preampGainText.setText(_translate("GroupBox", "asdf"))
        self.pictureSizeLabel.setText(_translate("GroupBox", "Picture Size:"))
        self.pictureSizeText.setText(_translate("GroupBox", "asdf"))
        self.pictureStartLabel.setText(_translate("GroupBox", "Picture Start:"))
        self.pictureStartText.setText(_translate("GroupBox", "asdf"))
        self.exposureTimeLabel.setText(_translate("GroupBox", "Exposure Time (s):"))
        self.exposureTimeText.setText(_translate("GroupBox", "asdf"))
        self.FPSLabel.setText(_translate("GroupBox", "FPS (Hz):"))
        self.FPSText.setText(_translate("GroupBox", "asdf"))
        self.temperatureLabel.setText(_translate("GroupBox", "Temperature (C):"))
        self.temperatureText.setText(_translate("GroupBox", "asdf"))

