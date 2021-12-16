def flash(octopi, pos, flashing):
    num = 0
    stack = [pos]
    n, m = len(octopi), len(octopi[0])
    while len(stack) > 0:
        num += 1
        r, c = stack.pop()
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i < 0 or j < 0 or i >= n or j >= m: continue
                if octopi[i][j] == 9:
                    octopi[i][j] = 0
                    flashing.add((i, j))
                    stack.append((i, j))
                elif (i, j) not in flashing: octopi[i][j] += 1
    return num

def num_flashes(octopi, days=100):
    num = 0
    n, m = len(octopi), len(octopi[0])
    for _ in range(days):
        flashing = set()
        for r in range(n):
            for c in range(m):
                if octopi[r][c] == 9:
                    octopi[r][c] = 0
                    flashing.add((r, c))
                    num += flash(octopi, (r, c), flashing)
                elif (r, c) not in flashing: octopi[r][c] += 1
    return num

def all_flash(octopi):
    day = 0
    n, m = len(octopi), len(octopi[0])
    while True:
        day += 1
        num, flashing = 0, set()
        for r in range(n):
            for c in range(m):
                if octopi[r][c] == 9:
                    octopi[r][c] = 0
                    flashing.add((r, c))
                    num += flash(octopi, (r, c), flashing)
                elif (r, c) not in flashing: octopi[r][c] += 1
        if num == n*m: return day

if __name__ == "__main__":
    octopi = []
    while(True):
        line = input()
        if line == '': break
        octopi.append([int(o) for o in list(line)])
    # print(num_flashes(octopi))
    print(all_flash(octopi))