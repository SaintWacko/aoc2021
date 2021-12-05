from itertools import groupby
def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        lines = sorted([line.split(' ') for line in lines])
        dir = dict([(key, sum([int(c[1]) for c in group])) for key, group in groupby(lines, lambda x: x[0])])
        return dir['forward'] * (dir['down'] - dir['up'])


if __name__ == "__main__":
    print(main())
