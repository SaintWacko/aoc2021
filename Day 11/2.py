import numpy as np
import sys


def main():
    flashes = 0
    step = 0
    with open('input', 'r') as file:
        octopi = np.array([[int(y) for y in list(x)] for x in file.read().splitlines()])
        while True:
            step += 1
            octopi = octopi + 1
            while np.any(octopi > 9):
                for (y, x), n in np.ndenumerate(octopi):
                    area = octopi[max(y - 1, 0):y + 2, max(x - 1, 0):x + 2]
                    if n > 9:
                        octopi[y][x] = 0
                        flashes += 1
                        area[:][area > 0] = area[area > 0] + 1
            if np.all(octopi == 0):
                return step


if __name__ == "__main__":
    print(main())
