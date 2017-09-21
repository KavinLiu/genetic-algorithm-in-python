# !/bin/python
# coding=utf-8

import math
import random


def fit_value(x):
    x = int(''.join(x), 2)
    x = x * 9.0/(2 ** 17 - 1)
    return x + 10*math.sin(5*x) + 7*math.cos(4*x)


def cross_value(a, b):
    c = ['0'] * len(a)
    sample = random.sample(range(len(a)), len(a)/2 + 1)
    for i in range(len(a)):
        if i in sample:
            c[i] = a[i]
        else:
            c[i] = b[i]
        if random.random() <= 0.000001:  # 十万分之一的变异概率
            c[i] = '1' if c[i] == '0' else '0'
    return c


def new_group(min_group):
    group_size = 100
    res = list()
    while True:
        a, b = random.sample(min_group, 2)
        c = cross_value(a, b)
        res.append(c)
        if len(res) == group_size:
            return res

init_a = [random.choice(['0', '1']) for i in range(1700)]
init_group = [[init_a[j*17+i] for i in range(17)] for j in range(100)]
for g in range(3000):
    valued_group = map(lambda x: [x, fit_value(x)], init_group)
    sorted_group = sorted(valued_group, key=lambda x: x[1], reverse=True)[:30]
    selected_group = map(lambda x: x[0], sorted_group)
    init_group = new_group(selected_group)
result = fit_value(init_group[-1])
print result
