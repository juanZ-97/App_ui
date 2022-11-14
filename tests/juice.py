import uiautomator2
import sys
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
import time

# print(uiautomator2.connect_adb_wifi('10.21.250.203:5090').info)

def android_driver():
    desired_caps = {'appActivity': '.activity.MainActivity',
                    'appPackage': 'cn.missevan',
                    'autoGrantPermissions': True,
                    'autoLaunch': False,
                    'automationName': 'uiautomator2',
                    'deviceName': 'xiaomi 10',
                    'noReset': True,
                    'platformName': 'Android',
                    'platformVersion': '11.0',
                    'newCommandTimeout': '30000',
                    'waitForIdleTimeout': 100,
                    }
    # 启动app
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def is_toast_exist(driver, text=None, timeout=5, poll_frequency=0.5):

    toast_loc = (By.XPATH, '//*[@class="android.widget.Toast"]')
    toast = WebDriverWait(driver, timeout, poll_frequency).until(
        ec.presence_of_element_located(toast_loc)
    )
    toast_text = toast.get_attribute('text')
    if text in toast_text:
        return True
    else:
        return False


driver = android_driver()
driver.find_element(By.ID, 'cn.missevan:id/feed').click() # 点击登录
print(is_toast_exist(driver, '投食成功'))