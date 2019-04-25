import unittest
from huxu.denglv import reglis


class MyTestCase(unittest.TestCase):

        usname1="admin"
        cipher2=123456
        ret = reglis(usname1,cipher2)
        print ret

if __name__ == '__main__':
    unittest.main()
