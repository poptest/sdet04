# -*- encoding:utf-8 -*-

year=int(raw_input("请输入一个年份："))
if((year%4==0) and (year%100!=0)):
    print(str(year)+"是普通闰年。")
elif(year%400==0):
    print(str(year)+"是世纪闰年。")
elif(year==float):
    print (str(year)+"输入错误。")
else:
    print(str(year)+"不是闰年。")