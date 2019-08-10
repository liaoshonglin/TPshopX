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
bluetooth=driver.find_element_by_xpath('//*[@text="蓝牙"]')
search=driver.find_element_by_accessibility_id('搜索')
# 4.获取蓝牙的id
print('蓝牙的id',bluetooth.get_attribute('resourceId'))
#获取蓝牙的class
print('蓝牙的class',bluetooth.get_attribute('className'))
#获取蓝牙的text
print('蓝牙的text',bluetooth.get_attribute('text'))
#获取搜索按钮的content-desc
print('搜索按钮的content-desc',search.get_attribute('name'))
#关闭驱动
driver.quit()