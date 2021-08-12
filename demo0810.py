# 1. 方法/函数
# Python自带的方法有print()、input()、type()......
# 方法的自定义
# def checkname(a):  # def--方法的声明 checkname--方法的名称 a--参数 if--方法的逻辑代码
#     if a>0:
#         print("a大于0")
#     else:
#         print("a小于0")
# checkname(-1) #方法的调用
# def sum(a,b):
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         print("输入的a和b不是数值，不能相加")
# sum(1,8)

# c=[]
# c.append("哈哈")
# print(c) #打印哈哈
# print(c.append("哈哈")) #打印None
# print(c.count("哈哈"))  #打印2 count是一个值

# 引出return
# def sum(a,b):
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return "输入的a和b不是数值，不能相加"
# print(sum(1,3))  #返回值 返回只有我们可以对这个值进行其他的操作  但是如果直接是print的话 则不能进行操作

# a=[1,2,3,4]
# b=a.index(1)
# print(a[b])

# 2. 异常捕获
# try:  except: 异常捕获 联动
# try:
#     print("a"+1)
# except:
#     print("代码错误！")

# a=input("请输入姓名：")
# b=input("请输入年龄：")
# try:
#     if int(b)>18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except Exception  as e:  #exception 是异常类
#     print("您输入的年龄错误：",e)