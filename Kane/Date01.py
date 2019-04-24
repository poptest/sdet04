# -*-encoding=utf-8-*-
str_date=raw_input("请输入一个年份")

#新建一个变量将输入的值转化为float类型的数据
date=float(str_date)
print("Weidong nihao")

#判断输入的数据是否大于0
if date<=0:
    print ("请正确输入年份")

#判断输入的数据是否为小数
elif str_date.count('.')==1:
    print ("请输入整数年份")
else:
    #判断输入的数据是否为闰年
    if date%4==0 and date%100!=0:
        print (str(date)+"年是一个闰年")
    elif date%400==0:
        print (str(date) + "年是一个闰年")
    else:
        print (str(date) + "年不是一个闰年")