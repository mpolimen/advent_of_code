from collections import Counter
from functools import lru_cache

def frequency_range(counts):
    sorted_freq = counts.most_common()
    return sorted_freq[0][1] - sorted_freq[-1][1]

def polymer_range(polymer, rules, steps):
    @lru_cache(maxsize=None)
    def insert_step(pair, steps):
        if steps == 0 or pair not in rules: return Counter()
        mid = rules[pair]
        l, r = pair[0]+mid, mid+pair[1]
        counts = Counter(mid)
        counts.update(insert_step(l, steps-1))
        counts.update(insert_step(r, steps-1))
        return counts
    res = Counter(polymer)
    for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            res.update(insert_step(pair, steps))
    return res

if __name__ == "__main__":
    template = input()
    rules = {}
    input()
    while True:
        r = input()
        if r == '': break
        r = r.split(" -> ")
        rules[r[0]] = r[1]
    print(frequency_range(polymer_range(template, rules, steps=40)))
