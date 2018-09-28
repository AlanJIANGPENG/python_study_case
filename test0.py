#coding=utf-8 

from appium import webdriver
import time

desired_caps = {
	'platformName':'Android',
	'deviceName':'c578308',      # 小米4测试机
	# 'diveceName':'D6FMMBOZSSAAPBTC',      # Honor 3C
	# 'deviceName':'emulator-5554',    # 启动AVD太慢了得15分钟才能起来，不用这
	'platformVersion':'6.0',
	# 'platformVersion':'4.2.2',

	# cmd指令:aapt dump badging D:\test\xxx.apk获取以下两行信息
	# 启动顺逛APP
	# 'appPackage':'com.ehaier.shunguang',
	# 'appActivity':'com.ehaier.shunguang.MainActivity'     # 下拉至中间查找

	# 获取当前运行appPackage和appActivity：
	# adb shell dumpsys window | findstr mCurrentFocus
	# 命令行后加上 >>  E:\test010.txt  生成文件输出
	# 启动计算器
	'appPackage':'com.miui.calculator',
	'appActivity':'com.miui.calculator.cal.CalculatorActivity'
	# 启动微信
	# 'appPackage':'com.tencent.mm',
	# 'appActivity':'com.tencent.mm.ui.LauncherUI'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(6)


driver.find_element_by_name("1").click()
time.sleep(2)
driver.find_element_by_name("5").click()
time.sleep(2)
driver.find_element_by_name("9").click()
time.sleep(2)
driver.find_element_by_id("com.miui.calculator:id/btn_del_s").click()
time.sleep(2)
driver.find_element_by_name("9").click()
time.sleep(2)
driver.find_element_by_name("5").click()
time.sleep(2)
driver.find_element_by_id("com.miui.calculator:id/btn_plus_s").click()
time.sleep(2)
driver.find_element_by_name("6").click()
time.sleep(2)
driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()
time.sleep(2)
driver.quit()
time.sleep(2)