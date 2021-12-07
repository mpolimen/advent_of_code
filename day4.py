def is_winner(check):
    columns = [True for _ in range(5)]
    for r in range(5):
        good_row = True
        for c in range(5):
            if not check[r][c]:
                good_row = False
                columns[c] = False
        if good_row: return True
    return any(columns)

def score(board, check, draw):
    res = 0
    for r in range(5):
        for c in range(5):
            if not check[r][c]: res += int(board[r][c])
    return res * int(draw)

def winning_score(boards, draws):
    NB = len(boards)
    checks = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]
    for draw in draws:
        for i in range(NB):
            board = boards[i]
            for r in range(5):
                for c in range(5):
                    if board[r][c] == draw:
                        checks[i][r][c] = True
                        if is_winner(checks[i]):
                            return score(board, checks[i], draw)

def last_score(boards, draws):
    NB = len(boards)
    checks = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]
    done = [False for _ in boards]
    for draw in draws:
        for i in range(NB):
            if done[i]: continue
            board = boards[i]
            for r in range(5):
                for c in range(5):
                    if board[r][c] == draw:
                        checks[i][r][c] = True
                        if is_winner(checks[i]):
                            done[i] = True
                            if all(done):
                                return score(board, checks[i], draw)
                        
if __name__ == "__main__":
    draws = input().split(",")
    boards = []
    while(True):
        i = input()
        if i == 'end': break
        elif i == '': continue
        boards.append([i.split()])
        for i in range(4):
            line = input().split()
            print(line)
            boards[-1].append(line)
    # print(winning_score(boards, draws))
    print(last_score(boards, draws))