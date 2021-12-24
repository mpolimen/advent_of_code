def practice_game(p1, p2):
    p1, p2 = p1-1, p2-1
    rolls, score1, score2, dice = 0, 0, 0, 1
    def turn(rolls, score, dice, pos):
        rolls, move = rolls+3, 0
        for _ in range(3): move, dice = move+dice, dice+1 if dice<100 else 1
        pos = (pos+move)%10
        score += pos+1
        return rolls, score, dice, pos
    while score2 < 1000:
        rolls, score1, dice, p1 = turn(rolls, score1, dice, p1)
        if score1 >= 1000: break
        rolls, score2, dice, p2 = turn(rolls, score2, dice, p2)
    return rolls, score1, score2

from functools import lru_cache
@lru_cache(maxsize=None)
def wins(p1, p2, t1=21, t2=21):
    if t2 <= 0: return (0, 1)
    w1, w2 = 0, 0
    roll_freq = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
    for (r, f) in roll_freq:
        c2, c1 = wins(p2, (p1+r)%10, t2, t1 - 1 - (p1+r)%10)
        w1, w2 = w1 + f * c1, w2 + f * c2
    return w1, w2

if __name__ == "__main__":
    p1 = input()
    p2 = input()
    p1, p2 = int(p1[p1.find(": ")+2:]), int(p2[p2.find(": ")+2:])
    # turns, score1, score2 = practice_game(p1, p2)
    # print(turns*min(score1, score2))
    print(max(wins(p1-1, p2-1)))