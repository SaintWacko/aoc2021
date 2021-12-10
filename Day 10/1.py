def main():
    openings = ['<', '{', '[', '(']
    closings = ['>', '}', ']', ')']
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    errors = []
    with open('input', 'r') as file:
        lines = [list(x) for x in file.read().splitlines()]
        for line in lines:
            for char in line:
                if char in openings:
                    stack.append(char)
                if char in closings:
                    if char == closings[openings.index(stack[-1])]:
                        stack.pop()
                    else:
                        errors.append(char)
                        break
    return sum([scores[c] for c in errors])


if __name__ == "__main__":
    print(main())
