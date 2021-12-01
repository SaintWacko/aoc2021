
def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        lines = [int(x) for x in lines]
        count = 0
        num1 = sum(lines[:2])
        num2 = 0
        idx = 0
        while (idx < len(lines) - 3):
            num2 += lines[idx + 3]
            num2 -= lines[idx]
            if num2 > num1:
                count += 1
            num1 = num2
            idx += 1
        return count


if __name__ == "__main__":
    print(main())


# 1 2 3 4 5 6 7 8
# 1+2+3
#   2+3+4