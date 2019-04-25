import unittest
from yiongqi1.usergmr.usergmr import login

class MyTestCase(unittest.TestCase):
    def test_something(self):
        ret = login("zhaoyongqi","123456")
        print (ret)

if __name__ == '__main__':
    unittest.main()
