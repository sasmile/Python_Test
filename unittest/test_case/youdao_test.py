#coding=utf-8
import unittest,time
from selenium import webdriver

class youdao_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.youdao.com')
    def test_youdao(self):
        driver = self.driver
        driver.find_element_by_name('q').send_keys('你好')
        driver.find_element_by_tag_name('button').submit()
        page_source = driver.page_source
        self.assertIn('hi',page_source)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()