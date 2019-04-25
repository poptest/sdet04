import unittest

from laidada.laidada import login
class MyTestCase(unittest.TestCase):

    def test_something(self):
        name = "admin"
        key = "123456"
        msg = login(name,key)
        print(msg)



if __name__ == '__main__':
    unittest.main()
