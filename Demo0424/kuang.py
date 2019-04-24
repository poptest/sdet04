#-*-encoding:utf-8 -*-
#输入年份
str_age=raw_input("请输入年份")
#更改数据类型
age=float(str_age)
#判断数据是否是小数
if str_age.count(".")==1:
    print ("请输入一个整数年")
#判断是否是大于0
elif(age>0):
    #大于0时的判断
    if int(age)%4==0 and intern(age)%100!=0:
        print ("%s是普通闰年"%age)
    elif(age%400==0):
        print ("%s是世纪闰年"%age)
    else:
        print ("%s不是闰年"%age)
#0不做判断
elif age==0:
    print ("%s不计算在内")%(age)

else:
    print ("输入的年有误")
