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
def checkuser(name,password):
    if len(name)>2 and len(name)<5:
        if len(password)>5:
            print("注册成功",{name,password})
    else:
        print("用户和密码输入错误")
checkuser("aaa","123456")



