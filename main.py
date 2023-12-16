import easygui
import random
import json
print('欢迎使用 神龙加密v1.1\nby abcdesteve\n\n待处理的文件请放在本程序的目录下!\n')
if easygui.ynbox('神龙加密\n作者：abcdesteve', '神龙加密v1.1', ('加密', '解密')):
    dic = {}
    key=[]
    with open(input('请输入要打开文件的文件名（带后缀名）：'), 'r', encoding='UTF-8')as read:
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
    with open(input('请输入要保存文件的文件名（不带后缀名）：')+'.sljm', 'w')as write:
        json.dump(dic, write)
else:
    dic={}
    data=''
    with open(input('请输入要打开文件的文件名（不带后缀名）：')+'.sljm', 'r')as read:
        temp = json.load(read)
    jsondata = temp.pop('data')
    for key in temp:
        dic[temp[key]]=key
    temp = 0
    for temp in jsondata:
        data=data+dic[temp]
    with open(input('请输入要保存文件的文件名（带后缀名）：'), 'w')as write:
        write.write(data)
