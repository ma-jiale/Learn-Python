# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_2.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_window_2(object):
    def setupUi(self, window_2):
        if not window_2.objectName():
            window_2.setObjectName(u"window_2")
        window_2.resize(637, 309)
        window_2.setBaseSize(QSize(640, 640))
        self.actionQuit = QAction(window_2)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(window_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 90, 241, 16))
        window_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(window_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 637, 22))
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        window_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window_2)
        self.statusbar.setObjectName(u"statusbar")
        window_2.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(window_2)

        QMetaObject.connectSlotsByName(window_2)
    # setupUi

    def retranslateUi(self, window_2):
        window_2.setWindowTitle(QCoreApplication.translate("window_2", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("window_2", u"Quit", None))
        self.label.setText(QCoreApplication.translate("window_2", u"Hahaha, you can's go back!", None))
        self.menuSetting.setTitle(QCoreApplication.translate("window_2", u"Setting", None))
        self.menuFile.setTitle(QCoreApplication.translate("window_2", u"File", None))
    # retranslateUi

