# -*- coding: 866 -*-

from leapyear import isLeap


year = int(input("�ꢥ��� ������: "))

if isLeap(year):
    print("{0} � ��᮪�᭠ ������".format(year))
else:
    print("{0} �� � ��᮪�᭠ ������".format(year))
