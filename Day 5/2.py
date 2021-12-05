import numpy as np


def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        coords = [np.array([[int(n) for n in l.split(',')] for l in line.split(' -> ')]) for line in lines]
        max = np.amax(coords)
        grid = np.zeros(shape=(max + 1, max + 1))
        for coord in coords:
            rot = list(zip(*coord))
            cols = sorted(rot[0])
            rows = sorted(rot[1])
            area = grid[rows[0]:rows[1] + 1, cols[0]:cols[1] + 1]
            if any(np.all(coord == coord[0, :], axis=0)):
                area[:] = area + 1
            else:
                if (rot[0][0] > rot[0][1]) == (rot[1][0] > rot[1][1]):
                    np.fill_diagonal(area[:], area.diagonal() + 1)
                else:
                    np.fill_diagonal(np.fliplr(area[:]), np.fliplr(area).diagonal() + 1)
        return((grid > 1).sum())


if __name__ == "__main__":
    print(main())
