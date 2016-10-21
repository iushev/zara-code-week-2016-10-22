# -*- coding: 1251 -*-


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    return 1 if (n < 1) else n * factorial2(n - 1)


num = int(input("�������� �����: "))

if num < 0:
    print("����������, ��������� �� ���������� �� ����������� �����")
else:
    print("��������� �� {} � {}".format(num, factorial(num)))
