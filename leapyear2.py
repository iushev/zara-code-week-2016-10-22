# -*- coding: utf-8 -*-


def isLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    year = int(input("Въведете година: "))

    if isLeap(year):
        print("{0} е високосна година".format(year))
    else:
        print("{0} не е високосна година".format(year))
