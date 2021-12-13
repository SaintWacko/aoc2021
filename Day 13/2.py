import numpy as np


def main():
    with open('input', 'r') as file:
        points, folds = [line.splitlines() for line in file.read().split('\n\n')]
        points = np.array([p.split(',') for p in points]).astype(int)
        folds = [x.split()[2].split('=') for x in folds]
        xmin = min([int(x[1]) for x in folds if x[0] == 'x'])
        ymin = min([int(x[1]) for x in folds if x[0] == 'y'])
        grid = np.zeros((ymin, xmin))
        for x, y in points:
            for fold in folds:
                if fold[0] == 'x':
                    x = 0 - abs(x - int(fold[1])) + int(fold[1])
                if fold[0] == 'y':
                    y = 0 - abs(y - int(fold[1])) + int(fold[1])
            grid[y][x] = 1
        for row in grid:
            print(''.join(['#' if x else '.' for x in row]))


if __name__ == "__main__":
    print(main())
