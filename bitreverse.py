#!/usr/bin/env python
import sys


def rb2(n):
    b2n = bin(n).split('b')[-1]
    r_b2n = b2n[::-1]
    r_n = int(r_b2n, 2)
    return r_n


if __name__ == '__main__':
    number = int(sys.stdin.readline())
    print(rb2(number))
