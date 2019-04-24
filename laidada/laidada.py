#-*- coding:utf-8 -*-
year = int(raw_input("请输入一个年份:"))

if year%4==0 and year%100!=0:
    print("普通闰年")
elif year%400==0:
    print("世纪闰年")
else:
    print("不是闰年")