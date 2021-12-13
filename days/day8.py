def unique_segments(readings):
    guide = set([2, 4, 3, 7])
    c = 0
    for r in readings:
        for o in r[1]:
            if len(o) in guide: c += 1
    return c

def letter_map(left):
    let_map = {}
        # Find N=2, for cf // _
    for n in left:
        if len(n) == 2: let_map['c'], let_map['f'] = n[0], n[1]
    # Find N=3, for a (the other besides cf) // a
    for n in left:
        if len(n) == 3:
            for c in n:
                if c != let_map['c'] and c != let_map['f']:
                    let_map['a'] = c
    # Find N=4, for bd // a
    for n in left:
        if len(n) == 4:
            flag = False
            for c in n:
                if c != let_map['c'] and c != let_map['f']:
                    if not flag: let_map['b'] = c
                    else: let_map['d'] = c
                    flag = True
    # Find N=6 w/o c, for f (assign c to other) // acf
    for n in left:
        if (len(n) == 6 and 
            not (let_map['c'] in n and let_map['f'] in n)):
            if let_map['c'] in n:
                tmp = let_map['c']
                let_map['c'], let_map['f'] = let_map['f'], tmp 
    # Find N=6 w/ abcdf, for g (only missing letter) // acfg
    seen = set([let_map[k] for k in let_map])
    for n in left:
        if (len(n) == 6 and seen <= set(n)):
            for c in n:
                if c not in seen: let_map['g'] = c
    # Find N=5 w/ acfg, for d (assign b to other) // abcdfg
    check = set([let_map['a'], let_map['c'], let_map['f'], let_map['g']])
    for n in left:
        if (len(n) == 5 and check <= set(n)):
            for c in n:
                if c not in check and c != let_map['d']:
                    tmp = let_map['b']
                    let_map['b'], let_map['d'] = let_map['d'], tmp
    # Give e the remaining letter // abcdefg
    seen = set([let_map[k] for k in let_map])
    for c in "abcdefg":
        if c not in seen:
            let_map['e'] = c
    return let_map

def decode(input, let_map):
    print(input)
    num_map = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
        "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
    rev_map = {let_map[k]:k for k in let_map}
    letters = []
    for c in input:
        letters.append(rev_map[c])
    letters = sorted(letters)
    return num_map[''.join(letters)]

def sum_readings(readings):
    c = 0
    for r in readings:
        left, right = r
        let_map = letter_map(left)
        num = 0
        for n in right:
            num = num*10 + decode(n, let_map)
        c += num
    return c

if __name__ == "__main__":
    readings = []
    while(True):
        r = input()
        if r == '': break
        delim = r.split(" | ")
        readings.append((delim[0].split(" "), delim[1].split(" ")))
    # print(unique_segments(readings))
    print(sum_readings(readings))