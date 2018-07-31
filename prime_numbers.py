lower = 1
upper = 100000000000

for num in range(lower, upper + 1):
    if num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            print(num)
