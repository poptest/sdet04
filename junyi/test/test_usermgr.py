import unittest

from junyi.usermgr import login

class MyTestCase(unittest.TestCase):

    def test_case01_succeess(self):
        uname = "admin"
        pased = "123456"
        ret = login(uname, pased)
        print(ret)

    def test_case02_fail(self):
        uname = "admin"
        pased = "1234567"
        ret = login(uname, pased)
        print(ret)




if __name__ == '__main__':
    unittest.main()
