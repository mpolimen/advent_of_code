def is_low_point(h_map, pos, lens):
    r, c = pos
    n, m = lens
    val = h_map[r][c]
    return ((r < 1 or h_map[r-1][c] > val) and (c < 1 or h_map[r][c-1] > val)
     and (r > n-2 or h_map[r+1][c] > val) and (c > m-2 or h_map[r][c+1] > val))

def risk_levels(h_map):
    l_points = set()
    n, m = len(h_map), len(h_map[0])
    for r in range(n):
        for c in range(m):
            if is_low_point(h_map, (r, c), (n, m)): l_points.add((r, c))
    return sum([h_map[r][c]+1 for r, c in l_points])

def largest_basins(h_map):
    size, stack, basins = 0, [], []
    n, m = len(h_map), len(h_map[0])
    for r in range(n):
        for c in range(m):
            if h_map[r][c] == 9: continue
            stack.append((r, c))
            size = 1
            h_map[r][c] = 9
            while(len(stack) != 0):
                r1, c1 = stack.pop()
                if r1 > 0 and h_map[r1-1][c1] != 9:
                    size += 1
                    stack.append((r1-1, c1))
                    h_map[r1-1][c1] = 9
                if c1 > 0 and h_map[r1][c1-1] != 9:
                    size += 1
                    stack.append((r1, c1-1))
                    h_map[r1][c1-1] = 9
                if r1 < (n-1) and h_map[r1+1][c1] != 9:
                    size += 1
                    stack.append((r1+1, c1))
                    h_map[r1+1][c1] = 9
                if c1 < (m-1) and h_map[r1][c1+1] != 9:
                    size += 1
                    stack.append((r1, c1+1))
                    h_map[r1][c1+1] = 9
            basins.append(size)
            size = 0
    prod = 1
    print(basins)
    for n in sorted(basins, reverse=True)[:3]: prod *= n
    return prod 

if __name__ == "__main__":
    h_map = []
    while(True):
        r = input()
        if r == '': break
        h_map.append([int(p) for p in list(r)])
    # print(risk_levels(h_map))
    print(largest_basins(h_map))