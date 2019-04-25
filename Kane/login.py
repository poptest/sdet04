# -*- encoding:utf-8 -*-

#声明一个登录的方法
def userlogin(username, password):

    #对用户名和密码进行判断,如果用户密码正确就返回1，反之返回0
    if username=="kane" and password=="123456":
        return 1
    else:
        return 0