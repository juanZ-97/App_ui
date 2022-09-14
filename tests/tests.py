
from utils.shell import Device
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
import time

udid = Device.get_android_devices() [0]
# host = "http://localhost:4723/wd/hub"
# desired_caps = {'appActivity': '.activity.MainActivity',
#                 'appPackage': 'cn.missevan',
#                 'autoGrantPermissions': True,
#                 'autoLaunch': False,
#                 'automationName': 'UiAutomator2',
#                 'deviceName': udid,
#                 'noReset': True,
#                 'platformName': 'Android',
#                 'platformVersion': '11.0',
#                 'newCommandTimeout': '30000',
#                 'udid': udid}
#
# driver = webdriver.Remote(host, desired_caps)
# driver.implicitly_wait(5)
#
#
# def get_toast(driver, text=None, timeout=5, poll_frequency=0.5):
#     if text:
#         toast_loc = ("//*[contains(@text, '%s')]" % text)
#         print('有text')
#     else:
#         toast_loc = "//*[@class='android.widget.Toast']"
#         print('没有预设定的text')
#     try:
#         WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(('xpath', toast_loc)))
#         print('找到 toast_loc 了', toast_loc)
#         toast_elm = driver.find_element_by_xpath(toast_loc)
#         print('找到 toast_elm 了', toast_elm)
#         return toast_elm
#     except:
#         print('要返回 False 了')
#         return False


# -*- coding:utf-8 -*-
# @author: 给你一页白纸

def android_driver():
    desired_caps = {'appActivity': '.activity.MainActivity',
                    'appPackage': 'cn.missevan',
                    'autoGrantPermissions': True,
                    'autoLaunch': False,
                    'automationName': 'uiautomator2',
                    'deviceName': udid,
                    'noReset': True,
                    'platformName': 'Android',
                    'platformVersion': '11.0',
                    'newCommandTimeout': '30000',
                    'waitForIdleTimeout': 100,
                    'udid': udid}
    # 启动app
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def is_toast_exist(driver, text, timeout=5, poll_frequency=0.5):
    '''
    判断toast是否存在，是则返回True，否则返回False
    '''
    try:
        start = time.perf_counter()
        toast_loc = (By.XPATH, ".//*[contains(@text, %s)]" % text)
        WebDriverWait(driver, timeout, poll_frequency).until(
            ec.presence_of_element_located(toast_loc)
        )
        end = time.perf_counter()
        print("判断 toast 是否存在花费的时间为：", end - start)
        return True
    except:
        return False


def get_toast_text(driver, timeout=5, poll_frequency=0.5):
    '''
    定位toast元素，获取text属性
    '''
    toast_loc = (By.XPATH, '//*[@class="android.widget.Toast"]')
    try:
        start = time.perf_counter()
        toast = WebDriverWait(driver, timeout, poll_frequency).until(
            ec.presence_of_element_located(toast_loc)
        )
        toast_text = toast.get_attribute('text')
        end = time.perf_counter()
        print("通过 xpath 定位到 toast 花费的时间为：", end - start)
        return toast_text
    except Exception as e:
        return e


def login_opera(driver):
    '''登录今日头条操作'''
    try:
        # driver.find_element_by_id("com.ss.android.article.news:id/cji").click()  # 点击【同意】
        start = time.perf_counter()
        driver.find_element(By.ID, 'cn.missevan:id/feed').click() # 点击登录
        end = time.perf_counter()
        print("通过 id 定位到点击投食按钮花费的时间为：", end - start)
    except Exception as e:
        print("投食失败，原因为：{}".format(e))
    else:
        toast_text = get_toast_text(driver)
        print('toast_text 是：', toast_text)
        toast_el = is_toast_exist(driver, "投食成功")
        print(toast_el)


if __name__ == '__main__':
    driver = android_driver()
    login_opera(driver)


