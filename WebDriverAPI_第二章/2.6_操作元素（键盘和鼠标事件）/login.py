# coding:utf-8
import csv
'''
enumerate()是python的内置函数
 enumerate在字典上是枚举、列举的意思
 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
 enumerate多用于在for循环中得到计数。
'''

# #  如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
# list = ["这", "是", "一个", "测试","数据"]
# for i in range(len(list)):
#     print(i,list[i])
#
# # 上述方法有些累赘，利用enumerate()会更加直接和优美：
# list1 = ["这", "是", "一个", "测试","数据"]
# for index, item in enumerate(list1):
#     print(index,item)


def get_csv_data(csv_file, line):
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            if index == line:
                return row
'''
以下是 enumerate() 方法的语法:
enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。
'''

csv_file = 'D:/Pycharm/Pycharm/python-selenium/login.csv'
data = get_csv_data(csv_file, 1)   # 第一行
# print(data[0])                   # 第一列