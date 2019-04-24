#-*-encoding:utf-8 -*-
str_age=raw_input("请输入年份")
age=float(str_age)
if str_age.count(".")==1:
    print ("请输入一个整数年")
elif(age>0):
    if int(age)%4==0 and intern(age)%100!=0:
        print ("%s是普通闰年"%age)
    elif(age%400==0):
        print ("%s是世纪闰年"%age)
    else:
        print ("%s不是闰年"%age)
elif age==0:
    print ("%s不计算在内")%(age)

else:
    print ("输入的年有误")
