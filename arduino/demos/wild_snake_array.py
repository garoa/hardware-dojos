moves = {
    0:  [1],
    1:  [13, 2],
    2:  [3],
    3:  [4],
    4:  [6, 5],
    5:  [0],
    6:  [2,8],
    7:  [12],
    8:  [7],
    9:  [13, 8],
    10: [9],
    11: [10],
    12: [6, 11],
    13: [5, 11]
}

for i, move in sorted(moves.items()):
    cmove = [len(move)] + move
    if len(cmove) < 3:
        cmove = cmove + [-1]
    print repr(cmove).replace('[', '{').replace(']', '}')+',', '//', i
