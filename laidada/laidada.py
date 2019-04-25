#-*- coding:utf-8 -*-
def login(username, password):
    if username == "admin" and password == "123456":
        return ("登入成功")
    else:
        return ("登入失败")