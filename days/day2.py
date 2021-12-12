def positions(instructions):
    x, y = 0, 0
    for instr, dist in instructions:
        if instr == "forward": x += int(dist)
        elif instr == "up": y -= int(dist)
        elif instr == "down": y += int(dist)
    return (x, y)

def positions_with_aim(instructions):
    x, y, aim = 0, 0, 0
    for instr, dist in instructions:
        dist = int(dist)
        if instr == "forward":
            x += dist
            y += (aim * dist)
        elif instr == "up": aim -= dist
        elif instr == "down": aim += dist
    return (x, y)

if __name__ == "__main__":
    instructions = []
    while(True):
        i = input()
        if i == '': break
        instructions.append(i.split(" "))
    # res = positions(instructions)
    res = positions_with_aim(instructions)
    print(res[0]*res[1])