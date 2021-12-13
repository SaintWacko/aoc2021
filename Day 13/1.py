import numpy as np


def main():
    with open('input', 'r') as file:
        points, folds = [line.splitlines() for line in file.read().split('\n\n')]
        points = np.array([p.split(',') for p in points]).astype(int)
        folds = [x.split()[2].split('=') for x in folds]
        dimensions = list(zip(*points[::-1]))
        xmax = max(dimensions[0])
        ymax = max(dimensions[1])
        grid = np.zeros((ymax + 1, xmax + 1))
        for x, y in points:
            for fold in folds[:1]:
                if fold[0] == 'x':
                    x = 0 - abs(x - int(fold[1])) + int(fold[1])
                if fold[0] == 'y':
                    y = 0 - abs(y - int(fold[1])) + int(fold[1])
            grid[y][x] = 1
        return np.count_nonzero(grid)


if __name__ == "__main__":
    print(main())
