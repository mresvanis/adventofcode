#!/usr/bin/env python3


def __compute_duplicate():
    results = {}
    freq = 0

    while (True):
        with open('input.txt', 'r') as f:
            line = f.readline()
            while (line):
                freq += int(line)

                if (str(freq) in results):
                    return freq

                results[str(freq)] = True

                line = f.readline()


if __name__ == '__main__':
    print(__compute_duplicate())
