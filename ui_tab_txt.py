# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_txt.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_tab_txt(object):
    def setupUi(self, tab_txt):
        if not tab_txt.objectName():
            tab_txt.setObjectName(u"tab_txt")
        tab_txt.resize(400, 300)
        self.gridLayout = QGridLayout(tab_txt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_decripted = QLabel(tab_txt)
        self.label_decripted.setObjectName(u"label_decripted")

        self.gridLayout.addWidget(self.label_decripted, 0, 0, 1, 1)

        self.textedit_decripted = QPlainTextEdit(tab_txt)
        self.textedit_decripted.setObjectName(u"textedit_decripted")

        self.gridLayout.addWidget(self.textedit_decripted, 0, 1, 1, 2)

        self.label_key = QLabel(tab_txt)
        self.label_key.setObjectName(u"label_key")

        self.gridLayout.addWidget(self.label_key, 1, 0, 1, 1)

        self.lineedit_key = QLineEdit(tab_txt)
        self.lineedit_key.setObjectName(u"lineedit_key")
        self.lineedit_key.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_key, 1, 1, 1, 1)

        self.ckb_vertify = QCheckBox(tab_txt)
        self.ckb_vertify.setObjectName(u"ckb_vertify")
        self.ckb_vertify.setEnabled(False)

        self.gridLayout.addWidget(self.ckb_vertify, 1, 2, 1, 1)

        self.label_encripted = QLabel(tab_txt)
        self.label_encripted.setObjectName(u"label_encripted")

        self.gridLayout.addWidget(self.label_encripted, 2, 0, 1, 1)

        self.textedit_encripted = QPlainTextEdit(tab_txt)
        self.textedit_encripted.setObjectName(u"textedit_encripted")

        self.gridLayout.addWidget(self.textedit_encripted, 2, 1, 1, 2)


        self.retranslateUi(tab_txt)

        QMetaObject.connectSlotsByName(tab_txt)
    # setupUi

    def retranslateUi(self, tab_txt):
        tab_txt.setWindowTitle(QCoreApplication.translate("tab_txt", u"Form", None))
        self.label_decripted.setText(QCoreApplication.translate("tab_txt", u"\u539f\u6587\uff1a", None))
        self.label_key.setText(QCoreApplication.translate("tab_txt", u"\u5bc6\u94a5\uff1a", None))
        self.ckb_vertify.setText(QCoreApplication.translate("tab_txt", u"\u539f\u6587\u6821\u9a8c", None))
        self.label_encripted.setText(QCoreApplication.translate("tab_txt", u"\u5bc6\u6587\uff1a", None))
    # retranslateUi

