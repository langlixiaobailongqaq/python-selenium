"""
异常捕获处理
"""


try:
	open("abc.txt", "r")
except FileNotFoundError:
	print("没有找到这样的文件或目录")


# 打印出 出现异常的错误
try:
	print(bb)
except Exception as msg:
	print(msg)
else:
	print("一切正常")


# 无论是否出现错误，继续执行finally的内容
try:
	print(xx)
except Exception as e:
	print(e)
finally:
	print("程序执行完毕!")