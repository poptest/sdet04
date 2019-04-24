# -*- encoding:utf-8 -*-

score = int(raw_input("请输入学员分数："))

if score>90 and score<=100:
     print("等级A")
elif score>80 and score<=90:
     print("等级B")
elif score>60 and score<=80:
     print("等级C")
elif score>=0 and score<=60:
     print("等级D")
else:
    print("请输入正确成绩")
print score
print ("Hello World")