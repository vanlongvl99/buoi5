from copy import deepcopy
from queue import Queue
class point():
    def __init__(seft,x,y):
        seft.x = x
        seft.y = y
t = int(input())
for index in range(t):
    row, line = map(int,input().split())
    rowOfMatrix = [-2]*line
    matrix = []
    entryAndExit = []
    for i in range(row):
        matrix.append(deepcopy(rowOfMatrix))
    for x in range(row):
        characters = input()
        for y in range(line):
            if characters[y] == ".":
                if x == 0 or x == row - 1 or y == 0 or y == line -1:
                    # print(x,y)
                    entryAndExit.append(point(x, y))
                matrix[x][y] = -1
    if len(entryAndExit) != 2:
        print("invalid")
        continue
    # for i in range(len(matrix)):
        # print(matrix[i])
    curQueue = Queue()
    matrix[entryAndExit[0].x][entryAndExit[0].y] = 1
    curQueue.put(entryAndExit[0])
    while not curQueue.empty():
        pointer = curQueue.get()
        x = pointer.x
        y = pointer.y
        if x + 1 > -1 and x + 1 < row and matrix[x + 1][y] == -1:
            matrix[x + 1][y] = 1
            curQueue.put(point(x + 1, y))
        if x - 1 > -1 and x - 1 < row and matrix[x - 1][y] == -1:
            matrix[x - 1][y] = 1
            curQueue.put(point(x - 1,y))
        if y + 1 > -1 and y + 1 < line and matrix[x][y + 1] == -1:
            matrix[x][y + 1] = 1
            curQueue.put(point(x, y + 1))
        if y - 1 > -1 and y - 1 < line and matrix[x][y - 1] == -1:
            matrix[x][y - 1] = 1
            curQueue.put(point(x, y - 1))
    if matrix[entryAndExit[1].x][entryAndExit[1].y] == 1:
        print("valid")
    else:
        print("invalid")
