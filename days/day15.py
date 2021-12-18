def enlarge_cave(cave):
    n, m = len(cave), len(cave[0])
    for i in range(1, 5):
        for r in range(n):
            for c in range(m):
                val = cave[r][c]
                cave[r].append(val+i if val+i < 10 else (val+i) % 9)
    m = len(cave[0])
    for i in range(1, 5):
        for r in range(n):
            tmp = []
            for c in range(m):
                val = cave[r][c]
                tmp.append(val+i if val+i < 10 else (val+i) % 9)
            cave.append(tmp)
    return cave

def safest_path(cave, adv=True):
    cave = cave if not adv else enlarge_cave(cave)
    edges = {(0, 0): ((0, 0), 0)}
    curr_vertex, dist, n, m = (0, 0), 0, len(cave), len(cave[0])
    reachable = {}
    def find_reachable(vertex, dist):
        x, y = vertex
        pos = (x-1, y)
        if (x > 0 and pos not in edges and
            (pos not in reachable or reachable[pos][1] > cave[y][x-1] + dist)):
            reachable[pos] = ((x, y), cave[y][x-1] + dist)
        pos = (x+1, y)
        if (x < m-1 and pos not in edges and
            (pos not in reachable or reachable[pos][1] > cave[y][x+1] + dist)):
            reachable[pos] = ((x, y), cave[y][x+1] + dist)
        pos = (x, y-1)
        if (y > 0 and pos not in edges and
            (pos not in reachable or reachable[pos][1] > cave[y-1][x] + dist)):
            reachable[pos] = ((x, y), cave[y-1][x] + dist)
        pos = (x, y+1)
        if (y < n-1 and pos not in edges and
            (pos not in reachable or reachable[pos][1] > cave[y+1][x] + dist)):
            reachable[pos] = ((x, y), cave[y+1][x] + dist)
    while curr_vertex != (m-1, n-1):
        find_reachable(curr_vertex, dist)
        to_vertex = min(reachable, key=lambda k: reachable[k][1])
        edges[to_vertex] = reachable[to_vertex]
        curr_vertex, dist = to_vertex, reachable[to_vertex][1]
        reachable.pop(to_vertex)
    return dist

if __name__ == "__main__":
    cave = []
    while True:
        c = input()
        if c == '': break
        cave.append([int(d) for d in list(c)])
    print(safest_path(cave, adv=True))