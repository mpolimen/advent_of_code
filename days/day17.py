def high_y(ranges):
    n = -ranges[1][0] - 1
    return n*(n+1) // 2

def lands(vx, vy, gx, gy):
    x, y, tmpx, tmpy = 0, 0, vx, vy
    while (not (gx[0] <= x <= gx[1] and gy[0] <= y <= gy[1])):
        if x > gx[1] or y < gy[0]: return False
        x, y = x+tmpx, y+tmpy
        tmpx, tmpy = tmpx-1 if tmpx > 0 else 0, tmpy-1
    return True

def num_velos(ranges):
    gx, gy = ranges[0], ranges[1]
    count = 0
    x_velo_min, pos, n = 0, 0, -gy[0] - 1
    while pos < gx[0]:
        x_velo_min += 1
        pos += x_velo_min
    for vx in range(x_velo_min, gx[1]+1):
        for vy in range(gy[0], n+1):
            count += 1 if lands(vx, vy, gx, gy) else 0
    return count

if __name__ == "__main__":
    ranges = [[int(d) for d in r[2:].split("..")] 
                for r in input()[13:].split(", ")]
    # print(high_y(ranges))
    print(num_velos(ranges))