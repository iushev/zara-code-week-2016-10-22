# -*- coding: 866 -*-

num = int(input("�ꢥ��� �᫮: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("�ꦠ���, 䠪�ਥ� �� �����㢠 �� ����⥫�� �᫠")
elif num == 0:
    print("����ਥ� �� 0 � 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("䠪�ਥ� �� {} � {}".format(num, factorial))
