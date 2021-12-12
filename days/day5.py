def find_marks(vent):
    start = (int(vent[0][0]), int(vent[0][1]))
    end = (int(vent[1][0]), int(vent[1][1]))
    if start[0] == end[0]:
        min_y = min(start[1], end[1])
        max_y = max(start[1], end[1])
        return [(start[0], i) for i in range(min_y, max_y+1)]
    elif start[1] == end[1]:
        min_x = min(start[0], end[0])
        max_x = max(start[0], end[0])
        return [(i, start[1]) for i in range(min_x, max_x+1)]
    x, y = start
    res = []
    while(True):
        res.append((x, y))
        x = x+1 if start[0] < end[0] else x-1
        y = y+1 if start[1] < end[1] else y-1
        if x == end[0]:
            res.append((x, y))
            break
    return res

def diag(v):
    start = (int(v[0][0]), int(v[0][1]))
    end = (int(v[1][0]), int(v[1][1]))
    return abs(start[0]-end[0]) == abs(start[1]-end[1])

def num_overlaps(vents, adv=False):
    res = 0
    marks = [[0 for _ in range(1000)] for _ in range(1000)]
    for v in vents:
        if (v[0][0] != v[1][0] and v[0][1] != v[1][1] and
         (not adv or not diag(v))):
            continue
        for m in find_marks(v):
            if marks[m[0]][m[1]] == 1: res += 1
            marks[m[0]][m[1]] += 1
    return res

if __name__ == "__main__":
    vents = []
    while(True):
        i = input()
        if i == '': break
        coords = i.split(" -> ")
        vents.append((coords[0].split(","), coords[1].split(",")))
    print(num_overlaps(vents, True))