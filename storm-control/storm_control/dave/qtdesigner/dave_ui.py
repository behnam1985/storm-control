# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dave.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 723)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(590, 500))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainGridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.mainGridLayout.setContentsMargins(2, 2, 2, 2)
        self.mainGridLayout.setSpacing(2)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.sequenceGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sequenceGroupBox.setObjectName("sequenceGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sequenceGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sequenceLabel = QtWidgets.QLabel(self.sequenceGroupBox)
        self.sequenceLabel.setObjectName("sequenceLabel")
        self.verticalLayout.addWidget(self.sequenceLabel)
        self.mainGridLayout.addWidget(self.sequenceGroupBox, 0, 1, 1, 4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.notificationGroupBox = QtWidgets.QGroupBox(self.widget)
        self.notificationGroupBox.setMinimumSize(QtCore.QSize(260, 0))
        self.notificationGroupBox.setObjectName("notificationGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.notificationGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.estimatesGroupBox = QtWidgets.QGroupBox(self.notificationGroupBox)
        self.estimatesGroupBox.setMinimumSize(QtCore.QSize(84, 0))
        self.estimatesGroupBox.setObjectName("estimatesGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.estimatesGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spaceLabel = QtWidgets.QLabel(self.estimatesGroupBox)
        self.spaceLabel.setObjectName("spaceLabel")
        self.verticalLayout_2.addWidget(self.spaceLabel)
        self.timeLabel = QtWidgets.QLabel(self.estimatesGroupBox)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_2.addWidget(self.timeLabel)
        self.remainingLabel = QtWidgets.QLabel(self.estimatesGroupBox)
        self.remainingLabel.setObjectName("remainingLabel")
        self.verticalLayout_2.addWidget(self.remainingLabel)
        self.gridLayout.addWidget(self.estimatesGroupBox, 11, 0, 1, 3)
        self.fromAddressLineEdit = QtWidgets.QLineEdit(self.notificationGroupBox)
        self.fromAddressLineEdit.setObjectName("fromAddressLineEdit")
        self.gridLayout.addWidget(self.fromAddressLineEdit, 4, 0, 1, 3)
        self.statusMsgCheckBox = QtWidgets.QCheckBox(self.notificationGroupBox)
        self.statusMsgCheckBox.setObjectName("statusMsgCheckBox")
        self.gridLayout.addWidget(self.statusMsgCheckBox, 10, 0, 1, 1)
        self.fromPasswordLabel = QtWidgets.QLabel(self.notificationGroupBox)
        self.fromPasswordLabel.setObjectName("fromPasswordLabel")
        self.gridLayout.addWidget(self.fromPasswordLabel, 5, 0, 1, 3)
        self.errorMsgCheckBox = QtWidgets.QCheckBox(self.notificationGroupBox)
        self.errorMsgCheckBox.setObjectName("errorMsgCheckBox")
        self.gridLayout.addWidget(self.errorMsgCheckBox, 9, 0, 1, 1)
        self.frequencyLabel = QtWidgets.QLabel(self.notificationGroupBox)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.gridLayout.addWidget(self.frequencyLabel, 10, 1, 1, 1)
        self.frequencySpinBox = QtWidgets.QSpinBox(self.notificationGroupBox)
        self.frequencySpinBox.setObjectName("frequencySpinBox")
        self.gridLayout.addWidget(self.frequencySpinBox, 10, 2, 1, 1)
        self.toAddressLabel = QtWidgets.QLabel(self.notificationGroupBox)
        self.toAddressLabel.setObjectName("toAddressLabel")
        self.gridLayout.addWidget(self.toAddressLabel, 7, 0, 1, 3)
        self.smtpServerLabel = QtWidgets.QLabel(self.notificationGroupBox)
        self.smtpServerLabel.setObjectName("smtpServerLabel")
        self.gridLayout.addWidget(self.smtpServerLabel, 1, 0, 1, 3)
        self.fromAddressLabel = QtWidgets.QLabel(self.notificationGroupBox)
        self.fromAddressLabel.setObjectName("fromAddressLabel")
        self.gridLayout.addWidget(self.fromAddressLabel, 3, 0, 1, 3)
        self.toAddressLineEdit = QtWidgets.QLineEdit(self.notificationGroupBox)
        self.toAddressLineEdit.setObjectName("toAddressLineEdit")
        self.gridLayout.addWidget(self.toAddressLineEdit, 8, 0, 1, 3)
        self.smtpServerLineEdit = QtWidgets.QLineEdit(self.notificationGroupBox)
        self.smtpServerLineEdit.setText("")
        self.smtpServerLineEdit.setObjectName("smtpServerLineEdit")
        self.gridLayout.addWidget(self.smtpServerLineEdit, 2, 0, 1, 3)
        self.fromPasswordLineEdit = QtWidgets.QLineEdit(self.notificationGroupBox)
        self.fromPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.fromPasswordLineEdit.setObjectName("fromPasswordLineEdit")
        self.gridLayout.addWidget(self.fromPasswordLineEdit, 6, 0, 1, 3)
        self.GroupBox = QtWidgets.QGroupBox(self.notificationGroupBox)
        self.GroupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.GroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.GroupBox, 12, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 0, 1, 1)
        self.warningsGroupBox = QtWidgets.QGroupBox(self.notificationGroupBox)
        self.warningsGroupBox.setObjectName("warningsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.warningsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.numWarningsToPause = QtWidgets.QSpinBox(self.warningsGroupBox)
        self.numWarningsToPause.setMinimum(1)
        self.numWarningsToPause.setObjectName("numWarningsToPause")
        self.gridLayout_2.addWidget(self.numWarningsToPause, 1, 0, 1, 1)
        self.numWarningsToPauseLabel = QtWidgets.QLabel(self.warningsGroupBox)
        self.numWarningsToPauseLabel.setObjectName("numWarningsToPauseLabel")
        self.gridLayout_2.addWidget(self.numWarningsToPauseLabel, 1, 1, 1, 1)
        self.clearWarningsPushButton = QtWidgets.QPushButton(self.warningsGroupBox)
        self.clearWarningsPushButton.setObjectName("clearWarningsPushButton")
        self.gridLayout_2.addWidget(self.clearWarningsPushButton, 2, 0, 1, 1)
        self.currentWarnings = DaveWarningsViewer(self.warningsGroupBox)
        self.currentWarnings.setObjectName("currentWarnings")
        self.gridLayout_2.addWidget(self.currentWarnings, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.warningsGroupBox, 13, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.notificationGroupBox)
        self.mainGridLayout.addWidget(self.widget, 1, 4, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.commandGroupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandGroupBox.sizePolicy().hasHeightForWidth())
        self.commandGroupBox.setSizePolicy(sizePolicy)
        self.commandGroupBox.setObjectName("commandGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.commandGroupBox)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.commandSequenceTreeView = DaveCommandTreeViewer(self.commandGroupBox)
        self.commandSequenceTreeView.setObjectName("commandSequenceTreeView")
        self.verticalLayout_3.addWidget(self.commandSequenceTreeView)
        self.verticalLayout_7.addWidget(self.commandGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 185))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.commandTableView = QtWidgets.QTableView(self.groupBox)
        self.commandTableView.setMaximumSize(QtCore.QSize(16777215, 150))
        self.commandTableView.setShowGrid(False)
        self.commandTableView.setObjectName("commandTableView")
        self.commandTableView.horizontalHeader().setVisible(False)
        self.commandTableView.horizontalHeader().setDefaultSectionSize(100)
        self.commandTableView.verticalHeader().setVisible(False)
        self.commandTableView.verticalHeader().setDefaultSectionSize(17)
        self.verticalLayout_6.addWidget(self.commandTableView)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtWidgets.QPushButton(self.widget_3)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.abortButton = QtWidgets.QPushButton(self.widget_3)
        self.abortButton.setObjectName("abortButton")
        self.horizontalLayout.addWidget(self.abortButton)
        self.validateSequenceButton = QtWidgets.QPushButton(self.widget_3)
        self.validateSequenceButton.setObjectName("validateSequenceButton")
        self.horizontalLayout.addWidget(self.validateSequenceButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addWidget(self.widget_3)
        self.mainGridLayout.addWidget(self.widget_2, 1, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuXML = QtWidgets.QMenu(self.menubar)
        self.menuXML.setObjectName("menuXML")
        self.menuNotifications = QtWidgets.QMenu(self.menubar)
        self.menuNotifications.setObjectName("menuNotifications")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Sequence = QtWidgets.QAction(MainWindow)
        self.actionNew_Sequence.setObjectName("actionNew_Sequence")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionGenerate = QtWidgets.QAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionGenerateXML = QtWidgets.QAction(MainWindow)
        self.actionGenerateXML.setObjectName("actionGenerateXML")
        self.actionSendTestEmail = QtWidgets.QAction(MainWindow)
        self.actionSendTestEmail.setObjectName("actionSendTestEmail")
        self.menuFile.addAction(self.actionNew_Sequence)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuXML.addAction(self.actionGenerateXML)
        self.menuNotifications.addAction(self.actionSendTestEmail)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuXML.menuAction())
        self.menubar.addAction(self.menuNotifications.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dave"))
        self.sequenceGroupBox.setTitle(_translate("MainWindow", "Sequence File"))
        self.sequenceLabel.setText(_translate("MainWindow", "NA"))
        self.notificationGroupBox.setTitle(_translate("MainWindow", "Notifications"))
        self.estimatesGroupBox.setTitle(_translate("MainWindow", "Estimates"))
        self.spaceLabel.setText(_translate("MainWindow", "TextLabel"))
        self.timeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.remainingLabel.setText(_translate("MainWindow", "TextLabel"))
        self.statusMsgCheckBox.setText(_translate("MainWindow", "e-mail status messages"))
        self.fromPasswordLabel.setText(_translate("MainWindow", "From password:"))
        self.errorMsgCheckBox.setText(_translate("MainWindow", "e-mail error messages"))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency:"))
        self.toAddressLabel.setText(_translate("MainWindow", "To address:"))
        self.smtpServerLabel.setText(_translate("MainWindow", "SMTP server:"))
        self.fromAddressLabel.setText(_translate("MainWindow", "From address:"))
        self.GroupBox.setTitle(_translate("MainWindow", "Sequence Progress"))
        self.warningsGroupBox.setTitle(_translate("MainWindow", "Warnings"))
        self.numWarningsToPauseLabel.setText(_translate("MainWindow", "Number of Warnings  to Pause"))
        self.clearWarningsPushButton.setText(_translate("MainWindow", "Clear Warnings"))
        self.commandGroupBox.setTitle(_translate("MainWindow", "Command Sequence"))
        self.groupBox.setTitle(_translate("MainWindow", "Command Details"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.abortButton.setText(_translate("MainWindow", "Abort"))
        self.validateSequenceButton.setText(_translate("MainWindow", "Validate"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuXML.setTitle(_translate("MainWindow", "&XML"))
        self.menuNotifications.setTitle(_translate("MainWindow", "&Notifications"))
        self.actionNew_Sequence.setText(_translate("MainWindow", "&Load Sequence"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionGenerate.setText(_translate("MainWindow", "Generate (Version 1.0)"))
        self.actionGenerateXML.setText(_translate("MainWindow", "&Generate XML"))
        self.actionSendTestEmail.setText(_translate("MainWindow", "&Send Test Email"))

from storm_control.dave.daveWarnings import DaveWarningsViewer
from storm_control.dave.sequenceViewer import DaveCommandTreeViewer
