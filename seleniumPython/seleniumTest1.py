from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#启动浏览器
driver = webdriver.Chrome()

# first_url = 'https://www.baidu.com'
# print('now access %s'%(first_url))
# driver.get(first_url)
# #
# second_url = 'http://news.baidu.com'
# print('now access %s'%(second_url))
# driver.get(second_url)
#
# print('back to %s'%(first_url))
# driver.back()
#
# print('foward to %s'%(second_url))
# driver.forward()

# driver.refresh()

# print("设置浏览器宽480，高880显示")
# # driver.set_window_size(480,800)
# driver.maximize_window()


driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys("selenium")
# driver.find_element_by_id('su').click()
# driver.quit()
# driver.find_element_by_id('kw').send_keys('selenium').submit()
# size = driver.find_element_by_id('kw').size
# print(size)

# text = driver.find_element_by_id('cp').text
# type = driver.find_element_by_id('kw').get_attribute('type')
# driver.quit()
# print(type)
# display = driver.find_element_by_id('kw').is_displayed()
# driver.quit()
# print(display)
#
# above = driver.find_element_by_link_text('设置')
# ActionChains(driver).click(above).perform
driver.find_element_by_id('kw').send_keys('seleniumm')
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)