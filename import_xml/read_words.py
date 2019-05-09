import re
import xml.etree.ElementTree as ET

def import_xml(words):
    #创建根节点
    root = ET.Element("wordbook")
    for w,translation in words.items():
        #创建子节点，并添加属性
        item = ET.SubElement(root,"item")
        word = ET.SubElement(item,'word')
        trans = ET.SubElement(item,'trans')
        phonetic = ET.SubElement(item,'phonetic')
        tags = ET.SubElement(item,'tags')
        progress = ET.SubElement(item,'progress')

        #创建子节点，并添加数据
        word.text = w
        trans.text = translation
        tags.text = 'FRM'
    #创建elementtree对象，写文件
    tree = ET.ElementTree(root)
    tree.write("test.xml",'utf-8')

path ='c:\\words.txt'
words = open(path,'r')

all_words = {}
# lines = words.readline()
# sc = re.compile('[\u4e00-\u9fa5]')
# se = re.compile('[A-Za-z]')
# e = sc.split(lines)[0]
# c= se.split(lines)[-1].replace('\n','')

result = []
lines = words.readlines()
for l in lines:
    line = l.rstrip('\n')
    if  not re.match('^\d+$',line):
       if re.match('^[\u4e00-\u9fa5]',line):
           result[-1] = result[-1]+line
       else:
           result.append(line)
words.close()

for r in result:
    sc = re.compile('[\u4e00-\u9fa5]')
    se = re.compile('[A-Za-z]')
    e = sc.split(r)[0]
    if '（' in e :
        e = e.rstrip('（')
    c = se.split(r)[-1]
    all_words[e] = c



import_xml(all_words)