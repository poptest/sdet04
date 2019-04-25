# -*- encoding:utf-8 -*-
import unittest

#选择被测试的单元函数
from Kane.calculate import add

class MyTestCase(unittest.TestCase):
    '''用例测试01'''
    #单元函数测试
    def test_case01(self):
        #定义期望值
        exp_val=2
        #获取实际值
        act_val=add(1, 1)
        #判断（断言）期望值和实际值相等
        self.assertEqual(exp_val, act_val)

    def test_case02(self):
        # 定义期望值
        exp_val = 3
        # 获取实际值
        act_val = add(1, 1)
        # 判断（断言）期望值和实际值相等
        self.assertEqual(exp_val, act_val)

if __name__ == '__main__':
    unittest.main()
