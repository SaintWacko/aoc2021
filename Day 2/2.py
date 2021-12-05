
def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        lines = [line.split(' ') for line in lines]
        lines = [[line[0], int(line[1])] for line in lines]
        aim = 0
        x = 0
        y = 0
        for line in lines:
            if line[0] == 'down':
                aim += line[1]
            elif line[0] == 'up':
                aim -= line[1]
            else:
                x += line[1]
                y += line[1] * aim
        return x * y


if __name__ == "__main__":
    print(main())
