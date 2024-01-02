# -*- coding: utf-8 -*-

from appium import webdriver
from base.action import ElementActions
from utils import shell
from utils.shell import Device


class Singleton(object):
    """单例模式
    """
    Action = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            udid = Device.get_android_devices()[0]
            host = "http://localhost:4722/wd/hub"
            desired_caps = {'appActivity': '.activity.MainActivity',
                            'appPackage': 'cn.missevan',
                            'autoGrantPermissions': True,
                            'autoLaunch': False,
                            # 'autoLaunch': True,
                            'automationName': 'UiAutomator2',
                            'deviceName': udid,
                            'noReset': True,
                            'fullReset': False,
                            'platformName': 'Android',
                            'platformVersion': '10',
                            'newCommandTimeout': 30000,
                            'waitForIdleTimeout': 100,
                            'udid': udid}

            driver = webdriver.Remote(host, desired_caps)
            ADB = shell.ADB(udid)
            desired_caps['platformVersion'] = ADB.get_android_version()
            Action = ElementActions(driver, ADB, Parameterdict=desired_caps)
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.Action = Action
        return cls._instance


class DriverClient(Singleton):
    pass
