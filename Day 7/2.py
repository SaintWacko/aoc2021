import sys


def main():
    with open('input', 'r') as file:
        fuel = sys.maxsize
        values = [int(n) for n in file.read().split(',')]
        for n in range(min(values), max(values)):
            f = sum([abs(val - n) * (abs(val - n) + 1) / 2 for val in values])
            if f < fuel:
                fuel = f
        return fuel


if __name__ == "__main__":
    print(main())
