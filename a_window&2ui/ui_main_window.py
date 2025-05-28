# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(699, 621)
        self.actionQuit = QAction(main_window)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bottom_bar = QWidget(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 30))
        self.bottom_bar.setMaximumSize(QSize(16777215, 30))
        self.bottom_bar.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border-top: 2px solid gray;\n"
"}")

        self.gridLayout.addWidget(self.bottom_bar, 1, 0, 1, 3)

        self.widget_menu = QWidget(self.centralwidget)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setBaseSize(QSize(640, 640))
        self.widget_menu.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.widget_menu)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.gridLayout.addWidget(self.widget_menu, 0, 1, 1, 2)

        self.widget_content = QWidget(self.centralwidget)
        self.widget_content.setObjectName(u"widget_content")
        self.widget_content.setMaximumSize(QSize(150, 16777215))
        self.widget_content.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(153, 153, 153);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_content)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.widget_content)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_content)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.widget_content)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget_content, 0, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 699, 22))
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        main_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("main_window", u"Quit", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_window", u"Clear", None))
        self.pushButton_3.setText(QCoreApplication.translate("main_window", u"Next Page", None))
        self.pushButton.setText(QCoreApplication.translate("main_window", u"Welcome", None))
        self.menu.setTitle(QCoreApplication.translate("main_window", u"Seeting", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
    # retranslateUi

