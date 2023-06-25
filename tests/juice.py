import uiautomator2
import sys
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
import time

# print(uiautomator2.connect_adb_wifi('10.21.250.203:5090').info)

# 连接安卓
# def android_driver():
#     desired_caps = {'appActivity': '.activity.MainActivity',
#                     'appPackage': 'cn.missevan',
#                     'autoGrantPermissions': True,
#                     'autoLaunch': False,
#                     'automationName': 'uiautomator2',
#                     'deviceName': 'xiaomi 10',
#                     'noReset': True,
#                     'platformName': 'Android',
#                     'platformVersion': '11.0',
#                     'newCommandTimeout': '30000',
#                     'waitForIdleTimeout': 100,
#                     }
#     # 启动app
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     return driver

#
# def is_toast_exist(driver, text=None, timeout=5, poll_frequency=0.5):
#
#     toast_loc = (By.XPATH, '//*[@class="android.widget.Toast"]')
#     toast = WebDriverWait(driver, timeout, poll_frequency).until(
#         ec.presence_of_element_located(toast_loc)
#     )
#     toast_text = toast.get_attribute('text')
#     if text in toast_text:
#         return True
#     else:
#         return False
#
#
# driver = android_driver()
# driver.open_notifications()
# time.sleep(2)
# driver.press_keycode(4)


# driver.find_element(By.ID, 'cn.missevan:id/feed').click() # 点击登录
# print(is_toast_exist(driver, '投食成功'))

# 连接 iOS
def android_driver():
    # 12
    # desired_caps = {'bundleId': 'com.missevan.CatEarFM',
    #                 'udid': '00008101-0011481014DA001E',
    #                 'autoGrantPermissions': True,
    #                 'autoLaunch': True,
    #                 'automationName': 'XCUITest',
    #                 'deviceName': 'iPhone 12',
    #                 'noReset': True,
    #                 'platformName': 'iOS',
    #                 'platformVersion': '16.0.3',
    #                 'newCommandTimeout': '30000',
    #                 'waitForIdleTimeout': 100,
    #                 }
    # 6P
    desired_caps = {'bundleId': 'com.missevan.CatEarFM',
                    'udid': 'd32f7fcfd7e4a45cc1d6fb571c115d3f17d03626',
                    'autoGrantPermissions': True,
                    'autoLaunch': True,
                    'automationName': 'XCUITest',
                    'deviceName': 'iPhone 6 Plus',
                    'noReset': True,
                    'platformName': 'iOS',
                    'platformVersion': '12.5.3',
                    'newCommandTimeout': '30000',
                    'waitForIdleTimeout': 100,
                    }
    # 启动app
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


for x in range(1000):
    driver = android_driver()
    time.sleep(5)
    driver.terminate_app('com.missevan.CatEarFM')
