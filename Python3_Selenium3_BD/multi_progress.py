"""
多进程：
	multiprocessing模块：
	多进程multiprocessing模块的使用与多线程 threading 模块的用法类似。
		Multiprocessing 提供了本地和远程的并发性。

"""


import multiprocessing
from time import sleep, ctime


def super_player(file_, time):
	for i in range(2):
		print("I was listening to %s !%s" % (file_, ctime()))
		sleep(3)


# 播放的文件和时长
lists = {'追光者.mp3': 3, '阿凡达.mp4': 5, '葫芦娃.mp3': 6}

# 创建进程数组
threads = []
files = range(len(lists))
for file_, time in lists.items():
	t = multiprocessing.Process(target=super_player, args=(file_, time))
	threads.append(t)


if __name__ == '__main__':
	# music('葫芦娃', 3)
	# movie("蜡笔小新", 3)
	# print("over  %s" % ctime())
	for t in files:
		# t.start()
		threads[t].start()

	# 守护进程
	for t in files:
		# t.join()
		threads[t].join()
	print("结束! %s" % ctime())

