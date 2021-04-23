import random
print("请在0~100中猜数字")
num = int(input("输入你要猜的数字："))
real_num = random.randint(0, 100)
count = 1
while num != real_num:
    if num > real_num:
        print("猜大了！")
    else:
        print("猜小了！")
    num = int(input("请重新输入："))
    count = count + 1
print("猜对了！猜的次数：", count)
