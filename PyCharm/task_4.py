#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys


def get_input():
    get_str = input("Введите число: ")
    return get_str


def test_input(b):
    return b.isdigit()


def str_to_int(b):
    return int(b)


def print_int(c):
    print(c)


if __name__ == '__main__':
    a = get_input()
    bol = test_input(a)
    if bol:
        ch = str_to_int(a)
        print_int(ch)
    else:
        print(f"ошибка", file=sys.stderr)
