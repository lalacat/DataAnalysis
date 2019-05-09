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


# import_xml(words)