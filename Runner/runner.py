# -*- coding: utf-8 -*-

__author__ = 'vBoardTester'
import sys

sys.path.append("..")
import platform #该模块用来访问平台相关属性
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.LoginTest import LoginTest
from TestCase.JoinMeetingTest import JoinMeetingTest

from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init, mk_file
from Base.BaseStatistics import countDate, writeExcel, countSumDevices
from Base.BasePickle import *
from datetime import datetime
from Base.BaseApk import ApkInfo
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")

#创建进程池
def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        #调取Base.Apk.py文件中的ApkInfo类，传入测试app
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _initApp["waitappActivity"]='com.smartcity.maxnerva.vborad_phone.view.activity.*'
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    #运行runnerCaseApp方法
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    print(devices)
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest, param=devices))
    suite.addTest(ParametrizedTestCase.parametrize(JoinMeetingTest, param=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")

if __name__ == '__main__':

    kill_adb()

    #通过BaseAdb文件的AndroidDebugBridge().attached_devices()获得所有设备信息
    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        #创建文件，参看BaseInit.py文件和BaseFile.py文件
        mk_file()
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            #向设备中安装uiautomator2这两个应用，具体参看BaseInit.py
            init(dev)
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            #为devices字典中添加app
            app["app"]=PATH("../app/VBoard_V1.2.0.5_qa.apk")

            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的安卓设备")
