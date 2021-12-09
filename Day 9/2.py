import numpy as np

values = []


def main():
    global values
    with open('input', 'r') as file:
        basins = []
        values = np.array([[int(y) for y in list(x)] for x in file.read().splitlines()])
        for (x, y), n in np.ndenumerate(values):
            h = values[max(x - 1, 0):min(x + 2, len(values)), y]
            v = values[x, max(y - 1, 0):min(y + 2, len(values[0]))]
            if (n == np.min(h) and np.count_nonzero(h == n) < 2) and (n == np.min(v) and np.count_nonzero(v == n) < 2):
                basin = seek(x, y)
                basins.append(basin)
        return(np.prod(sorted(basins)[-3:]))


def seek(x, y):
    if x == -1 or y == -1:
        return 0
    try:
        if values[x][y] < 9:
            values[x][y] = 9
            return 1 + seek(x + 1, y) + seek(x - 1, y) + seek(x, y + 1) + seek(x, y - 1)
        return 0
    except IndexError:
        return 0


if __name__ == "__main__":
    print(main())
