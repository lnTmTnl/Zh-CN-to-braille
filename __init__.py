# -*- coding:utf-8 -*-
import os
from pypinyin import lazy_pinyin,Style
from tkinter import *
import jieba
style=Style.TONE3

#节点
class node:
    pinYin = None
    blind = None
    sibling = None
    child = None
    def __init__(self, p, b):
        self.pinYin = p
        self.blind = b

#声母树
class blindTree1:
    __root=None
    def __init__(self):
        self.__root=node('b','⠃')
        p = self.__root
        p.sibling = node('p', '⠏')
        p=p.sibling
        p.sibling=node('m','⠍')
        p=p.sibling
        p.sibling=node('f','⠋')
        p=p.sibling
        p.sibling=node('d','⠙')
        p=p.sibling
        p.sibling=node('t','⠞')
        p=p.sibling
        p.sibling=node('n','⠝')
        p=p.sibling
        p.sibling=node('l','⠇')
        p=p.sibling
        p.sibling=node('g','⠛')
        p=p.sibling
        p.sibling=node('j','⠛')
        p=p.sibling
        p.child=node('u','⠛⠬')
        q=p.child
        q.child=node('a','⠛⠯')
        q.child.child=node('n','⠛⠯')
        q.child.sibling=node('e','⠛⠾')
        q.child.sibling.sibling=node('n','⠛⠸')
        p.sibling=node('k','⠅')
        p=p.sibling
        p.sibling=node('q','⠅')
        p=p.sibling
        p.child = node('u', '⠅⠬')
        q = p.child
        q.child = node('a', '⠅⠯')
        q.child.child = node('n', '⠅⠯')
        q.child.sibling = node('e', '⠅⠾')
        q.child.sibling.sibling = node('n', '⠅⠸')
        p.sibling=node('h','⠓')
        p=p.sibling
        p.sibling=node('x','⠓')
        p=p.sibling
        p.child = node('u', '⠓⠬')
        q = p.child
        q.child = node('a', '⠓⠯')
        q.child.child = node('n', '⠓⠯')
        q.child.sibling = node('e', '⠓⠾')
        q.child.sibling.sibling = node('n', '⠓⠸')

        p.sibling=node('r','⠚')
        p=p.sibling
        p.child=node('i','⠚')

        p.sibling=node('z','⠵')
        p=p.sibling
        p.child=node('i','⠵')
        q=p.child
        q.sibling=node('h','⠌')
        q=q.sibling
        q.child=node('i','⠌')

        p.sibling = node('c','⠉')
        p = p.sibling
        p.child = node('i','⠉')
        q = p.child
        q.sibling = node('h','⠟')
        q = q.sibling
        q.child = node('i','⠟')

        p.sibling = node('s','⠎')
        p = p.sibling
        p.child = node('i','⠎')
        q = p.child
        q.sibling = node('h','⠱')
        q = q.sibling
        q.child = node('i','⠱')

        p.sibling=node('y','⠊')
        p=p.sibling
        p.child=node('a','⠫')
        q=p.child
        q.sibling=node('o','⠊⠢')
        q.child=node('o','⠜')
        q.child.sibling=node('n','⠩')
        q.child.sibling.child=node('g','⠭')
        q=q.sibling
        q.sibling=node('e','⠑')
        q.child=node('n','⠹')
        q.child.child=node('g','⠹')
        q=q.sibling
        q.sibling=node('i','⠊')
        q=q.sibling
        q.child=node('n','⠣')
        q.child.child=node('g','⠡')
        q.sibling=node('u','⠬')
        q=q.sibling
        q.child=node('a','⠯')
        q.child.child=node('n','⠯')
        q.child.sibling=node('e','⠾')
        q.child.sibling.sibling=node('n','⠸')

        p.sibling = node('w','⠥')
        p = p.sibling
        p.child = node('a', '⠿')
        q = p.child
        q.sibling = node('o','⠕')
        q.child = node('i','⠽')
        q.child.sibling = node('n','⠻')
        q.child.sibling.child = node('g','⠶')
        q = q.sibling
        q.sibling = node('e', '⠥⠢')
        q=q.sibling
        q.child = node('i','⠺')
        q.child.sibling = node('n','⠒')
        q.child.sibling.child = node('g', '⠲')
        q.sibling=node('u','⠥')

    def getRoot(self):
        return self.__root

#韵母树
class blindTree2:
    __root = None
    def __init__(self):
        self.__root = node('a','⠔')
        p = self.__root
        p.child=node('i','⠪')
        q=p.child
        q.sibling=node('o','⠖')
        q=q.sibling
        q.sibling=node('n','⠧')
        q=q.sibling
        q.child=node('g','⠦')

        p.sibling=node('e','⠢')
        p=p.sibling
        p.child=node('i','⠮')
        q=p.child
        q.sibling=node('n','⠴')
        q=q.sibling
        q.child=node('g','⠼')

        p.sibling=node('o','⠢')
        p=p.sibling
        p.child=node('u','⠷')
        q=p.child
        q.sibling=node('n','⠼')
        q=q.sibling
        q.child=node('g','⠼')

        p.sibling=node('i','⠊')
        p=p.sibling
        p.child=node('a','⠫')
        q=p.child
        q.child=node('o','⠜')
        q.child.sibling=node('n','⠩')
        q.child.sibling.child=node('g','⠭')
        q.sibling=node('o','⠹')
        q=q.sibling
        q.child=node('n','⠹')
        q.child.child=node('g','⠹')
        q.sibling=node('e','⠑')
        q=q.sibling
        q.sibling=node('u','⠳')
        q=q.sibling
        q.sibling=node('n','⠣')
        q=q.sibling
        q.child=node('g','⠡')

        p.sibling=node('u','⠥')
        p=p.sibling
        p.child=node('a','⠿')
        q=p.child
        q.child=node('i','⠽')
        q.child.sibling=node('n','⠻')
        q.child.sibling.child=node('g','⠶')
        q.sibling=node('o','⠕')
        q=q.sibling
        q.sibling=node('e','⠾')
        q=q.sibling
        q.sibling=node('i','⠺')
        q=q.sibling
        q.sibling=node('n','⠒')

        p.sibling=node('v','⠬')

    def getRoot(self):
        return self.__root

#声调列表
phonetic_symbols=['','⠁','⠂','⠄','⠆']

#词典：用于对字母、数字、标点符号等非汉字的转换
dictionary={"。": '⠐⠆', "，": '⠐', "、": '⠈', "；": '⠰', "？": '⠐⠄', "！": '⠰⠂', "：": '⠤',
            "“": '⠘', "”": '⠘', "‘": '⠘⠘', "’": '⠘⠘', "（": '⠰⠄', "）": '⠠⠆', "【": '⠰⠆',
            "】": '⠰⠆', "——": '⠠⠤', "……": '⠐⠐⠐', "—": '⠤', "《": '⠐⠤', "》": '⠤⠂', "〈": '⠐⠄',
            "〉": '⠠⠂', "·": '⠠⠄', " ": ' ', "\n":'\n',

            ".": '⠲', ",": '⠂', "!": '⠖', "?": '⠦', ";": '⠆', ":": '⠒', "-": '⠤', "'": '⠄',
            "(": '⠶', ")": '⠶', "/": '⠌', "…": '⠄⠄⠄', "_": '⠤⠤⠤', "[": '⠠⠶', "]": '⠶⠄',

            "1": '⠁', "2": '⠃', "3": '⠉', "4": '⠙', "5": '⠑', "6": '⠋', "7": '⠛', "8": '⠓',
            "9": '⠊', "0": '⠚',

            "A": '⠁', "B": '⠃', "C": '⠉', "D": '⠙', "E": '⠑', "F": '⠋', "G": '⠛', "H": '⠓',
            "I": '⠊', "J": '⠚', "K": '⠅', "L": '⠇', "M": '⠍', "N": '⠝', "O": '⠕', "P": '⠏',
            "Q": '⠟', "R": '⠗', "S": '⠎', "T": '⠞', "U": '⠥', "V": '⠧', "W": '⠺', "X": '⠭',
            "Y": '⠽', "Z": '⠵',

            "a": '⠁', "b": '⠃', "c": '⠉', "d": '⠙', "e": '⠑', "f": '⠋', "g": '⠛', "h": '⠓',
            "i": '⠊', "j": '⠚', "k": '⠅', "l": '⠇', "m": '⠍', "n": '⠝', "o": '⠕', "p": '⠏',
            "q": '⠟', "r": '⠗', "s": '⠎', "t": '⠞', "u": '⠥', "v": '⠧', "w": '⠺', "x": '⠭',
            "y": '⠽', "z": '⠵'
            }

dictionaryB={"⠁": '100000', "⠂": '010000', "⠃": '110000', "⠄": '001000', "⠅": '101000', "⠆": '011000',
             "⠇": '111000', "⠈": '000100', "⠉": '100100', "⠊": '010100', "⠋": '110100', "⠌": '001100',
             "⠍": '101100', "⠎": '011100', "⠏": '111100', "⠐": '000010', "⠑": '100010', "⠒": '010010',
             "⠓": '110010', "⠔": '001010', "⠕": '101010', "⠖": '011010', "⠗": '111010', "⠘": '000110',
             "⠙": '100110', "⠚": '010110', "⠛": '110110', "⠜": '001110', "⠝": '101110', "⠞": '011110',
             "⠟": '111110', "⠠": '000001', "⠡": '100001', "⠢": '010001', "⠣": '110001', "⠤": '001001',
             "⠥": '101001', "⠦": '011001', "⠧": '111001', "⠨": '000101', "⠩": '100101', "⠪": '010101',
             "⠫": '110101', "⠬": '001101', "⠭": '101101', "⠮": '011101', "⠯": '111101', "⠰": '000011',
             "⠱": '100011', "⠲": '010011', '⠳': '110011', "⠴": '001011', "⠵": '101011', "⠶": '011011',
             "⠷": '111011', "⠸": '000111', "⠹": '100111', "⠺": '010111', "⠻": '110111', "⠼": '001111',
             "⠽": '101111', "⠾": '011111', "⠿": '111111', " ": ' '}

parts=('无', '普通名词', '人名', '地名', '机构名', '作品名', '处所名词', '方位名词', '时间', '其他专名',
       '形容词', '数量词', '量词', '连词', '普通动词', '名动词', '动副词', '副词', '副形词', '名形词',
       '代词', '介词', '助词', '其他虚词', '标点符号')

partsDictionary={"无": '', "普通名词": 'n', "人名": 'nr', "地名": 'ns', "机构名": 'nt', "作品名": 'nw', "处所名词": 's',
                 "方位名词": 'f', "时间": 't', "其他专名": 'nz', "形容词": 'a', "数量词": 'm', "量词": 'q',
                 "连词": 'c', "普通动词": 'v', "名动词": 'vn', "动副词": 'vd', "副词": 'd', "副形词": 'ad',
                 "名形词": 'an', "代词": 'r', "介词": 'p', "助词": 'u', "其他虚词": 'xc', "标点符号": 'w'}

bpm=blindTree1()
p1=bpm.getRoot()
aoe=blindTree2()
p2=aoe.getRoot()

#分词函数
def cutWords(str):
    _str= jieba.cut(str, cut_all=False)
    newstr = "  ".join(_str)
    return newstr

#转换函数
def toBraille(list1,text):

    capitalflag = True
    digitalflag = True

    text.delete("0.0", END)

    for i in range(len(list1)):
        res = dictionary.get(list1[i])
        if (res != None):
            if ('A' <= list1[i] <= 'Z' and capitalflag == True):
                res = '  ⠠' + res
                capitalflag = False
            elif ('0' <= list1[i] <= '9' and digitalflag == True):
                res = '  ⠼' + res
                digitalflag = False
            if (capitalflag == False and ('A' > list1[i] or list1[i] > 'Z') and list1[i] != ' '):
                capitalflag = True
            if (digitalflag == False and ('0' > list1[i] or list1[i] > '9') and list1[i] != ' '):
                digitalflag = True
            list1[i] = res
        else:
            capitalflag = True
            digitalflag = True

    for i in list1:
        if ('⠁' <= i <= '⠿' or '  ⠼⠁' <= i <='  ⠼⠁⠛'  or '  ⠠⠁' <= i <='  ⠠⠽'):
            text.insert(END,i)
            continue
        res = dictionary.get(i)
        if (res != None):
            text.insert(END, res)
        if ('a' < i[len(i) - 1] < 'z'):
            i += '0'
        j = 0
        p1 = bpm.getRoot()
        p2 = aoe.getRoot()
        p = p1
        while (len(i) - 1 > j and p1.sibling != None and (i[j] != p1.pinYin or i[j] == 'b')):
            if (i[j] != 'b'):
                p1 = p1.sibling
            if (p1.pinYin == i[j]):
                j += 1
                p = p1
                if (p1.child != None):
                    p1 = p1.child
                else:
                    break
                while (len(i) - 1 > j and p1.pinYin == i[j]):
                    j += 1
                    p = p1
                    if (p1.child != None):
                        p1 = p1.child
                if (i[j] == p1.pinYin):
                    j += 1
                    p = p1
        if (j != 0):
            text.insert(END, p.blind)
            flag = p.blind
        while (len(i) - 1 > j and p2.sibling != None and (i[j] != p2.pinYin or i[j] == 'a')):
            if (i[j] != 'a'):
                p2 = p2.sibling
            if (p2.pinYin == i[j]):
                j += 1
                p = p2
                if (p2.child != None):
                    p2 = p2.child
                else:
                    break
                while (len(i) - 1 > j and p2.pinYin == i[j]):
                    j += 1
                    p = p2
                    if (p2.child != None):
                        p2 = p2.child
                if (i[j] == p2.pinYin):
                    j += 1
                    p = p2
        if (j != 0 and flag != p.blind):
            text.insert(END, p.blind + phonetic_symbols[int(i[len(i) - 1])] + "")
        elif (j != 0 and flag == p.blind):
            text.insert(END, phonetic_symbols[int(i[len(i) - 1])] + "")

def toBrailleB(text1, text2):
    text2.delete("0.0", END)
    for i in text1.get("0.0",END):
        if(dictionaryB.get(i)!=None):
            text2.insert(END, dictionaryB.get(i))
        else:
            text2.insert(END, i)

userDictionary=[] #用于存储自定义词典的内存空间

if not os.path.isfile("userDict.txt"):  # 无文件时创建
    userDictFile = open("userDict.txt", mode="w", encoding="utf-8")
    userDictFile.close()
else:
    jieba.load_userdict("userDict.txt")
    userDictFile=open("userDict.txt", encoding='utf-8')
    while True:
        line=userDictFile.readline()
        if not line:
            break
        else:
            lineList = line.split()
            if len(lineList) == 1:
                lineList.append('')
            userDictionary.append(lineList)
    userDictFile.close()