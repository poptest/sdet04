# -*- encoding:utf-8 -*-
for i in range(100):
    print("%s Hello World" %(i+1))

week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
print(week[0])
print(week[-1])
print(week[0:4])

#range(3)  >=0 and <3
for i in range(1,4):
    print(week[i])


for day in week:
    print(day)