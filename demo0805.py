# 1. 判断
# 判断一
# a=int(input("请输入a的值："))
# if a==2:
#     print("a的值等于2")
# 判断二
# a=int(input("请输入a的值："))
# b=int(input("请输入b的值："))
# if a<b:
#     print("a的值小于b")
# else:
#     print("a的值大于b")
# 判断三
# weight=float(input("请输入你的体重（斤）："))
# if weight<80:
#     print("你不需要减肥了")
# elif weight<=80 and weight<90:
#     print("你可能需要减肥了")
# elif 90<=weight<100:
#     print("你必须要减肥了")
# else:
#     print("你真的真的需要减肥了")
# tips：a.判断条件的细节：if+条件+冒号  换行  空四格（一个缩进）
#       b.if条件判断是从上面运行到下面，符合条件就不再运行了
#       c.判断条件相等用==，赋值用=
#       e.判断条件有==、!=、>、<、in、is、not in、not is 
# in的用法
# a="您好，啊啊啊啊"
# if "您好" in a:
#     print("正确")
# b=input("请输入b的值:")
# if b=="":
#     print("输入的值不能为空")
#     exit()
# if b in "123456789":
#     b=int(b)
# else:
#     print("请输入正确的数值")
#     exit()  #如果满足继续执行
# if b>5:
#     print("b的值大于5")
# is的用法
# a=input("请输入a的值：")
# if type(a) is int:
#     print("a的类型是数值")
# elif type(a) is str:
#     print("a的类型的字符串")
# else:
#     print("a的类型是其他")

# 2. 循环
# while循环
# a=1
# while a<3:
#     print("a第",a,"次循环")
#     a=a+1
# 练习一
# 现在有5个学生的成绩，需要录入到系统当中
# 这10个人分别是: 张三、李四、王五、王麻子、刘能
# 并且名字和成绩需要对应上
# 而且大于60和小于60的需要分开储存
# 方法一用while循环
# a={} #定义一个空字典来储存成绩大于等于60的学生
# b={} #定义一个空字典来储存成绩小于60的学生
# student=["张三","李四","王五","王麻子","刘能"] 
# c=0 #相当于第一个值的下标 
# while c<len(student):
#     grade=input("请输入学生"+student[c]+"的成绩:")  #录入成绩
#     if float(grade)>=60: 
#         a[student[c]]=grade  #存在字典中
#     else:
#         b[student[c]]=grade
#     c=c+1 #下标+1 再去取值
# print("大于等于60的学生的成绩",a)
# print("小于60的学生的成绩",b)
# 方法二用for循环来解决问题
# a={} #定义一个空字典来储存成绩大于等于60的学生
# b={} #定义一个空字典来储存成绩小于60的学生
# student=["张三","李四","王五","王麻子","刘能"] 
# for i in student:
#     grade=input("请输入学生"+i+"的成绩:")  #录入成绩
#     if float(grade)>=60: 
#         a[i]=grade  #存在字典中
#     else:
#         b[i]=grade
# print("大于等于60的学生的成绩",a)
# print("小于60的学生的成绩",b)

# for循环
# a="你好，今天天气怎么样"
# for i in a:
#     print(i)  #把i作为遍历对象，挨着遍历字符串里面的值
# b=["张三","李四","王五"]
# for i in b:
#     print(i)  #把i作为遍历对象，挨着遍历数组
# range（）方法的使用
# a=list(range(0,10)) # 自动生成一个数列
# print(a)
# b=list(range(0,10,2))
# print(b)
# for i in range(10):    #range（10） 默认是1,10的数字，左闭右开
#     print(i)
# for i in range(0,10):  #list(range(0,10))是0到10的数组
#     print(i)
# for i in range(0,10,2):
#     print(i)  #range(0,10,2)是步长、步进为2的数字 

# 练习二 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end=" ")
#     print()
# 解释 
# 当第一次循环时
# i=1 j=1
# 1*1=1
# 第二次循环的时
# i=2 j=1 j=2
# 2*1=2 2*2=4

#end()和print()的作用
# a=["张三","李四"]
# for i in a:
#      print(i,end="||")   #print里面的参数end是使它不换行
#      print("-----")      #print里面的作用就是让他换行

#练习三 通过print打印，模拟一个红绿灯，注意：红灯30次，绿灯35次，黄灯3次
#方法一
# a=0
# while a==0:
#     for i in range(30,0,-1):
#         print("红灯还有",i,"秒结束")
#     for j in range(36,0,-1):
#         print("绿灯还有",j,"秒结束")
#     for k in range(3,0,-1):
#         print("黄灯还有",k,"秒结束")
#方法二 
# light={"红灯":30,"绿灯":36,"黄灯":3} #定义一个字典 可维护性很很高
# while True: #死循环和while 1 一样
#     for i in light:  #for循环中i取值取得是key值
#         for j in range(light[i]):
#             print(i,"倒计时结束还有",light[i]-j,"秒")


#练习四 
# 使用代码，实现一个注册功能 用户输入账户和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头
# 并且储蓄到字典中
# 方法一
# a={}
# username=input("请输入用户名：")
# password=input("请输入用户名密码：")
# if len(username)>=5 and len(username)<=8 and len(password)>=6 and len(password)<=12 and username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#     print("用户名输入正确")
#     a[username]=password
#     print(a)
# else:
#     print("用户名或密码输入错误，请重新输入")
#方法二
# username=input("请输入用户名：")
# password=input("请输入用户名密码：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         if len(password)>=6 and len(password)<=12:
#             print("注册成功",{username:password})
#         else:
#             print("用户密码长度必须是6-12位")
#     else:
#         print("用户名的首字母必须小写")
# else:
#     print("用户名长度必须是5-8位")

# continue和break的作用
# for i in range(10):
#     if i==5:
#         continue  #跳出当前循环 继续执行下一循环
#     print(i)
# for i in range(10):
#     if i==5:
#         break  #终止当前循环，不在执行
#     print(i)
# tips：continue和break 都只在当层循环中起作用


