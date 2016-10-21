# -*- coding: 866 -*-

num = int(input("Въведете число: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Съжаляваме, факториел не съществува за отрицателни числа")
elif num == 0:
    print("Факториел от 0 е 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("факториел от {} е {}".format(num, factorial))
