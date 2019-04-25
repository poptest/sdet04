import unittest

from WZ.usergmr import login
class MyTestCase(unittest.TestCase):
    def test_something(self):
       name="admin"
       pased="123456"
       ret=login(name,pased)
       print (ret)


if __name__ == '__main__':
    unittest.main()
