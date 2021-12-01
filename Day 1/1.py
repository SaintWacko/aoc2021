def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        lines = [int(x) for x in lines]
        count = 0
        num1 = lines[0]
        num2 = 0
        for line in lines[1:]:
            num2 = line
            if num2 > num1:
                count += 1
            num1 = line
        return count

if __name__ == "__main__":
    print(main())
