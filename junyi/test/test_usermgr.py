import unittest

from junyi.usermgr import login

class MyTestCase(unittest.TestCase):

    def test_something(self):
        uname = "admin"
        pased = "123456"
        ret = login(uname, pased)
        print(ret)



if __name__ == '__main__':
    unittest.main()
