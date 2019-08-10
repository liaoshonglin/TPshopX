"""
语法:
    driver.swipe(起始x,起始y,终止x,duration=滑动操作的持续时间 单位ms)
    driver.get_windows_size 获取手机宽高--手机屏幕

总结:
    1.swipe滑动操作对项目标
    2.如果duration参数不填,滑动的时候有一定的惯性
    3.当duration的值越大,滑动的距离越接近起始坐标和终止坐标的差
"""
from appium import webdriver
import time


# 2.配置启动参数(键值对---字典)
desired_caps = {}
# 2.1 指定系统名称
desired_caps["platformName"] = "Android"
# 2.2 指定系统版本
desired_caps["platformVersion"] = "5.1.1"
# 2.3 指定设备名称
# 设备名称在运行ios系统的时候必须按照正确的设备名称填写,对于Android来说只要不为空即可
desired_caps["deviceName"] = "127.0.0.1:21503"
# 2.4 指定app包名
desired_caps["appPackage"] = "com.android.settings"
# 2.5 指定APP启动名
desired_caps["appActivity"] = ".Settings"
desired_caps['unicodeKeyboard']=True
desired_caps['reseKeyboard']=True
# 3.打开手机(app)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)
print(driver.get_window_size())

driver.swipe(250,800,250,200)
time.sleep(2)
driver.quit()