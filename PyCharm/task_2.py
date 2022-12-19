#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import math
import sys


def cylinder():
    """""
    Вычисление площади полной/боковой поверхности цилиндра
    """""
    while True:
        com = int(input("Вычисление площади поверхности цилиндра (введите число):\n"
                        "1 - Боковой поверхности\n"
                        "2 - Полной поверхности\n"))
        if (com != 1) and (com != 2):
            print(f"Неверное число {com}", file=sys.stderr)
            break

        r = int(input("Введите радиус "))
        h = int(input("Введите высоту "))

        if com == 1:
            s = 2 * math.pi * r * h
            print("S(бок.) = ", '{:.3f}'.format(s))
            break

        elif com == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S(полн.) = ", '{:.3f}'.format(s))
            break


def circle(r):
    """""
    Вычисление площади круга по введенному радиусу
    """""
    return math.pi * (r ** 2)


if __name__ == '__main__':
    cylinder()
