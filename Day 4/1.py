import numpy as np

def main():
    with open('input', 'r') as file:
        lines = file.read().split('\n\n')
        balls = lines.pop(0).split(',')
        boards = [np.array([l.split() for l in line.split('\n')]) for line in lines]
        marks = [np.zeros(shape=(5, 5)) for b in boards]
        total = 0
        for ball in balls:
            for idx, board in enumerate(boards):
                loc = np.argwhere(board == ball)
                if loc.size > 0:
                    loc = loc[0]
                    marks[idx][loc[0]][loc[1]] = 1
                    if any(np.all(marks[idx], axis=0)) or any(np.all(marks[idx], axis=1)):
                        for iy, ix in np.ndindex(marks[idx].shape):
                            if marks[idx][iy][ix] == 0:
                                total += int(board[iy][ix])
                        return total * int(ball)


if __name__ == "__main__":
    print(main())
