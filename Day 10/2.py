from statistics import median


def main():
    openings = ['<', '{', '[', '(']
    closings = ['>', '}', ']', ')']
    scoring = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    with open('input', 'r') as file:
        lines = [list(x) for x in file.read().splitlines()]
        for line in lines:
            stack = []
            clean = True
            total = 0
            for char in line:
                if char in openings:
                    stack.append(char)
                if char in closings:
                    if char == closings[openings.index(stack[-1])]:
                        stack.pop()
                    else:
                        clean = False
                        break
            if clean:
                for char in stack[::-1]:
                    total = total * 5 + scoring[char]
                scores.append(total)
    return(median(scores))


if __name__ == "__main__":
    print(main())
