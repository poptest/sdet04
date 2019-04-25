# -*- encoding:utf-8 -*-
import unittest

#选择被测试的单元函数
from Kane.login import userlogin

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #给测试的单元函数赋值进行测试
        username="kane"
        password="123456"
        #将赋值的变量传入到单元函数中
        result=userlogin(username, password)
        print (result)


if __name__ == '__main__':
    unittest.main()
