#coding=utf-8
import unittest
import baidu_test, youdao_test

suite = unittest.TestSuite()
suite.addTest(baidu_test.baidu_test('test_baidu'))
suite.addTest(youdao_test.youdao_test('test_youdao'))

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)