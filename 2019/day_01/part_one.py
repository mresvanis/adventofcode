#!/usr/env/bin python


def __compute_fuel():
    with open('input.txt', 'r') as f:
        fuel = [(int(x) // 3) - 2 for cnt, x in enumerate(f)]
    return sum(fuel)


if __name__ == '__main__':
    print(__compute_fuel())
