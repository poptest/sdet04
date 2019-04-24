## encoding:utf-8

runyear=int(raw_input("请输入年份"))
if(runyear<0):
    print (str(runyear)+"年份输入错误，请输入大于0的整数")
elif(int(runyear%4==0) and int(runyear%100!=0)):
    print (str(runyear)+"是闰年")
elif(int(runyear%400==0)):
    print (str(runyear)+"是世纪闰年")


else:
    print (str(runyear)+"不是闰年")

