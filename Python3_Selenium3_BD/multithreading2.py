"""
多线程:
Threading模块：
	Python有thread 和 threading 连个库对线程的支持。
	Python有thread模块不支持守护线程。当主线程退出时，所有的子线程不管是否还在工作,都会被强行退出。
	threading模块支持守护线程
"""

import threading
from time import sleep, ctime


# 创建线程类
class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def run(self):
		self.func(*self.args)


def super_player(file_, time):
	for i in range(2):
		print("Start Playing %s! %s" % (file_, time))
		sleep(time)


# 播放的文件和播放时长
lists = {'追光者.mp3': 3, '阿凡达.mp4': 5, '葫芦娃.mp3': 6}

# 创建线程数组
threads = []
files = range(len(lists))
for file_, time in lists.items():
	t = MyThread(super_player, (file_, time), super_player.__name__)
	threads.append(t)


if __name__ == '__main__':
	for t in files:
		threads[t].start()
	# 守护线程
	for t in files:
		threads[t].join()
	print("结束! %s" % ctime())


