# -*- coding:utf-8 -*-
from braille.__init__ import *
import copy
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.ttk import Combobox
from tkinter import messagebox

root=Tk()
root.title("汉盲转换")

frame0=Frame(root)

canvas0=Canvas(frame0)

frame1=Frame(canvas0, bg="#2fa4d9")

scroll=Scrollbar(canvas0,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll.configure(command=canvas0.yview)
canvas0.config(yscrollcommand=scroll.set)

text1=Text(frame1,width=80,height=20, bg="#3e454d", foreground = 'white')
text1.grid(row=1,column=0)
scroll1=Scrollbar(frame1,orient=VERTICAL)
scroll1.grid(row=1,column=1, sticky=S + W + E + N)
scroll1.config(command=text1.yview)
text1.config(yscrollcommand=scroll1.set)

text2=Text(frame1,width=80,height=20, bg="#3e454d", foreground = 'white')
text2.grid(row=3,column=0)
scroll2=Scrollbar(frame1,orient=VERTICAL)
scroll2.grid(row=3,column=1, sticky=S + W + E + N)
scroll2.config(command=text2.yview)
text2.config(yscrollcommand=scroll2.set)

text3=Text(frame1,width=80,height=20, bg="#3e454d", foreground = 'white')
text3.grid(row=1,column=3)
scroll3=Scrollbar(frame1,orient=VERTICAL)
scroll3.grid(row=1,column=4, sticky=S + W + N)
scroll3.config(command=text3.yview)
text3.config(yscrollcommand=scroll3.set)

text4=Text(frame1,width=80,height=20, bg="#3e454d", foreground = 'white')
text4.grid(row=3,column=3)
scroll4=Scrollbar(frame1,orient=VERTICAL)
scroll4.grid(row=3,column=4, sticky=S + W + N)
scroll4.config(command=text4.yview)
text4.config(yscrollcommand=scroll4.set)

label1=Label(frame1,text="输入待转换内容：", bg="#1d7ca7", foreground = 'white')
label1.grid(row=0,column=0)
label2=Label(frame1,text="分词结果：", bg="#1d7ca7", foreground = 'white')
label2.grid(row=2,column=0)
label3=Label(frame1,text="转换结果 点序：", bg="#1d7ca7", foreground = 'white')
label3.grid(row=0,column=3)
label4=Label(frame1,text="转换结果 二进制：", bg="#1d7ca7", foreground = 'white')
label4.grid(row=2,column=3)

Label(frame1,text="    ", bg="#2fa4d9").grid(row=1,column=2)

menubar = Menu(root,tearoff=False)

text1.bind("<Button-3>", lambda x: rightKey(x, text1))
text2.bind("<Button-3>", lambda x: rightKey(x, text2))
text3.bind("<Button-3>", lambda x: rightKey(x, text3))
text4.bind("<Button-3>", lambda x: rightKey(x, text4))


def cut(editor, event=None):
    editor.event_generate("<<Cut>>")
def tcopy(editor, event=None):
    editor.event_generate("<<Copy>>")
def paste(editor, event=None):
    editor.event_generate('<<Paste>>')
def rightKey(event, editor):
    menubar.delete(0,END)
    menubar.add_command(label='剪切', command=lambda: cut(editor))
    menubar.add_command(label='复制', command=lambda: tcopy(editor))
    menubar.add_command(label='粘贴', command=lambda: paste(editor))
    menubar.post(event.x_root, event.y_root)

def showCut():
    str=text1.get("0.0",END)
    newStr=cutWords(str)
    text2.delete("0.0", END)
    text2.insert("0.0",newStr)

def showBraille(str):
    list1=list(str)
    listPinyin=lazy_pinyin(list1, style=style)
    toBraille(listPinyin,text3)
    toBrailleB(text3, text4)
    #text3.insert("0.0",str)

def selectPath():
    path_ = askdirectory()
    if path_ != '':
        path.set(path_+"/braille.txt")
        pathB.set(path_+"/brailleB.txt")

def saveTxt():
    if path.get() != '' and pathB.get() != '':
        file=open(path.get(),"w",encoding='utf-8')
        file.write(text3.get("0.0",END))
        file.close()
        file = open(pathB.get(), "w", encoding='utf-8')
        file.write(text4.get("0.0", END))
        file.close()
    else:
        messagebox.showwarning('', '请选择正确的目录')

def addDict():
    addWin=Tk()
    addWin.title("添加词典")
    addWin.wm_attributes('-topmost',1) #窗口置顶

    Label(addWin, text="词汇").grid(row=0, column=0)
    Label(addWin, text="词性").grid(row=0, column=1)

    dictText=Text(addWin, width=20, height=1)
    partText = Combobox(addWin, width=16, state="readonly")
    partText['value'] = parts
    changePartText = Combobox(addWin, width=16, state="readonly")
    changePartText['value'] = parts
    changeText = Text(addWin, width=18, height=1)
    searchText = Text(addWin, width=18, height=1)

    dictText.bind("<Button-3>", lambda x: rightKey(x, dictText))
    changeText.bind("<Button-3>", lambda x: rightKey(x, changeText))
    searchText.bind("<Button-3>", lambda x: rightKey(x, searchText))

    partText.current(0)
    changePartText.current(0)

    dictText.grid(row=1, column=0)
    partText.grid(row=1, column=1)
    changeText.grid(row=3, column=0)
    changePartText.grid(row=3, column=1)
    searchText.grid(row=4, column=0)

    dictList = Listbox(addWin, exportselection = 0)
    partList = Listbox(addWin, exportselection = 0)
    dictList.grid(row=2, column=0)
    partList.grid(row=2, column=1)

    tempList = copy.deepcopy(userDictionary)  # 临时列表
    removedList = [] # 临时被删除列表

    def selectDict(event):
        partList.select_clear(0, END)
        curDictIndex = dictList.curselection()[0]
        partList.selection_set(curDictIndex)
        changeText.delete('0.0', END)
        changeText.insert('0.0', tempList[curDictIndex][0])
        curPart = list(partsDictionary.keys())[list(partsDictionary.values()).index(tempList[curDictIndex][1])]
        partIndex = parts.index(curPart)
        changePartText.current(partIndex)

    def selectPart(event):
        dictList.select_clear(0,END)
        curPartIndex = partList.curselection()[0]
        dictList.selection_set(curPartIndex)
        changeText.delete('0.0', END)
        changeText.insert('0.0', tempList[curPartIndex][0])
        curPart = list(partsDictionary.keys())[list(partsDictionary.values()).index(tempList[curPartIndex][1])]
        partIndex = parts.index(curPart)
        changePartText.current(partIndex)

    dictList.bind('<<ListboxSelect>>', selectDict)
    partList.bind('<<ListboxSelect>>', selectPart)

    def addUserDict():
        userDictsTurple = dictList.get(0, END) #列表框内容导出元组
        userDictName = dictText.get("0.0", END) #用户输入词
        userDictName = userDictName.replace('\n', '') #消除换行符
        userDictPart = partText.get() #用户输入词性
        if not (userDictName in userDictsTurple or userDictName == ''):
            dictList.insert(0, userDictName)
            partList.insert(0, userDictPart)
            tempList.insert(0, [userDictName, partsDictionary.get(userDictPart)])
            dictText.delete("0.0", END)
            partText.current(0)

    def deleteUserDict():
        if dictList.curselection() != ():
            curDictIndex = dictList.curselection()[0]
            dictList.delete(curDictIndex)
            partList.delete(curDictIndex)
            removedList.append(tempList.pop(curDictIndex)[0])

    def changeUserDict():
        if dictList.curselection() != () and changeText.get('0.0', END).replace('\n', '') != '':
            curDictIndex = dictList.curselection()[0]
            curDict = tempList[curDictIndex]
            changeDict = changeText.get('0.0',END).replace('\n', '')
            changePart = changePartText.get()
            if (not changeDict in dictList.get(0, END)) or (changeDict == curDict[0] and partsDictionary.get(changePart) != curDict[1]):
                dictList.delete(curDictIndex)
                partList.delete(curDictIndex)
                dictList.insert(curDictIndex, changeDict)
                partList.insert(curDictIndex, changePart)
                curDict[0] = changeDict
                curDict[1] = partsDictionary.get(changePart)

    def searchUserDict():
        dictList.select_clear(0, END)
        partList.select_clear(0, END)
        userDictsTurple = dictList.get(0, END)
        userDictName = searchText.get("0.0", END)
        userDictName = userDictName.replace('\n', '')
        if userDictName in userDictsTurple:
            dictIndex = userDictsTurple.index(userDictName)
            dictList.selection_set(dictIndex)
            dictList.see(dictIndex)
            partList.selection_set(dictIndex)
            partList.see(dictIndex)
        else:
            messagebox.showwarning('', '未找到该词汇')

    def saveUserDict():
        global userDictionary
        userDictionary = copy.deepcopy(tempList)
        userDictFile = open("userDict.txt", 'w', encoding='utf-8')
        for userDict in userDictionary:
            userDictFile.write(userDict[0]+' '+userDict[1]+'\n')
        userDictFile.close()
        jieba.load_userdict("userDict.txt")
        if len(removedList) != 0:
            for w in removedList:
                jieba.del_word(w)
            removedList.clear()

    Button(addWin, text="添加", command=addUserDict).grid(row=1, column=2)
    Button(addWin, text="修改", command=changeUserDict).grid(row=3, column=2)
    Button(addWin, text="查找", command=searchUserDict).grid(row=4, column=1, sticky='w')
    Button(addWin, text="删除", command=deleteUserDict).grid(row=5, column=2)
    Button(addWin, text="保存", command=saveUserDict).grid(row=6, column=1)

    def Wheel(event):  # 鼠标滚轮动作
        dictList.yview_scroll(int(-1 * (event.delta / 120)), "units")
        partList.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def ScrollCommand(*xx):  # 在滚动条上点击、拖动等动作
        dictList.yview(*xx)
        partList.yview(*xx)

    scrollbar1 = Scrollbar(addWin, orient="vertical", command=ScrollCommand)
    dictList.configure(yscrollcommand=scrollbar1.set)
    scrollbar1.grid(row=2, column=2, sticky='ns')
    for userDicts in userDictionary:
        dictList.insert(END, userDicts[0])  # 便于展示效果
        partList.insert(END, list(partsDictionary.keys())[list(partsDictionary.values()).index(userDicts[1])])
    dictList.bind("<MouseWheel>", Wheel)
    partList.bind("<MouseWheel>", Wheel)
    scrollbar1.bind("<MouseWheel>", Wheel)

    mainloop()

path=StringVar()
pathB=StringVar()

Button(frame1,text="分词",command=showCut, bg="#53b4df", foreground = 'white').grid(row=5,column=0,pady=10)
Button(frame1,text="转换",command=lambda :showBraille(text2.get("0.0",END)), bg="#53b4df", foreground = 'white').grid(row=5,column=3,sticky=N)

path1 = Entry(frame1, width=50, textvariable=path, bg="#3e454d", foreground = 'white')
path2 = Entry(frame1, width=50, textvariable=pathB, bg="#3e454d", foreground = 'white')
path1.bind("<Button-3>", lambda x: rightKey(x, path1))
path2.bind("<Button-3>", lambda x: rightKey(x, path2))
path1.grid(row=6, column=3,sticky=E)
path2.grid(row=7, column=3,sticky=E)
Button(frame1, text= "选择路径", command= selectPath, bg="#53b4df", foreground = 'white').grid(row=6,column=4,sticky=W)
Button(frame1, text= "转换结果保存为txt", command= saveTxt, bg="#53b4df", foreground = 'white').grid(row=8,column=3,sticky=S)
Button(frame1, text="添加词典", command=addDict, bg="#53b4df", foreground = 'white').grid(row=7, column=0)

frame1.pack()

canvas0.pack()

frame0.pack()

mainloop()