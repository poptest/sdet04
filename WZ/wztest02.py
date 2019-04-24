# -*- encoding:utf-8 -*-
year = int(raw_input("请输入整数型的年份："))
if year>=0:
    if year%4==0and year%100!=0:
        print "公元"+str(year)+"年是普通闰年"
    elif  year%400==0:
        print "公元"+str(year)+"年是世纪闰年"
    else:print "公元"+str(year)+"年不是闰年"
elif year%4==0and year%100!=0:
    print "公元前"+str(-year)+"年是普通闰年"
elif year%400==0:
    print "公元前"+str(-year)+"年是世纪闰年"
else:print "公元前"+str(-year)+"年不是闰年"
