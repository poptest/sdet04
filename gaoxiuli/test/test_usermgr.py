import unittest

from gaoxiuli.usermgr import login

class MyTestCase(unittest.TestCase):
    def test_something(self):
        name = "admin"
        password = "123456"
        ret = login(name,password)
        print (ret)


if __name__ == '__main__':
    unittest.main()
