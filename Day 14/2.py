import sys


def main():
    steps = int(sys.argv[1])
    with open('input', 'r') as file:
        template, rules = file.read().split('\n\n')
        rules = {k: v for k, v in [rule.split(' -> ') for rule in rules.splitlines()]}
        polymers = set(list(template[0]) + list(rules.values()))
        pairs = {p: 0 for p in list(rules.keys())}
        counts = {p: template.count(p) for p in polymers}
        for i in range(len(template) - 1):
            pairs[template[i:i + 2]] += 1
        for _ in range(steps):
            output = {p: 0 for p in list(rules.keys())}
            for k, v in pairs.items():
                output[k[0] + rules[k]] += v
                output[rules[k] + k[1]] += v
                counts[rules[k]] += v
            pairs = output
        print(counts)
        counts = sorted(counts.values())
        return (counts[-1] - counts[0])


if __name__ == "__main__":
    print(main())
