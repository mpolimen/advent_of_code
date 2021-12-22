from ast import literal_eval as leval
import math
import copy

def magnitude(snum):
    if type(snum) is int: return snum
    return 3*magnitude(snum[0]) + 2*magnitude(snum[1])

def explode(snum, layer=1, right=None):
    res, exploded, left = [], False, None
    def left_add(left):
        tmp = res
        while type(tmp[-1]) is not int: tmp = tmp[-1]
        tmp[-1] += left
    for i in range(len(snum)):
        def right_add(right):
            if type(snum[i+1]) is int:
                snum[i+1] += right
                return
            tmp = snum[i+1]
            while type(tmp[0]) is not int: tmp = tmp[0]
            tmp[0] += right
        sn = snum[i]
        if type(sn) is list:
            if layer == 4:
                exploded = True
                x, y = sn[0], sn[1]
                if len(res) > 0: left_add(x)
                else: left = x
                if i < len(snum)-1: right_add(y)
                else: right = y
                res.append(0)
                res.extend([e for e in snum[i+1:]])
                break
            else:
                tmp, exp, left, right = explode(sn, layer+1, right)
                if exp:
                    if left and len(res) > 0:
                        left_add(left)
                        left = None
                    res.append(tmp)
                    if right and i < len(snum)-1:
                        right_add(right)
                        right = None
                    exploded = True
                    res.extend([e for e in snum[i+1:]])
                    break
                res.append(tmp)
        else: res.append(sn)
    return res, exploded, left, right

def split(snum):
    res, broken = [], False
    for i in range(len(snum)):
        sn = snum[i]
        if type(sn) is list:
            elem, broken = split(sn)
            res.append(elem)
            if broken:
                res.extend([e for e in snum[i+1:]])
                break
        elif sn >= 10:
            res.append([sn//2, math.ceil(sn/2)])
            broken = True
            res.extend([e for e in snum[i+1:]])
            break
        else:
            res.append(sn)
    return res, broken

def add(snum1, snum2):
    snum = [snum1, snum2]
    while True:
        # Check for explodes, continue if it happens
        snum, exploded, _, _ = explode(snum)
        if exploded: continue
        # Check for splits, coninue if it happens
        snum, broken = split(snum)
        if broken: continue
        break
    return snum

if __name__ == "__main__":
    snums = []
    while True:
        snum = input()
        if snum == '': break
        snums.append(leval(snum))
    # Part 1
    stotal = copy.deepcopy(snums[0])
    for i in range(1, len(snums)): stotal = add(stotal, copy.deepcopy(snums[i]))
    print(magnitude(stotal))
    # Part 2
    high = 0
    for i in range(len(snums)):
        for j in range(i+1, len(snums)):
            print("(i, j):", i, j)
            high = max(high,
             magnitude(add(copy.deepcopy(snums[i]), copy.deepcopy(snums[j]))))
            high = max(high,
             magnitude(add(copy.deepcopy(snums[j]), copy.deepcopy(snums[i]))))
    print("Highest Magnitude:", high)

