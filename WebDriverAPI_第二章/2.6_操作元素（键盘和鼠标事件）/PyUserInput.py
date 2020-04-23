# conding:utf-8
from pymouse import PyMouse # 模拟鼠标操作
from pykeyboard import PyKeyboard # 模拟键盘操作

m = PyMouse()
k = PyKeyboard()

_dim, y_dim = m.screen_size() #–获得屏幕尺寸
k.type_string("Hello, World!") #–模拟键盘输入字符串