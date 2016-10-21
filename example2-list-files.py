# -*- coding: utf-8 -*-

import os

f = []
files = os.listdir('.')

for file in files:
    size = os.path.getsize('./{}'.format(file))
    print('{:<40}{}'.format(file, size))
