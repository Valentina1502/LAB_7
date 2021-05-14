#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# 0.43 4.4 -6.876 3.545 3.5343 -2.43 7.6 -45.5 0.432 45.54

if __name__ == '__main__':
    # ввод списка одной строкой
    A = tuple(map(float, input("Введите списok: ").split()))

    # вывод суммы нечетных элементов
    s = 0
    for i, item in enumerate(A):
        if i % 2 == 1:
            s += A[i]
    print(f"1)  Сумма нечетных эл-ов списка: {s}")
    # 1 и последний отриц. эл-ты
    f, l, f_item, l_item = 0, 0, 0, 0
    for x, item in enumerate(A):
        if item < 0:
            f, f_item = x, item
            break
    for x, item in enumerate(A):
        if item < 0:
            l, l_item = x, item
    print(f"2)  Первый {f_item} и последний {l_item} отрицательные эл-ты")
    m_A = A[f+1:l:1]            # Срез списка
    print(f"Сумма эл-ов между ними ({m_A}) = {sum(m_A)}")

    Aee = tuple(sorted(A, key=lambda x: math.fabs(x)))
    print(Aee)
    n = 0
    t = ()
    for i in range(len(A)):
        if math.fabs(Aee[i]) < 1:
            n = i
            t = t + (0, )
    c = Aee[n+1:] + t

    print(f"3)  Измененный список: {c}")
