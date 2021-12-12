paths = []


def main():
    connections = {}
    with open('input', 'r') as file:
        lines = [x.split('-') for x in file.read().splitlines()]
        for line in lines:
            if line[0] in connections:
                connections[line[0]].append(line[1])
            else:
                connections[line[0]] = [line[1]]
            if line[1] in connections:
                connections[line[1]].append(line[0])
            else:
                connections[line[1]] = [line[0]]
        path('start', connections)
        return len(paths)


def path(loc, connections, trail=[], double=True):
    global paths
    if loc == 'end':
        paths.append(trail + [loc])
        return
    if loc.islower() and loc in trail:
        if double and loc != 'start':
            for conn in connections[loc]:
                path(conn, connections, trail[:] + [loc], False)
        return
    for conn in connections[loc]:
        path(conn, connections, trail[:] + [loc], double)


if __name__ == "__main__":
    print(main())
