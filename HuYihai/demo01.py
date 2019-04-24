# -*- encoding:utf-8 -*-
a = int(raw_input("请输入年份："))
"a = %s"
b = 4
c = 100
d = 400
if a>0 and a%b==0 and a%c!=0:
    print("这是普通闰年")
elif a>0 and a%d==0:
    print("这是世纪闰年")
else:
    print("这不是闰年")
print ("Hello World")
