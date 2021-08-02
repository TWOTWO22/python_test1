
"""
print("python数据类型：")
print ("hello word!") #字符串
print (2333) #整数
print(2.33)  #小数
print(True) # 布尔值
print(())  # 元祖
print([])  # 数组
print({}) # 字典

print("python运算符：")
print("哈哈",3333)
print("哈哈"+"嘻嘻")  #字符串拼接
print("哈哈"*10)
print((1+2)*(100-99)/2) #数字的运算 
print(2>3) #布尔值 用在判断里面

print("变量和赋值：")
name="张三" #把张三这个值赋值给了名字叫name的这个变量
print(name)

初闻不见山之高
再问已是山中人

"""

"""
print("哈哈",3333)
a=input("请输入：") #输入内容
b=input("请输入： ")
print("input获取的内容：",a)
print("input获取的内容：",a+b)  #input默认都是字符串的拼接，引申出字符串的转换
"""
# c=type(123)
# print(c)
# print(type("哈哈"))
# print(type(123))
# print(type(2.33))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a=int("2333")
# print(type(a))

# print("作业布置(数字的相加)：")
# a=float(input("请输入a的值："))
# b=float(input("请输入b的值："))
# print("input获取a+b的值:",a+b)

# c="123456789"
# print(len(c))

print("练习1：通过代码获取两段不同的内容，并且计算他们长度的和")
a=(input("请输入a内容:"))
b=(input("请输入b内容："))
print("方法一--a和b内容长度的和",len(a)+len(b))
print("方法二--a和b内容长度的和：",len(a+b))
