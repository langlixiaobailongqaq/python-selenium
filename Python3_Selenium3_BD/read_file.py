"""
read        读取整个文件
readline    读取一行数据
readlines   读取所有行数据
"""
import csv   # 导入csv包
from xml.dom.minidom import parse
import xml.dom.minidom


# 读取txt
user_file = open('username_psw.txt', 'r')
lines = user_file.readlines()
print(lines)
user_file.close()

for line in lines:
	username = line.split(',')[0]
	password = line.split(',')[1]
	print(username, password)


# 读取csv
with open("music.csv", "r", encoding="utf-8") as csvfile:
	# 读取csv文件，返回的是迭代类型
	read = csv.reader(csvfile)
	for i in read:
		print(i)


# 读取xml文件,使用 minidom 解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("info.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
	print("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
	print("*****Movie*****")
	if movie.hasAttribute("title"):
		print("Title: %s" % movie.getAttribute("title"))

type = movie.getElementsByTagName('type')[0]
print("Type: %s" % type.childNodes[0].data)
format = movie.getElementsByTagName('format')[0]
print("Format: %s" % format.childNodes[0].data)
rating = movie.getElementsByTagName('rating')[0]
print("Rating: %s" % rating.childNodes[0].data)
description = movie.getElementsByTagName('description')[0]
print("Description: %s" % description.childNodes[0].data)