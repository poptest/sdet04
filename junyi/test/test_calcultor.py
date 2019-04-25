# -*- encoding:utf-8 -*-
import unittest
from junyi.calcultor import jia

class MyTestCase(unittest.TestCase):

    def test_case01(self):
        # 定义期望值
        exp_val = 2
        # 获取实际值
        act_val = jia(1, 1)
        # 判断(断言) 期望值和实际值相等
        self.assertEqual(exp_val, act_val)

    def test_case02(self):
        # 定义期望值
        exp_val = 3
        # 获取实际值
        act_val = jia(1, 1)
        # 判断(断言) 期望值和实际值相等
        self.assertEqual(exp_val, act_val)

    def test_case03(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
