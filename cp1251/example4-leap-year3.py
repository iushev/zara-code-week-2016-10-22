# -*- coding: 1251 -*-

from leapyear import isLeap


year = int(input("�������� ������: "))

if isLeap(year):
    print("{0} � ��������� ������".format(year))
else:
    print("{0} �� � ��������� ������".format(year))
