import tkinter
import random
import json
import tkinter.filedialog
def lock():
    dic = {}
    key=[]
    with open(tkinter.filedialog.askopenfilename(filetypes=[('All File', '*')]), 'r', encoding='utf-8')as read:
        data = read.read()
    allkey=''
    for temp in data:
        if temp not in allkey:
            allkey+=temp
    temp = 0
    for temp in allkey:
        key.append(temp)
    temp = 0
    for temp in allkey:
        dic[temp] = random.choice(key)
        key.remove(dic[temp])   
    jsondata=''
    temp = 0
    for temp in data:
        jsondata=jsondata+dic[temp]
    dic['data']=jsondata
    with open(tkinter.filedialog.asksaveasfilename(filetypes=[('神龙加密文件', '*.sljm')]), 'w', encoding='utf-8')as write:
        json.dump(dic, write)
def unlock():
    dic={}
    data=''
    with open(tkinter.filedialog.askopenfilename(filetypes=[('神龙加密文件', '*.sljm')]), 'r', encoding='utf-8')as read:
              temp = json.load(read)
    jsondata = temp.pop('data')
    for key in temp:
        dic[temp[key]]=key
    temp = 0
    for temp in jsondata:
        data=data+dic[temp]
    with open(tkinter.filedialog.asksaveasfilename(filetypes=[('All File', '*')]), 'w', encoding='utf-8')as write:
        write.write(data)
win = tkinter.Tk()
win.title('神龙加密v1.2')
text = tkinter.Label(win, text='欢迎使用 神龙加密v1.2\nby abcdesteve\n')
text.pack()
b1 = tkinter.Button(win, text='加密',command=lock)
b1.pack()
b2 = tkinter.Button(win, text='解密',command=unlock)
b2.pack()
win.mainloop()
