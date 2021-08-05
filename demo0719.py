# 1.数据类型
"""
print("python数据类型：")
print ("hello word!") #字符串
print (2333) #整数
print(2.33)  #小数
print(True) # 布尔值
print(())  # 元祖
print([])  # 数组
print({}) # 字典
"""

# 2. 数据运算符
"""
print("python运算符：")
print("哈哈",3333)
print("哈哈"+"嘻嘻")  #字符串拼接
print("哈哈"*10)
print((1+2)*(100-99)/2) #数字的运算 
print(2>3) #布尔值 用在判断里面
"""

# 3. 变量和赋值
"""
print("变量和赋值：")
name="张三" #把张三这个值赋值给了名字叫name的这个变量
print(name)

初闻不见山之高
再问已是山中人
"""

# 4.input的使用
"""
print("哈哈",3333)
a=input("请输入：") #输入内容
b=input("请输入： ")
print("input获取的内容：",a)
print("input获取的内容：",a+b)  #input默认都是字符串的拼接，引申出字符串的转换
"""
# 5. 数据类型的转换
"""
c=type(123) #把123转换成字符串123
print(c)
print(type("哈哈"))
print(type(123))
print(type(2.33))
print(type(True))
print(type(()))
print(type([]))
print(type({}))
a=int("2333")
print(type(a))
"""
#练习一
"""
print("作业布置(数字的相加)：")
a=float(input("请输入a的值："))
b=float(input("请输入b的值："))
print("input获取a+b的值:",a+b)   #input默认的是字符串
"""

# 6.len()方法的使用
"""
c="123456789"
print(len(c)) #只支持求字符串、元组、数组、字段的长度
"""
#练习二
"""
print("练习1：通过代码获取两段不同的内容，并且计算他们长度的和")
a=(input("请输入a内容:"))
b=(input("请输入b内容："))
print("方法一--a和b内容长度的和",len(a)+len(b))
print("方法二--a和b内容长度的和：",len(a+b))
print("总结1")
"""

# 7. 元组  下标的编号从0开始
"""
a=(1,2,3,4,5,6,7,8,9,"哈哈","哈哈","嘻嘻",True,False)
print("打印元组里面所有的内容：",a)
print("只打印元组里面的哈哈：",a[4])
print("利用元组自带的方法查找某个值的下标index：",a.index("嘻嘻"))
print("当元组中有相同的值时index默认获取第一个值的下标：",a.index("哈哈"))
print("统计某个值在元组中的个数count：",a.count("哈哈"))
#  二维元组
b=(a,"哈哈","嘻嘻")
print("二维元组：",b) #一共3个值
print("取出b中的嘻嘻：",b[2])
print("取出a中的数字4：",b[0][3])
 切片 （批量取值）左闭右开
print("批量取出a元组中的数字方法一：",a[0:9])
print("批量取出a元组中的数字方法二：",a[:9])
print("批量取出a元组中的字符串：",a[9:12])
print("批量取出a元组中的布尔值方法一：",a[12:14])
print("批量取出a元组中的布尔值方法二：",a[12:])
print("批量取出a元组中的所有值：",a[:])"""

#  8. 数组
"""
# 元组和数组的区别：元组写好之后不能修改（写死的），数组可以写好之后可以修改
a=[1,2,3,4,5,6,7,8,9,"哈哈","哈哈","嘻嘻",True,False]
print("只取出a数组中的嘻嘻：",a[11])
print("在a数组中查找数字4的下标值：",a.index(4))
print("统计a数组中哈哈的数量：",a.count("哈哈"))
b=a.append("append1") #往数组追加数据
print("在a数组中的末尾插入一个为append1的值：",a)
print("错误：在a数组中的末尾插入一个为append1的值：",b) #错误示范 ，append是在队列末尾进行操作，这样会输出None
c=a.insert(0,"insert1") #在数组下标签插入数据
print("在a数组中1的前面面插入一个为insert1的值：",a)
print("错误：在a数组中1的后面插入一个为insert1的值：",c) #错误示范 ，insert是在队列里面进行操作，这会样输出None
d=a.pop(0) #从数组中剪切下标为0的值  需要看最后一个print打印出来的值
print("在a数组中剪切下标为0的值是：",d) #打印出剪切的值
print("打印出剪切之后a数组：",a) #打印出剪切之后的a数组
e=a.pop(0) #剪切出数字1
f=a.pop(0) #剪切出数字2
print("输出剪切出的e和f相加之和：",e+f)
print(a)
# a.clear() #清空a中的值，使其变成一个空数组
# print("输出清空a数组：",a)
g=[10,11,"嘿嘿"] 
a.extend(g) #往数组中加一个
print("往a数组中加一个g数组方法一",a) #和append去区别：extend可以插入一个数组，而append只能插入一个值
print("往a数组中插入一个g数组方法二：",a+g)  #数组可以直接相加
a.remove(4) #移走a中的数字4  和pop的区别：pop可以赋值，而remove不能赋值，只是对a进行操作
print("移除a中的数字4：",a)
h=[True,1,False,0] #一般会将true识别成1，false识别为0
print("查看true，1，false，0中有几个1：",h.count(1))
# tips：
# a.无论是元组还是数组，输入下标都不能越界，否则代码会报错
# b.所有的方法都是以()的方式，eg：print(),input()
# c.元组，数组，字典的取值，都是用中括号[] eg:a[0]
# d.元组，数组，字典的定义分别是(),[],{} 
"""

#8.字典
"""
# 字典的特点
# a. 字典中的值是没有顺序的
# b. 字典中的结构必须是 键值对的结构  key：value
# d. 字典中的取值都是通过可以去取value的值
# e. 所有的字符串都必须加引号
a={"name":"张三",0:"哈哈","age":18}
print("向a字典中取姓名这个值:",a["name"]) #取值
a["high"]="180cm" #新增值 字典中不存在的
print("向a字典新增一个high键值对：",a) 
a["name"]="李四" #修改值 字典中存在的
print("修改字典a中的name的值：",a)
b=a.get("name") #get方法取值
print("用get方法在字典a中取出name的值：",b)
# print(a.get("name1"))
# print(a["name1"])  #get方法取值和直接取值区别：当key不存在时，get返回的none而直接取值直接报错
c=a.pop("name") #剪切值
print("用pop向字典a中取出name这个键值对：",c)
print("取出name之后的字典a：",a)
a.update(weight="45kg") #更新 可以修改也可以增加 weight在这里相当于变量，不加引号
print("用update向字典中增加一个weight值：",a)
a.update(weight="40kg")
print("用update向字典中修改weight值：",a)
# 数组和字典的删除
del a[0] #字典的删除
print("删除a字典中的0键对值：",a)
d=[1,2,3,4,5]
del d[0] #数组的删除
print("删除d数组中小标为o的值：",d)
"""

#练习三
# print("练习三：获取用户输入的个人信息，并且储存到字典中，个人信息包括了，name、age、sex")
a={}
b=input("请输入用户的name值：")
c=input("请输入用户的age值：")
d=input("请输入用户的sex值：")
a["name"]=b #用直接取值的方法添加
a.update(age=float(c))
a.update(sex=d)
print("获取name，age，sex之后打印a字典：",a)
# # a.update(name=b,age=c,sex=d)  #update可以同时
# # print(a)
# # a={"name":b,"age":c,"sex":d}
# # print(a)
