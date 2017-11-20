# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 770)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.reset_btn = QtWidgets.QPushButton(self.widget_3)
        self.reset_btn.setEnabled(False)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_btn.setObjectName("reset_btn")
        self.gridLayout.addWidget(self.reset_btn, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.start_btn = QtWidgets.QPushButton(self.widget_3)
        self.start_btn.setEnabled(False)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.gridLayout.addWidget(self.start_btn, 4, 1, 1, 1)
        self.mutation_prob = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.mutation_prob.setMinimumSize(QtCore.QSize(0, 30))
        self.mutation_prob.setAccelerated(True)
        self.mutation_prob.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.mutation_prob.setDecimals(4)
        self.mutation_prob.setMaximum(1.0)
        self.mutation_prob.setSingleStep(0.001)
        self.mutation_prob.setProperty("value", 0.001)
        self.mutation_prob.setObjectName("mutation_prob")
        self.gridLayout.addWidget(self.mutation_prob, 2, 1, 1, 1)
        self.apply_btn = QtWidgets.QPushButton(self.widget_3)
        self.apply_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_btn.setObjectName("apply_btn")
        self.gridLayout.addWidget(self.apply_btn, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.iterations = QtWidgets.QSpinBox(self.widget_3)
        self.iterations.setMinimumSize(QtCore.QSize(0, 30))
        self.iterations.setAccelerated(True)
        self.iterations.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.iterations.setMinimum(1)
        self.iterations.setMaximum(1000)
        self.iterations.setProperty("value", 100)
        self.iterations.setObjectName("iterations")
        self.gridLayout.addWidget(self.iterations, 1, 1, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.widget_3)
        self.next_btn.setEnabled(False)
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.size = QtWidgets.QSpinBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.size.sizePolicy().hasHeightForWidth())
        self.size.setSizePolicy(sizePolicy)
        self.size.setMinimumSize(QtCore.QSize(0, 30))
        self.size.setAccelerated(True)
        self.size.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.size.setMinimum(2)
        self.size.setMaximum(1000)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(self.widget_3)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout.addWidget(self.stop_btn, 5, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 40)
        self.gridLayout.setRowMinimumHeight(1, 40)
        self.gridLayout.setRowMinimumHeight(2, 40)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 10)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addWidget(self.widget)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_2)
        self.top_frame = QtWidgets.QWidget(self.centralwidget)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout.addWidget(self.top_frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_frame = QtWidgets.QWidget(self.centralwidget)
        self.left_frame.setObjectName("left_frame")
        self.horizontalLayout_2.addWidget(self.left_frame)
        self.right_frame = QtWidgets.QWidget(self.centralwidget)
        self.right_frame.setObjectName("right_frame")
        self.horizontalLayout_2.addWidget(self.right_frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progress_bar_text = QtWidgets.QLabel(self.centralwidget)
        self.progress_bar_text.setObjectName("progress_bar_text")
        self.verticalLayout_4.addWidget(self.progress_bar_text)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 12))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 19))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.progressBar = QtWidgets.QProgressBar(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 19))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.progressBar.raise_()
        self.progressBar.raise_()
        self.verticalLayout_4.addWidget(self.widget_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.setStretch(0, 40)
        self.verticalLayout_3.setStretch(1, 60)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
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
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Size"))
        self.start_btn.setText(_translate("MainWindow", "Start auto"))
        self.apply_btn.setText(_translate("MainWindow", "Apply"))
        self.label_3.setText(_translate("MainWindow", "Mutation probability"))
        self.next_btn.setText(_translate("MainWindow", "Next step"))
        self.label_2.setText(_translate("MainWindow", "Iterations"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.progress_bar_text.setText(_translate("MainWindow", "Ready"))
