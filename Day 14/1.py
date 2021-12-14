import sys


def main():
    steps = int(sys.argv[1])
    with open('input', 'r') as file:
        template, rules = [line.splitlines() for line in file.read().split('\n\n')]
        rules = {k: v for k, v in [rule.split(' -> ') for rule in rules]}
        polymers = set(list(template[0]) + list(rules.values()))
        for _ in range(steps + 1):
            output = ''
            for i in range(len(template) - 1):
                output += template[i] + rules[template[i] + template[i + 1]]
            template = output + template[-1]
        counts = sorted([template.count(p) for p in polymers])
        return(counts[-1] - counts[0])


if __name__ == "__main__":
    print(main())
