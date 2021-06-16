# pip install opencv-python
# pip install numpy
# pip install selenium

""" python实现掘金站点 https://juejin.im/
    滑动验证码自动验证功能
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from urllib import request
import cv2
import numpy as np


# 这个函数是用来显示图片的。
def show(name):
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 这里我用的google的驱动。
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = 'https://juejin.im/'


# 实现登录
def get_login(driver, url):
    driver.get(url)
    driver.find_element_by_xpath('//button[@class="login-button"]').click()
    driver.find_element_by_xpath('//span[@class ="clickable"]').click()
    driver.find_element_by_xpath('//input[@name="loginPhoneOrEmail"]').send_keys('1')
    driver.find_element_by_xpath('//input[@name="loginPassword"]').send_keys('填入自己的密码')
    driver.find_element_by_xpath('//button[@class="btn"]').click()
    sleep(2)
    return driver


driver = get_login(driver, url)

# 块图片
blockJpg = './block.jpg'
# 模板图片
templateJpg = './template.jpg'


# 获取验证码中的图片
def get_image(driver):
    # 获取背景图url
    bj = driver.find_element_by_xpath('//img[@class="sc-gqjmRU cHbGdz sc-ifAKCX itlNmx"]').get_attribute('src')
    # 获取移动块url
    yd = driver.find_element_by_xpath(
        '//img[@class="captcha_verify_img_slide react-draggable sc-VigVT ggNWOG"]').get_attribute('src')
    req = request.Request(bj)
    bg = open(templateJpg, 'wb+')
    bg.write(request.urlopen(req).read())
    bg.close()
    req = request.Request(yd)
    bk = open(blockJpg, 'wb+')
    bk.write(request.urlopen(req).read())
    bk.close()
    return templateJpg, blockJpg


bkg, blk = get_image(driver)


# 计算缺口的位置，由于缺口位置查找偶尔会出现找不准的现象，这里进行判断，如果查找的缺口位置x坐标小于100，
# 我们进行刷新验证码操作，重新计算缺口位置，知道满足条件位置。
def get_distance(bkg, blk):
    # 读取灰度图
    block = cv2.imread(blk, 0)
    tp = cv2.imread(bkg, 0)
    # 保存图像
    cv2.imwrite(templateJpg, tp)
    cv2.imwrite(blockJpg, block)

    block = cv2.imread(blockJpg)
    block = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
    block = abs(255 - block)
    cv2.imwrite(blockJpg, block)
    block = cv2.imread(blockJpg)
    tp = cv2.imread(templateJpg)
    ''' 
    模板匹配函数 cv2.matchTemplate(image, temp, method, result=None, mask=None)
    image：待搜索图像;temp：模板图像;result：匹配结果;method：计算匹配程度的方法
    '''
    result = cv2.matchTemplate(block, tp, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    # x, y, w, h = cv2.boundingRect(GrayImage)
    # 这里就是下图中的绿色框框  50*50是移动块的大小
    cv2.rectangle(tp, (y, x), (y + 52, x + 52), (7, 249, 151), 2)
    print('x坐标为：%d' % x)
    print('y坐标为：%d' % y)
    if y < 80:
        # 刷新按钮
        elem = driver.find_element_by_xpath(
            '//a[@class="secsdk_captcha_refresh refresh-button___StyledA-sc-18f114n-0 jgMJRc"]')
        sleep(1)
        elem.click()
        bkg, blk = get_image(driver)
        y, tp = get_distance(bkg, blk)
    return y, tp


distance, temp = get_distance(bkg, blk)


# 这个是用来模拟人为拖动滑块行为，快到缺口位置时，减缓拖动的速度，服务器就是根据这个来判断是否是人为登录的。
def get_tracks(dis):
    v = 0
    m = 0.3
    # 保存0.3内的位移
    tracks = []
    current = 0
    mid = distance * 4 / 5
    while current <= dis:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0 * m + 0.5 * a * (m ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * m
    return tracks


# 原图的像素是552*344，而网页的是340*212，图像缩小了。  340/552=0.6159420289855072
# double_distance = int(distance * 1.231884058)
double_distance = int(distance * 0.6159420289855072)
tracks = get_tracks(double_distance)
# 由于计算机计算的误差，导致模拟人类行为时，会出现分布移动总和大于真实距离，这里就把这个差添加到tracks中，也就是最后进行一步左移。
tracks.append(-(sum(tracks) - double_distance))

element = driver.find_element_by_xpath('//div[@class="secsdk-captcha-drag-icon sc-jKJlTe fsBatO"]')
ActionChains(driver).click_and_hold(on_element=element).perform()
for track in tracks:
    ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
sleep(0.5)
ActionChains(driver).release(on_element=element).perform()
# show(temp)