# -*- encoding:utf-8 -*-
year=(raw_input("请输入一个年份："))
try:
    int(year)
except:
    print "请输入正确年份格式"