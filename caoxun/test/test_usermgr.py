import unittest

from caoxun.usermgr import login

class MyTestCase(unittest.TestCase):
    def test_something(self):
        usernm = "caoxun"
        passwd = "112233"
        ret = login(usernm,passwd)



if __name__ == '__main__':
    unittest.main()
