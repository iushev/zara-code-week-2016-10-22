# -*- coding: 1251 -*-

num = int(input("�������� �����: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("����������, ��������� �� ���������� �� ����������� �����")
elif num == 0:
    print("��������� �� 0 � 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("��������� �� {} � {}".format(num, factorial))
