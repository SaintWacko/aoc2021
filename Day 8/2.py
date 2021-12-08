def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        total = 0
        for line in lines:
            mapping = {}
            signals, output = [x.split() for x in line.split(' | ')]
            signals = sorted(signals, key=len)
            mapping[1] = signals[0]
            mapping[7] = signals[1]
            mapping[4] = signals[2]
            mapping[8] = signals[9]
            l6 = signals[6:9]
            mapping[9] = next(x for x in l6 if set(mapping[4]).issubset(x))
            l6.remove(mapping[9])
            mapping[0] = next(x for x in l6 if set(mapping[7]).issubset(x))
            l6.remove(mapping[0])
            mapping[6] = l6[0]
            l5 = signals[3:6]
            mapping[3] = next(x for x in l5 if set(mapping[7]).issubset(x))
            l5.remove(mapping[3])
            mapping[5] = next(x for x in l5 if set(x + mapping[1]).issubset(mapping[9]))
            l5.remove(mapping[5])
            mapping[2] = l5[0]
            output = [next(key for key, value in mapping.items() if set(value) == set(x)) for x in output]
            total += int(''.join([str(x) for x in output]))
        return total


if __name__ == "__main__":
    print(main())
