# -*- encoding:utf-8 -*-

year = int(raw_input("请输入一个年份:"))

if year % 4 == 0 and year % 100 != 0:
    print("%s是普通闰年" % year)

elif year % 400 == 0:
    print("%s是世纪闰年" % year)

else:
    print("%s不是闰年" % year)