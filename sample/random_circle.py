#!/usr/local/bin/python3
# coding: UTF-8

import random
import math


def circle(f, pl, delimiter, ir, cx, cy):
    for _ in range(pl):
        r = random.random() * math.pi * 2.0
        s = ir * math.sqrt(random.random())
        x = s * math.cos(r) + 200 + cx
        y = s * math.sin(r) + 200 + cy
        f.write(str(x) + delimiter + str(y) + '\n')


c1_r = 150
c2_r = 100
c1_plot = 10000
c2_plot = 5000
delimiter = ','

f = open('mouse_data', 'w')
circle(f, c2_plot, delimiter, c2_r, 0, 0)
circle(f, c2_plot, delimiter, c2_r, c2_r * 2, 0)
circle(f, c1_plot, delimiter, c1_r, c2_r, -c2_r * 2)

f.close()
