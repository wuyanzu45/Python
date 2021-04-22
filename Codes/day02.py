name = input("请输入用户名：")
pwd = input("请输入密码：")
while name != "wuyanzu" or pwd != "123":
    print("用户名或密码错误，请重新输入！")
    name = input("请输入用户名：")
    pwd = input("请输入密码：")

print("登入成功！")
