import numpy as np


def main():
    with open('input', 'r') as file:
        total = 0
        values = np.array([[int(y) for y in list(x)] for x in file.read().splitlines()])
        for (x, y), n in np.ndenumerate(values):
            h = values[max(x - 1, 0):min(x + 2, len(values)), y]
            v = values[x, max(y - 1, 0):min(y + 2, len(values[0]))]
            if (n == np.min(h) and np.count_nonzero(h == n) < 2) and (n == np.min(v) and np.count_nonzero(v == n) < 2):
                total += 1 + n
        return total


if __name__ == "__main__":
    print(main())
