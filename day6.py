def lanternfish(fish, days):
    fish_map = {i:0 for i in range(9)}
    for f in fish: fish_map[f] += 1
    for _ in range(days):
        spawns = fish_map[0]
        for i in range(8): fish_map[i] = fish_map[i+1]
        fish_map[6] += spawns
        fish_map[8] = spawns
    return sum([fish_map[i] for i in fish_map])

if __name__ == "__main__":
    fish = input().split(",")
    fish = [int(a) for a in fish]
    print(lanternfish(fish, days=256))