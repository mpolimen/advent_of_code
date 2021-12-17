def print_paper(paper):
    for line in paper:
        print("".join(["." if not x else "#" for x in line]))

def fold(paper, instr):
    axis, pos = instr
    n, m, dist = len(paper), len(paper[0]), 1
    folded = []
    if axis == "y":
        while pos+dist < n and pos-dist >= 0:
            folded.insert(0, [])
            for i in range(m):
                folded[0].append(paper[pos+dist][i] or paper[pos-dist][i])
            dist += 1
        if pos-dist >= 0:
            for r in range(pos-dist, -1, -1):
                folded.insert(0, paper[r])
        if pos+dist < n:
            for r in range(pos+dist, n):
                folded.append(paper[r])
    else:
        folded = [[] for _ in range(n)]
        while pos+dist < m and pos-dist >= 0:
            for i in range(n):
                folded[i].insert(0, paper[i][pos+dist] or paper[i][pos-dist])
            dist += 1
        if pos-dist >= 0:
            for i in range(n):
                tmp = [e for e in paper[i][:pos-dist+1]]
                tmp.extend(folded[i])
                folded[i] = tmp
        if pos+dist < m:
            for i in range(n):
                folded[i].extend([e for e in paper[i][pos+dist:]])
    return folded

def draw_dots(dots):
    x_max, y_max = 0, 0
    for dot in dots: x_max, y_max = max(dot[0], x_max), max(dot[1], y_max)
    paper = [[False for _ in range(x_max+1)] for _ in range(y_max+1)]
    for dot in dots: paper[dot[1]][dot[0]] = True
    return paper

if __name__ == "__main__":
    dots = []
    folds = []
    while True:
        i = input()
        if i == 'end': break
        if i == "": continue
        if "fold along" in i:
            folds.append(i[11:].split("="))
            folds[-1][1] = int(folds[-1][1])
        else:
            dots.append([int(p) for p in i.split(",")])
    paper = draw_dots(dots)
    folded = fold(paper, folds[0])
    print("Part 1:", sum(r.count(True) for r in folded))
    for instr in folds[1:]: folded = fold(folded, instr)
    print("Part 2:")
    print_paper(folded)