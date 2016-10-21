# -*- coding: 1251 -*-

from leapyear import isLeap


year = int(input("Въведете година: "))

if isLeap(year):
    print("{0} е високосна година".format(year))
else:
    print("{0} не е високосна година".format(year))
