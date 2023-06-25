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
def android_driver():
    desired_caps = {'appActivity': '.activity.MainActivity',
                    'appPackage': 'cn.missevan',
                    'autoGrantPermissions': True,
                    'autoLaunch': False,
                    'automationName': 'uiautomator2',
                    'deviceName': 'ziyi',
                    'noReset': True,
                    'platformName': 'Android',
                    'platformVersion': '12',
                    'newCommandTimeout': '30000',
                    'waitForIdleTimeout': 100,
                    }
    # 启动app
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


for x in range(80):
    driver = android_driver()
    num = 920 + x
    driver.find_element('id','cn.missevan:id/iv_create').click()
    driver.find_element('id', 'cn.missevan:id/edt_name').send_keys(num)
    driver.find_element('id', 'cn.missevan:id/tvSure').click()
