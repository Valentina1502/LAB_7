#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    #ввод списка одной строкой
    A = tuple(map(int, input("Введите 10 элементов списка: ").split()))
    #кроверка кол-ва эл-тов
    if len(A) != 10:
        print("Размер списка не соответствует требованию", file=sys.stderr)
        exit(1)
    #сумма
    s = 0
    for item in A:
        if (item > 3 and item < 8):
            s += item

    print(f"Сумма элементов: {s}")
