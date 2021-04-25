num = 1
while num <= 100:
    if num % 2 == 1:
        print(num)
    num = num + 1

num = 1
total = 0
while num <= 100:
    if num % 2 == 1:
        total = total + num
    else:
        total = total - num
    num = num + 1
print(total)
