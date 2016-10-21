# -*- coding: 1251 -*-

import os

f = []
files = os.listdir('.')

files.sort()

for file in files:
    size = os.path.getsize('./{}'.format(file))
    print('{:<40}{}'.format(file, size))
