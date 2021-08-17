import time
now=time.strftime("%Y-%m-%d %H:%M:%S")
text=input("请输入今天收藏的小短句：") #输入内容,把语句收藏存在F:\python-test
with open("F:\python-test\语句收藏.txt","a",encoding="utf8") as f: #参数w：每次写入的都是新的内容之前的都清空 参数a:追加每次写入的内容
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("----------------------------------")