def corrupt_score(line):
    stack = []
    sym_map = {"(": ")", "[": "]", "<": ">", "{": "}"}
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for sym in line:
        if sym in sym_map: stack.append(sym)
        elif sym_map[stack.pop()] != sym: return score_map[sym]
    return 0

def syntax_score(lines):
    score = 0
    for line in lines:
        score += corrupt_score(line)
    return score

def complete_line(line):
    stack = []
    sym_map = {"(": ")", "[": "]", "<": ">", "{": "}"}
    for sym in line:
        if sym in sym_map: stack.append(sym)
        elif sym_map[stack.pop()] != sym: return ""
    return "".join([sym_map[s] for s in stack[::-1]])

def middle_score(lines):
    scores = []
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    for line in lines:
        completion = complete_line(line)
        if completion == "": continue
        score = 0
        for sym in completion: score = (score*5) + score_map[sym]
        scores.append(score)
    return sorted(scores)[len(scores)//2]

if __name__ == "__main__":
    lines = []
    while(True):
        line = input()
        if line == '': break
        lines.append(line)
    # print(syntax_score(lines))
    print(middle_score(lines))