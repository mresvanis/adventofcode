#!/usr/bin/env python3


def __correct_box_id():
    length = None

    with open('input.txt', 'r') as f:
        lines = [x.rstrip() for i, x in enumerate(f)]

    length = len(lines[0])

    for i, x in enumerate(lines):
        for j, y in enumerate(lines):
            if i == j:
                continue

            res = [a for a, b
                   in zip(list(x.rstrip()), list(y.rstrip()))
                   if a == b]

            if length - len(res) <= 1:
                return ''.join(res)


if __name__ == '__main__':
    print(__correct_box_id())
