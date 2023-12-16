# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_pic.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_tab_pic(object):
    def setupUi(self, tab_pic):
        if not tab_pic.objectName():
            tab_pic.setObjectName(u"tab_pic")
        tab_pic.resize(400, 300)
        self.gridLayout = QGridLayout(tab_pic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_password = QLabel(tab_pic)
        self.label_password.setObjectName(u"label_password")

        self.horizontalLayout.addWidget(self.label_password)

        self.lineedit_password = QLineEdit(tab_pic)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineedit_password)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.btn_decript_select = QPushButton(tab_pic)
        self.btn_decript_select.setObjectName(u"btn_decript_select")

        self.gridLayout.addWidget(self.btn_decript_select, 1, 0, 1, 1)

        self.line = QFrame(tab_pic)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 3, 1)

        self.btn_encript_select = QPushButton(tab_pic)
        self.btn_encript_select.setObjectName(u"btn_encript_select")

        self.gridLayout.addWidget(self.btn_encript_select, 1, 2, 1, 1)

        self.btn_decript_save = QPushButton(tab_pic)
        self.btn_decript_save.setObjectName(u"btn_decript_save")

        self.gridLayout.addWidget(self.btn_decript_save, 2, 0, 1, 1)

        self.btn_encript_save = QPushButton(tab_pic)
        self.btn_encript_save.setObjectName(u"btn_encript_save")

        self.gridLayout.addWidget(self.btn_encript_save, 2, 2, 1, 1)

        self.label_decript = QLabel(tab_pic)
        self.label_decript.setObjectName(u"label_decript")
        self.label_decript.setScaledContents(True)
        self.label_decript.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_decript, 3, 0, 1, 1)

        self.label_encript = QLabel(tab_pic)
        self.label_encript.setObjectName(u"label_encript")
        self.label_encript.setScaledContents(True)
        self.label_encript.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_encript, 3, 2, 1, 1)


        self.retranslateUi(tab_pic)

        QMetaObject.connectSlotsByName(tab_pic)
    # setupUi

    def retranslateUi(self, tab_pic):
        tab_pic.setWindowTitle(QCoreApplication.translate("tab_pic", u"Form", None))
        self.label_password.setText(QCoreApplication.translate("tab_pic", u"\u5bc6\u94a5\uff1a", None))
        self.btn_decript_select.setText(QCoreApplication.translate("tab_pic", u"\u9009\u62e9\u56fe\u7247", None))
        self.btn_encript_select.setText(QCoreApplication.translate("tab_pic", u"\u9009\u62e9\u56fe\u7247", None))
        self.btn_decript_save.setText(QCoreApplication.translate("tab_pic", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.btn_encript_save.setText(QCoreApplication.translate("tab_pic", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.label_decript.setText(QCoreApplication.translate("tab_pic", u"\u89e3\u5bc6\u533a", None))
        self.label_encript.setText(QCoreApplication.translate("tab_pic", u"\u52a0\u5bc6\u533a", None))
    # retranslateUi

