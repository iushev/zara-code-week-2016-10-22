# -*- coding: 866 -*-

print('����᫥� � ���� �᫮ �� 1 �� 10')

minVal = 1
maxVal = 10
val = 5

while True:
    print('{} �� � ���� �᫮?'.format(val))
    print('    0: ��.')
    print('    1: �� ���� �᫮ � ��-�����.')
    print('    2: �� ���� �᫮ � ��-���אַ.')
    answ = input("")
    if answ == 0:
        break
    elif answ == 1:
        maxVal = val
        val = minVal + (val - minVal) // 2
    else:
        minVal = val
        val = minVal + (maxVal - val) // 2

print('���������')
