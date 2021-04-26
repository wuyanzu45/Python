count = 3
while count > 0:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name == "wuyanzu" and pwd == "123":
        print("登陆成功！")
        break
    else:
        print("用户名或密码错误！请重新输入！")
        count -= 1
        print(f"您还有{count}次输入机会！")