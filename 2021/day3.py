def power_consumption(bits):
    N = len(bits[0])
    res = [0 for _ in range(N)]
    for num in bits:
        for i in range(N):
            res[i] += 1 if num[i] == "1" else -1
    res = ["1" if res[i] > 0 else "0" for i in range(N)]
    gamma = int("".join(res), 2)
    return gamma * (gamma ^ int("1"*N, 2))

def life_support_rating(bits, oxygen):
    N, curr, balance, new_bits = len(bits[0]), 0, 0, []
    while curr < N:
        for num in bits: balance += 1 if num[curr] == "1" else -1
        if oxygen: criteria = "1" if balance >= 0 else "0"
        else: criteria = "0" if balance >= 0 else "1"
        for num in bits:
            if num[curr] == criteria: new_bits.append(num)
        if len(new_bits) == 1: return int(new_bits[0], 2)
        bits, balance, curr, new_bits = new_bits, 0, curr+1, []

if __name__ == "__main__":
    bits = []
    while(True):
        b = input()
        if b == '': break
        bits.append(b)
    # print(power_consumption(bits))
    print(life_support_rating(bits, True) * life_support_rating(bits, False))