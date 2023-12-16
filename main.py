import sys
import json
import random
import codecs
import math
from PIL import Image
from PySide2.QtWidgets import *
from ui_gui import Ui_gui


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lock_bottom.clicked.connect(self.lock)
        self.unlock_bottom.clicked.connect(self.unlock)

        self.show()

    def text2rgb(self, value):
        value = '0'*(8-len(hex(ord(value))))+hex(ord(value))[2:]
        return (int(value[0:2], 16), int(value[2: 4], 16), random.randint(0,255))

    def rgb2text(self, value):
        value = ''.join(['0'*(4-len(hex(temp)))+hex(temp)[2:]for temp in value])
        return chr(int(value[:4], 16))

    def lock(self):
        if self.open_format.currentIndex() < 17:
            name = QFileDialog.getOpenFileName(caption='打开文件')[0]
            with codecs.open(name, 'r', encoding=self.open_format.currentText())as path:
                file = path.read()
        else:
            name = QFileDialog.getOpenFileName(
                caption='打开文件', filter=f'(*.{self.open_format.currentText()})')[0]
            temp = Image.open(name).convert('RGB')
            data = []
            for y in range(temp.height):
                for x in range(temp.width):
                    data.append(self.rgb2text(temp.getpixel((x, y))))
            file = ''.join(data)

        keys, values = [], []
        for temp in file:
            if temp not in keys:
                keys.append(temp)
                values.append(temp)
        data = {}
        random.shuffle(values)
        for index in range(len(keys)):
            data[keys[index]] = values[index]
        code = ''
        for temp in file:
            code += data[temp]
        data['name'] = name
        data['data'] = code

        if self.save_format.currentIndex() < 17:
            with codecs.open(QFileDialog.getSaveFileName(caption='保存文件', filter='(*.sljm)')[0], 'w', encoding='utf-8')as path:
                json.dump(data, path)
        else:
            file = data.pop('data')
            file = [self.text2rgb(temp) for temp in file]
            length = math.ceil(len(file)**0.5)
            img=Image.new('RGB',(length,length))
            for y in range(length):
                for x in range(length):
                    if x*length+y<len(file):
                        img.putpixel((x,y),file[x*length+y])
            name = QFileDialog.getSaveFileName(
                caption='保存文件', filter=f'(*.{self.save_format.currentText()})')[0]
            if name[-3:] in ['png', 'bmp']:
                img = img.convert('RGBA')
            img.save(name)
            with codecs.open(name[:-3]+'sljm','w',encoding='utf-8')as file:
                json.dump(data,file)

    def unlock(self):
        if self.open_format.currentIndex() < 17:
            name=QFileDialog.getOpenFileName(caption='打开文件', filter='(*.sljm)')[0]
            with codecs.open(name, 'r', encoding='utf-8')as path:
                file = json.load(path)
        else:
            data = Image.open()
            code = file.pop('data')
            data = {}
            for index in range(len(file)):
                data[list(file.values())[index]] = list(file.keys())[index]
            text = ''
            for temp in code:
                text += data[temp]
            with codecs.open(QFileDialog.getSaveFileName(caption='保存文件')[0], 'w', encoding=self.save_format.currentText())as path:
                path.write(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
