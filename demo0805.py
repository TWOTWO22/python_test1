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
a=1
while a<3:
    print("a第",a,"次循环")
    a=a+1
