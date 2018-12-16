#!/usr/bin/env python3


def __compute_frequency():
    with open('input.txt', 'r') as f:
        changes = [int(x) for cnt, x in enumerate(f)]

    return sum(changes)


if __name__ == '__main__':
    print(__compute_frequency())
