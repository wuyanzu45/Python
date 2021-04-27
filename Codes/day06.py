# 猜年龄
count = 3
while count > 0:
    age = input("输入你猜的年龄：")
    count -= 1
    if age == "14":
        print("恭喜猜对！")
        break
    else:
        print("猜错了!")
        if count == 0:
            if input("是否继续(Y/N)?") == "Y":
                count = 3
            else:
                break







