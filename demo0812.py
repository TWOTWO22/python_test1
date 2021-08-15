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
class GirFriend():
    def _init_(self):    #类的属性
        self.sex="女"
        self.high="170cm"
        self.weight="55kg"    
        self.hair="大波浪" 
        self.age="18岁"
    def caiyi(self,num):  #才艺表演
        if num==1:
            print("胸口碎大石！")
        elif num==2:
            print("唱跳")
        else:
            print("单手开瓶盖")

zhangsan=GirFriend()
zhangsan.caiyi(2)
