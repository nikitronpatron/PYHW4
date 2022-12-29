# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input())

for i in range(1, num):
    if num % i == 0:
        temp = num / i 
        j = int(temp)
        print(f"{i} * {j}")
    
