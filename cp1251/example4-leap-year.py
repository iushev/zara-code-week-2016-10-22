# -*- coding: 1251 -*-

# https://bg.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D0%B0_%D0%B3%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0

year = int(input("Въведете година: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} е високосна година".format(year))
        else:
            print("{0} не е високосна година".format(year))
    else:
        print("{0} е високосна година".format(year))
else:
    print("{0} не е високосна година".format(year))
