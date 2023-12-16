import sys
import json
import random
import codecs
from PySide2.QtWidgets import *
from ui_gui import Ui_gui


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lock_bottom.clicked.connect(self.lock)
        self.unlock_bottom.clicked.connect(self.unlock)

        self.show()

    def lock(self):
        with codecs.open(QFileDialog.getOpenFileName(caption='打开文件')[0], 'r', encoding=self.open_format.currentText())as path:
            file = path.read()
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
        data['data'] = code
        with codecs.open(QFileDialog.getSaveFileName(caption='保存文件', filter='(*.sljm)')[0], 'w', encoding='utf-8')as path:
            json.dump(data, path)

    def unlock(self):
        with codecs.open(QFileDialog.getOpenFileName(caption='打开文件', filter='(*.sljm)')[0], 'r', encoding='utf-8')as path:
            file = json.load(path)
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
