#-*- coding:utf-8 -*-
import unittest

from laidada.jisuan import jsmj
class MyTestCase(unittest.TestCase):
    def test_case01(self):
        exp_val = 3
        act_val = jsmj(3, 1)
        self.assertEqual(exp_val, act_val)



if __name__ == '__main__':
    unittest.main()
