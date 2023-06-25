import uiautomator2
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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


def swipe(start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0):
    actions = ActionChains( )
    actions.w3c_actions = ActionBuilder(mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(duration / 1000)
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


# 登录
driver = android_driver()
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
numbers = [15000000101, 16621142901]
for x in range(len(numbers)):
    # driver.find_element('id', 'cn.missevan:id/nav_icon_mine').click()
    driver.find_element('id', 'cn.missevan:id/textView5').click()
    time.sleep(1)
    driver.find_element('id', 'cn.missevan:id/passwordLogin').click()
    driver.find_element('id', 'cn.missevan:id/etPhoneNum').send_keys(numbers[x])
    driver.find_element('id', 'cn.missevan:id/etPassword').send_keys('123456')
    driver.find_element('id', 'cn.missevan:id/privacy_checked').click()
    driver.find_element('id', 'cn.missevan:id/login').click()
    time.sleep(1)
    driver.find_element('id', 'cn.missevan:id/nav_icon_home').click()
# 开播
#     driver.find_elements('id', 'cn.missevan:id/tv_profile_title')[11].click()
    driver.find_element('id', 'cn.missevan:id/tv_tab_title').click()
    driver.find_element('id', 'cn.missevan:id/img_status').click()

    driver.find_element('id', 'cn.missevan:id/card_live_start').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
    driver.find_element('id', 'cn.missevan:id/tv_start_live').click()
    # driver.find_element('id', 'cn.missevan:id/tv_start_live').click()
    # driver.find_element('id', 'com.lbe.security.miui:id/permission_allow_foreground_only_button').click()  # 允许权限
    time.sleep(2)
    # 关播
    # driver.find_element('id', 'cn.missevan:id/close_icon').click()
    # time.sleep(1)
    # driver.find_element('id', 'cn.missevan:id/confirm').click()
    # driver.find_element('id', 'cn.missevan:id/close').click()
    # time.sleep(1)
    # driver.press_keycode(4)

    # 杀掉 app
    driver.terminate_app('cn.missevan')
    driver.launch_app()
    time.sleep(4)
    driver.find_element('id', 'cn.missevan:id/nav_icon_mine').click()
    driver.find_element('id', 'cn.missevan:id/iv_settings').click()
    time.sleep(1)
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000)
    time.sleep(1)
    driver.find_element('id', 'cn.missevan:id/logout').click()
    time.sleep(1)
    driver.find_element('id', 'cn.missevan:id/tv_sure').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
    # driver.find_element('id', '').click()
