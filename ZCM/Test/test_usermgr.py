import unittest

from ZCM.usermgr import login

class MyTestCase(unittest.TestCase):
    def test_something(self):
        user = "admin"
        pwd = "zcm980522"
        ret = login(user, pwd)
        print (ret)


if __name__ == '__main__':
    unittest.main()
