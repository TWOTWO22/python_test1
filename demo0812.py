# import pymysql
# db=pymysql.connect(host="127.0.0.1",user="root",password="",db="test1227")
# cur=db.cursor()
# try:
#     cur.execute("select * from t_class;")
#     res=cur.fetchall()
#     print(res)
# except:
#     print("sql语句错误！")

# import time  #导入time包
# import random
# a=random.randint(1,10) # 1到10之间一个随机数
# print(a)
# for i in range(10):
#     time.sleep(2)
#     print(i)

#练习一
#定义一个方法，用来判断用户名的账号和密码是否符合规范
# def checkuser(name,password):
#     if len(name)>2 and len(name)<5:
#         if len(password)>5:
#             return("注册成功",{name,password})  #return True
#         else:
#             print("密码错误")
#     else:
#         print("用户和密码输入错误")
# a=checkuser("aaa","123456")
# print("嘿嘿",a)

#类 
#class 声明类的名称 类的名字首字母必须大写
#class Test():  类里面所有的方法都必须传一个参数
#面向对象编程 （类=对象）
# class GirlFriend():
#     # def __init__(self):    #类的属性
#     #     self.sex="女"
#     #     self.high="170cm"
#     #     self.weight="55kg"    
#     #     self.hair="大波浪" 
#     #     self.age="18岁"
    
#     def __init__(self,sex,high,weight,hair,age):
#         self.sex=sex
#         self.high=high
#         self.weight=weight
#         self.hair=hair
#         self.age=age

#     def caiyi(self,num):  #才艺表演
#         print("性别为",self.sex,"开始才艺表演")
#         if num==1:
#             print("胸口碎大石！")
#         elif num==2:
#             print("唱跳")
#         else:
#             print("单手开瓶盖")
#     def chuyi(self):  #厨艺
#         print("体重为"+self.weight+"开始厨艺表演")
#         print("精通八大菜系")
#     def work(self):   #工作
#         print("身高为"+self.high+"开始工作")
#         print("开挖掘机")

# #类的实例化
# # zhangsan=GirlFriend()
# zhangsan=GirlFriend("女","170cm","45kg","直发","18")
# zhangsan.caiyi(1)
# zhangsan.chuyi()
# zhangsan.work()
# print(zhangsan.high)

class Car():
    def __init__(self,appearance,brand):
        self.appearance=appearance
        self.brand=brand
    def fly(self):
        print(self.appearance+"的"+self.brand)
        print("会飞")
    def transform(self):
        print("变形")
landRover=Car("高端大气","路虎")
landRover.fly()
landRover.transform()

class NewCar(Car):  #newcar继承新车
    def fly(self):
        print(self.appearance+"的"+self.brand)
        print("不会飞哦")
Tesla=NewCar("小巧","特斯拉")
Tesla.fly()
        


