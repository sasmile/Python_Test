# coding = utf-8
import time
from selenium import webdriver
import unittest

class baidu_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
    def test_baidu(self):
        driver = self.driver
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title,"unittest_百度搜索",msg='title错误')

    def tearDown(self):
        driver = self.driver
        driver.quit()
if __name__ == '__main__':
        unittest.main()