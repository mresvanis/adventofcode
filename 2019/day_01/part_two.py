#!/usr/env/bin python


def __compute_fuel():
    def __compute_added(fuel):
        added = (fuel // 3) - 2
        if added <= 0:
            return 0
        return added + __compute_added(added)

    with open('input.txt', 'r') as f:
        fuel = [__compute_added(int(x)) for x in f.readlines()]
    return sum(fuel)


if __name__ == '__main__':
    print(__compute_fuel())
