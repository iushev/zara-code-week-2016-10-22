# -*- coding: 866 -*-

print('Намислете си едно число от 1 до 10')

minVal = 1
maxVal = 10
val = 5

while True:
    print('{} ли е вашето число?'.format(val))
    print('    0: Да.')
    print('    1: Не моето число е по-малко.')
    print('    2: Не моето число е по-голямо.')
    answ = input("")
    if answ == 0:
        break
    elif answ == 1:
        maxVal = val
        val = minVal + (val - minVal) // 2
    else:
        minVal = val
        val = minVal + (maxVal - val) // 2

print('Довиждане')
