# -*- encoding:utf-8 -*-
print ("Hello Word !")

year = int(raw_input("请输入年份："))

if year%4==0 and year%100!=0:
    print ("%s年是普通闰年" % year)
elif(year%400==0):
    print ("%s年是世纪闰年"%year)
elif(year<=0):
    print ("%s年不是年份"%year)
else:
    print ("%s年不是闰年" % year)

print ("one day *_*")
print ("two day *_*")