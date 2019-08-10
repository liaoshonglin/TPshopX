"""
语法:
    id:driver.find_element_by_id()
    id定位方式仅限于安卓应用
    UIautomatorViewer工具:resource_id
    appium inspecter工具:resource_id

    name:driver.find_element_by_name()
    andriod不能使用
    ios可以使用name

    class_name:driver.find_element_by_class_name()
"""
# 1.导入appium
from appium import webdriver
import time
import base64

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
# 3.打开手机(app)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)
# 4.元素定位
id_ele=driver.find_elements_by_id('com.android.settings:id/title')
for ele_id in id_ele:
    print('id定位的',ele_id.text)


class_ele=driver.find_elements_by_class_name('android.widget.TextView')
for ele1 in class_ele:
    print('class定位的',ele1.text)
driver.quit()