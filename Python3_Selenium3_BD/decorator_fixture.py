"""
@装饰器的使用以及fixture的使用

运行测试时，有时需要直接跳过某些测试用例，或者当用例符合某个条件时跳过测试，又或者直接将测试用例
	置为失败.Unittest提供了实现这些需求的装饰器。

unittest.skip(reason)               无条件跳过测试用例，并说明原因
unittest.skipif(reason)             满足条件跳过测试用例
unittest.skipUnless(reason)         条件为真则不跳过测试用例
unittest.expectedFailure(reason)     将测试用例标记为失败

fixture: 可以形象的把它比作夹心比干外层的两片饼干，这两块饼干就是 setup和 teardown，中间的心就是测试用例。
	除此之外, unittest还提供了更大范围的 fixtures,如测试类和模块的 fixtures

"""

import unittest

class MyTest(unittest.TestCase):
	"""装饰器"""
	def setUp(self):
		print("测试开始")

	def tearDown(self):
		print("测试结束")

	@unittest.skip("直接跳过")
	def test01_skip_101(self):
		print("test aaa")

	@unittest.skipIf(3 > 1, "当条件3>1为真的时候,跳过该测试")
	def test02_skip_if_102(self):
		print("test bbb")

	@unittest.skipUnless(3 > 2, "当条件为真的时候执行")
	def test03_skip_Unless_103(self):
		print("test ccc")

	@unittest.expectedFailure
	def test04_expected_Failure_104(self):
		print("不管结果怎么样，总是置为失败")



def setUpModule():
	print("测试模块开始")


def tearDownModule():
	print("模块测试结束")


class Test(unittest.TestCase):
	"""fixture 使用"""
	@classmethod
	def setUpClass(cls):
		print("类测试开始")

	@classmethod
	def tearDownClass(cls):
		print("类测试结束")

	def setUp(self):
		print("用例测试开始")

	def tearDown(self):
		print("用例测试结束")

	def test_01_case_101(self):
		print("测试用例1")

	def test_02_case_102(self):
		print("测试用例2")



