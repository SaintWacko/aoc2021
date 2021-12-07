import sys


def main():
    days = int(sys.argv[1])
    with open('input', 'r') as file:
        values = file.read().split(',')
        keys = set(values)
        fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, }
        for key in keys:
            fish[int(key)] = values.count(key)
        while days > 0:
            days -= 1
            new_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, }
            new_fish[8] = fish[0]
            new_fish[7] = fish[8]
            new_fish[6] = fish[7] + fish[0]
            for x in range(1, 7):
                new_fish[x - 1] = fish[x]
            fish = new_fish
        return(sum(fish.values()))


if __name__ == "__main__":
    print(main())
