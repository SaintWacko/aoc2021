def main():
    with open('input', 'r') as file:
        values = file.read().splitlines()
        values = [x for y in [a.split(' | ')[1].split() for a in values] for x in y]
        return(len([x for x in values if len(x) in [4, 7, 3, 2]]))


if __name__ == "__main__":
    print(main())
