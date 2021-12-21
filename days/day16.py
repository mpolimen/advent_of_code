def version_sum(packet):
    count = int(packet[:3], base=2)
    literal = int(packet[3:6], base=2) == 4
    if not literal:
        I = int(packet[6])
        L = int(packet[7:18], base=2) if I else int(packet[7:22], base=2)
        packet = packet[18:] if I else packet[22:]
        i, b = 0, 0
        while (I and i < L) or (not I and b < L):
            i, n = i+1, len(packet)
            c, packet = version_sum(packet)
            count, b = count+c, b+(n-len(packet))
    else:
        packet, stay = packet[6:], True
        while stay:
            stay, packet = int(packet[0]), packet[5:]
    return count, packet

import math
def operate(id, nums):
    if id == 0: return sum(nums)
    if id == 1: return math.prod(nums)
    if id == 2: return min(nums)
    if id == 3: return max(nums)
    if id == 5: return 1 if nums[0] > nums[1] else 0
    if id == 6: return 1 if nums[0] < nums[1] else 0
    if id == 7: return 1 if nums[0] == nums[1] else 0

def perform_packet(packet):
    id = int(packet[3:6], base=2)
    if id == 4: # a literal
        packet, stay, num = packet[6:], True, []
        while stay:
            num.append(packet[1:5])
            stay, packet  = int(packet[0]), packet[5:]
        num = int(''.join(num), base=2)
    else: # an operator
        I = int(packet[6])
        L = int(packet[7:18], base=2) if I else int(packet[7:22], base=2)
        packet = packet[18:] if I else packet[22:]
        i, b, num = 0, 0, []
        while (I and i < L) or (not I and b < L):
            i, n = i+1, len(packet)
            v, packet = perform_packet(packet)
            b = b+(n-len(packet))
            num.append(v)
        num = operate(id, num)
    return num, packet

def hex_to_binary(hexa):
    bin_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000",
        "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101",
        "E": "1110", "F": "1111"}
    return ''.join([bin_map[d] for d in hexa])

if __name__ == "__main__":
    packet = hex_to_binary(input())
    # print(version_sum(packet)[0])
    print(perform_packet(packet)[0])