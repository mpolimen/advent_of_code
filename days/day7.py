def best_position(crabs, adv=False):
    crabs = sorted(crabs)
    pos, fuel = crabs[0], 0
    for i in range(1, len(crabs)):
        n = crabs[i] - pos
        fuel += n*(n+1)//2 if adv else n
        for j in range(pos+1, crabs[i]+1):
            tmp_fuel = sum([abs(crabs[k] - j)*(abs(crabs[k] - j) + 1)//2 if adv
             else abs(crabs[k] - j) for k in range(i+1)])
            if fuel < tmp_fuel: break
            fuel, pos = tmp_fuel, j
    return fuel, pos

if __name__ == "__main__":
    crabs = input().split(",")
    crabs = [int(c) for c in crabs]
    print(best_position(crabs, adv=True))