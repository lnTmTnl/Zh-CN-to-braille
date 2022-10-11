# -*- coding:utf-8 -*-
from braille.__init__ import *
from tkinter import *
from tkinter.filedialog import askdirectory

root=Tk()
root.title("汉盲转换")

canvas0=Canvas(root)

frame0=Frame(canvas0)

scroll=Scrollbar(canvas0,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll.configure(command=canvas0.yview)

text1=Text(frame0,width=100,height=30)
text1.grid(row=1,column=0)
text2=Text(frame0,width=100,height=20)
text2.grid(row=3,column=0,rowspan=2)
text3=Text(frame0,width=100,height=30)
text3.grid(row=1,column=1,columnspan=2)
label1=Label(frame0,text="输入待转换内容：")
label1.grid(row=0,column=0)
label2=Label(frame0,text="分词结果：")
label2.grid(row=2,column=0)
label3=Label(frame0,text="转换结果：")
label3.grid(row=0,column=1)

def showCut():
    str=text1.get("0.0",END)
    newStr=cutWords(str)
    text2.insert("0.0",newStr)

def showBraille(str):
    list1=list(str)
    listPinyin=lazy_pinyin(list1, style=style)
    toBraille(listPinyin,text3)
    #text3.insert("0.0",str)

def selectPath():
    path_ = askdirectory()
    path.set(path_+"/braille.txt")

path=StringVar()

def saveTxt():
    file=open(path.get(),"w",encoding='utf-8')
    file.write(text3.get("0.0",END))
    file.close()

Button(frame0,text="分词",command=showCut).grid(row=5,column=0,pady=10)
Button(frame0,text="转换",command=lambda :showBraille(text2.get("0.0",END))).grid(row=2,column=1,sticky=N)

Entry(frame0, width=50, textvariable=path).grid(row=3, column=1,sticky=E)
Button(frame0, text= "选择路径", command= selectPath).grid(row=3,column=2,sticky=W)
Button(frame0, text= "转换结果保存为txt", command= saveTxt).grid(row=3,column=1,sticky=S)

frame0.pack()

canvas0.pack()

mainloop()

#toBraille(list0)