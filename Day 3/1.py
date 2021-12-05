def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        cols = list(zip(*lines[::-1]))
        gamma = ''
        for col in cols:
            if col.count('1') > len(col)/2:
                gamma += '1'
            else:
                gamma += '0'
        epsilon = ''.join('1' if n == '0' else '0' for n in gamma)
        return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    print(main())
