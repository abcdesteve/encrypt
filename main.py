import os
import sys
import json
import numpy as np
from PIL import Image
from sljm_core_1_2 import *

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qdarkstyle
from qt_material import apply_stylesheet

from ui_gui import Ui_gui
from ui_tab_txt import Ui_tab_txt
from ui_tab_pic import Ui_tab_pic
from ui_tab_settings import Ui_settings


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tab_txt = Ui_tab_txt()
        self.tab_txt.setupUi(self.tab_1)
        self.tab_pic = Ui_tab_pic()
        self.tab_pic.setupUi(self.tab_2)
        self.tab_settings = Ui_settings()
        self.tab_settings.setupUi(self.tab_3)

        self.tabWidget.currentChanged.connect(self.window_size_change)
        self.window_size_change()

        # load settings
        self.load_settings()

        # txt
        self.textedit_flag = 'decript'
        self.tab_txt.textedit_decripted.textChanged.connect(
            self.updata_last_decript)
        self.tab_txt.textedit_encripted.textChanged.connect(
            self.updata_last_encript)
        self.tab_txt.lineedit_key.textChanged.connect(self.updata_txt)
        # picture
        self.pic_dic = {}
        self.tab_pic.btn_decript_select.clicked.connect(
            lambda: self.picture_select(self.tab_pic.label_decript))
        self.tab_pic.btn_encript_select.clicked.connect(
            lambda: self.picture_select(self.tab_pic.label_encript))
        self.tab_pic.btn_decript_save.clicked.connect(
            lambda: self.picture_save(self.tab_pic.label_decript))
        self.tab_pic.btn_encript_save.clicked.connect(
            lambda: self.picture_save(self.tab_pic.label_encript))
        # settings
        self.tab_settings.radio_light.clicked.connect(
            self.settings_change_status)
        self.tab_settings.radio_dark.clicked.connect(
            self.settings_change_status)
        self.tab_settings.radio_colorful.clicked.connect(
            self.settings_change_status)
        self.tab_settings.ckb_enable_animation.clicked.connect(
            self.settings_change_status)
        self.tab_settings.cmb_theme.currentTextChanged.connect(
            self.settings_change_status)
        self.tab_settings.cmb_animation.currentTextChanged.connect(
            self.settings_change_status)
        self.tab_settings.animation_example.clicked.connect(
            self.settings_perform_animation)

        self.show()

    def load_settings(self):
        if os.path.isfile(os.path.join(path, '神龙加密', 'settings.json')):
            with open(os.path.join(path, '神龙加密', 'settings.json'), 'r')as file:
                data = json.load(file)
            {'light': self.tab_settings.radio_light, 'dark': self.tab_settings.radio_dark,
                'colorful': self.tab_settings.radio_colorful}[data['theme'][0]].setChecked(True)
            self.tab_settings.cmb_theme.setCurrentText(data['theme'][1])
            self.tab_settings.ckb_enable_animation.setChecked(
                data['animation'][0])
            self.tab_settings.cmb_animation.setCurrentText(
                data['animation'][1])
            self.settings_change_status(False)
        else:
            try:
                os.mkdir(path)
            except:
                pass
            try:
                os.mkdir(os.path.join(path, '神龙加密'))
            except:
                pass

            with open(os.path.join(path, '神龙加密', 'settings.json'), 'w')as file:
                print('Successfully created the setting file')
        self.settings_change_status()

    def window_size_change(self):
        self.animation = QPropertyAnimation(self, b'size')
        if self.tab_settings.ckb_enable_animation.isChecked():
            self.animation.setDuration(500)
        else:
            self.animation.setDuration(0)
        self.animation.setEasingCurve(
            eval('QEasingCurve.'+self.tab_settings.cmb_animation.currentText()))
        match self.tabWidget.currentIndex():
            case 0:
                self.animation.setEndValue(QSize(600, 400))
            case 1:
                self.animation.setEndValue(QSize(800, 400))
            case 2:
                self.animation.setEndValue(QSize(400, 100))
        self.animation.start()
# txt

    def updata_last_decript(self):
        if self.tab_txt.textedit_decripted.hasFocus():
            self.textedit_flag = 'decript'
            self.updata_txt()

    def updata_last_encript(self):
        if self.tab_txt.textedit_encripted.hasFocus():
            self.textedit_flag = 'encript'
            self.updata_txt()

    def updata_txt(self):
        if self.textedit_flag == 'decript':
            if self.tab_txt.textedit_decripted.toPlainText() and not self.tab_txt.textedit_encripted.hasFocus():
                txt, hash_value = encript(
                    list(self.tab_txt.textedit_decripted.toPlainText()), self.tab_txt.lineedit_key.text())
                self.tab_txt.textedit_encripted.setPlainText(
                    ''.join(txt)+hash_value[:5])
                self.tab_txt.ckb_vertify.setChecked(True)
        else:
            if self.tab_txt.textedit_encripted.toPlainText() and not self.tab_txt.textedit_decripted.hasFocus():
                txt, hash_check = decript(list(self.tab_txt.textedit_encripted.toPlainText()[
                                          :-5]), self.tab_txt.lineedit_key.text())
                self.tab_txt.textedit_decripted.setPlainText(''.join(txt))
                self.tab_txt.ckb_vertify.setChecked(
                    hash_check[:5] == self.tab_txt.textedit_encripted.toPlainText()[-5:])

# picture
    def picture_select(self, pos: QLabel):
        pos = pos.objectName()
        path = QFileDialog.getOpenFileName(
            self, '请选择图片', filter=('图片文件 (*.jpg *.png *.bmp *.gif *.tif)' if pos=='label_decript' else '图片文件 (*.png *.bmp *.tif)'))[0]
        if path:
            pic = Image.open(path)
            self.pic_dic[pos] = pic
            # scale=min(pos.width()/pic.width,pos.height()/pic.height)
            # pos.setPixmap(pic.resize((int(pic.width*scale),int(pic.height*scale))).toqpixmap())
            if pos == 'label_decript':
                width, height, factor = hex(pic.width)[2:].rjust(6, '0'), hex(pic.height)[
                    2:].rjust(6, '0'), nearest_factor_decomposition(pic.width*pic.height)[0]
                data = np.array(pic.getdata(), np.uint8).reshape([-1, factor, 3])
                print('初始化完成，源数据', data.shape, width, height)
                data, hash_value = encript(data.tolist(), self.tab_pic.lineedit_password.text())
                print('加密完成')

                data = np.concatenate([np.zeros(12,np.uint8),data])

                # create empty data to fit picture size
                empty = 0
                while True:
                    a, b = nearest_factor_decomposition((len(data)+empty*3)//3)
                    if abs(a-b)/min(a, b) <= 2:  # worst 1:3
                        break
                    empty += 1
                data[0:3]=hex2rgb(width)
                data[3:6]=hex2rgb(height)
                data[6:9]=hex2rgb(hex(factor)[2:].rjust(6,'0'))
                data[9:12]=hex2rgb(hex(empty)[2:].rjust(6,'0'))
                print('加密参数生成完成',width,height,factor,empty)

                process = np.append(data,np.zeros(empty*3,np.uint8)).reshape([-1, a, 3])
                self.pic_dic['label_encript'] = Image.fromarray(np.uint8(process))
            else:
                data = np.array(pic.getdata(), np.uint8).reshape([-1, 3])
                width, height, factor,empty = int(rgb2hex(data[0]), 16), int(
                    rgb2hex(data[1]), 16), int(rgb2hex(data[2]), 16),int(rgb2hex(data[3]), 16)
                print('初始化完成，源数据', data.shape, width, height)
                data = (data[4:-empty] if empty else data[4:]).reshape([-1, factor, 3])
                data, hash_value = decript(
                    data.tolist(), self.tab_pic.lineedit_password.text())
                print('解密完成')
                self.pic_dic['label_decript'] = Image.fromarray(
                    np.uint8(data.reshape([height, width, 3])))

            self.picture_update()
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def picture_update(self):
        if self.tab_pic.label_decript.objectName() in self.pic_dic.keys():
            self.tab_pic.label_decript.setPixmap(
                self.pic_dic[self.tab_pic.label_decript.objectName()].resize((320, 180)).toqpixmap())
        if self.tab_pic.label_encript.objectName() in self.pic_dic.keys():
            self.tab_pic.label_encript.setPixmap(
                self.pic_dic[self.tab_pic.label_encript.objectName()].resize((320, 180)).toqpixmap())

    def picture_save(self, pos: QLabel):
        pos = pos.objectName()
        if pos in self.pic_dic.keys():
            path = QFileDialog.getSaveFileName(
                self, '请选择图片保存位置', filter=('图片文件 (*.jpg *.png *.bmp *.tif *.gif)' if pos=='label_decript' else '图片文件 (*.png *.bmp *.tif)'))[0]
            if path:
                self.pic_dic[pos].save(path)
            else:
                QMessageBox.warning(self, '警告', '路径无效')
        else:
            QMessageBox.warning(self, '警告', '请先打开一张图片')
# settings

    def settings_change_status(self, flag=True):
        # update status
        if self.tab_settings.radio_colorful.isChecked():
            self.tab_settings.cmb_theme.setEnabled(True)
        else:
            self.tab_settings.cmb_theme.setEnabled(False)
        if self.tab_settings.ckb_enable_animation.isChecked():
            self.tab_settings.cmb_animation.setEnabled(True)
        else:
            self.tab_settings.cmb_animation.setEnabled(False)

        if self.tab_settings.radio_dark.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
        elif self.tab_settings.radio_colorful.isChecked():
            apply_stylesheet(
                app, self.tab_settings.cmb_theme.currentText()+'.xml')

        # update profile
        data = {'theme': [[i for i in [self.tab_settings.radio_light, self.tab_settings.radio_dark, self.tab_settings.radio_colorful] if i.isChecked()][0].objectName()[6:], self.tab_settings.cmb_theme.currentText()],
                'animation': [self.tab_settings.ckb_enable_animation.isChecked(), self.tab_settings.cmb_animation.currentText()]}
        with open(os.path.join(path, '神龙加密', 'settings.json'), 'w')as file:
            json.dump(data, file)

        if flag:
            self.settings_perform_animation()

    def settings_perform_animation(self):
        self.animation_example = QPropertyAnimation(
            self.tab_settings.animation_example, b'pos')
        if self.tab_settings.ckb_enable_animation.isChecked():
            self.animation_example.setDuration(2000)
        else:
            self.animation_example.setDuration(0)
        self.animation_example.setStartValue(QPoint(10, 10))
        self.animation_example.setEndValue(
            QPoint(self.tab_settings.widget.width()-30, 10))
        self.animation_example.setEasingCurve(
            eval('QEasingCurve.'+self.tab_settings.cmb_animation.currentText()))
        self.animation_example.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = os.path.expandvars(r'%appdata%/Avoconal')
    window = Main()
    sys.exit(app.exec())
