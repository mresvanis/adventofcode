#!/usr/bin/env python3

from itertools import groupby


def __compute_counters(arg):
    if not isinstance(arg, (list,)):
        arg = list(arg)

    arg_sorted = sorted(arg)

    return [len(list(group))
            for key, group in groupby(arg_sorted)]


def __checksum():
    twos = threes = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        while (line):
            counters = __compute_counters(line.rstrip())

            if 2 in counters:
                twos += 1
            if 3 in counters:
                threes += 1

            line = f.readline()

    return twos * threes


if __name__ == '__main__':
    print(__checksum())
