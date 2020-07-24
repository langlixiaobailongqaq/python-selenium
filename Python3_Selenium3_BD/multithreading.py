# __author__ =='浪里小白龙'

"""
多线程:
Threading模块：
	Python有thread 和 threading 连个库对线程的支持。
	Python有thread模块不支持守护线程。当主线程退出时，所有的子线程不管是否还在工作,都会被强行退出。
	threading模块支持守护线程
"""
from time import sleep, ctime
import threading


# # 听音乐的任务
# def music(func, loop):
# 	for i in range(loop):
# 		print("I was listening to %s music!%s" % (func, ctime()))
# 		sleep(3)
#
#
# 	# 看电影
# def movie(func, loop):
# 	for i in range(loop):
# 		print("I was listening to %s movie!%s" % (func, ctime()))
# 		sleep(3)


def super_player(file_, time):
	for i in range(2):
		print("I was listening to %s !%s" % (file_, ctime()))
		sleep(3)


# 播放的文件和时长
lists = {'追光者.mp3': 3, '阿凡达.mp4': 5, '葫芦娃.mp3': 6}

# 创建线程数组
threads = []
files = range(len(lists))
for file_, time in lists.items():
	t = threading.Thread(target=super_player, args=(file_, time))
	threads.append(t)



# # 创建线程数组
# threads = []
#
# # 创建线程1
# t1 = threading.Thread(target=music, args=('葫芦娃', 2))
# threads.append(t1)
#
# # 创建线程2
# t2 = threading.Thread(target=movie, args=('蜡笔小新', 2))
# threads.append(t2)

if __name__ == '__main__':
	# music('葫芦娃', 3)
	# movie("蜡笔小新", 3)
	# print("over  %s" % ctime())
	for t in files:
		# t.start()
		threads[t].start()

	# 守护线程
	for t in files:
		# t.join()
		threads[t].join()
	print("结束! %s" % ctime())

