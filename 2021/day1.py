def count_increases(depths):
    c = 0
    prev = float('inf')
    for d in depths:
        c = c if d <= prev else c+1
        prev = d
    return c

def count_increase_groups(depths):
    c = 0
    prev = float('inf')
    for i in range(2, len(depths)):
        d = sum(depths[i-2:i+1])
        c = c if d <= prev else c+1
        prev = d
    return c

if __name__ == "__main__":
    depths = []
    while(True):
        d = input()
        if d == '': break
        depths.append(int(d))
    # print(count_increases(depths))
    print(count_increase_groups(depths))