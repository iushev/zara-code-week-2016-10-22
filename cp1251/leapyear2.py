# -*- coding: 1251 -*-


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
    year = int(input("�������� ������: "))

    if isLeap(year):
        print("{0} � ��������� ������".format(year))
    else:
        print("{0} �� � ��������� ������".format(year))
