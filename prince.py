from copy import deepcopy
from queue import Queue

class point():
    def __init__(seft,x,y):
        seft.x = x
        seft.y = y

t = int(input())
for index in range(t):
    line, row = map(int,input().split())
    rowOfMatrix = [-2]*(line + 1)
    matrix = []
    for i in range(row + 1):
        matrix.append(deepcopy(rowOfMatrix))
    curQueue = Queue()
    for x in range(row):
        characters = input()
        for y in range(line):
            if characters[y] == ".":
                matrix[x][y] = -1
            if characters[y] == "@":
                matrix[x][y] = 1
                curQueue.put(point(x,y))
    total = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while not curQueue.empty():
        pointTer = curQueue.get()
        x = pointTer.x
        y = pointTer.y
        for i in range(len(dx)):
            if matrix[x + dx[i]][y + dy[i]] == -1:
                total += 1
                matrix[x + dx[i]][y + dy[i]] = 1
                curQueue.put(point(x + dx[i], y + dy[i]))
        
        # if x + 1 > -1 and x + 1 < row and matrix[x + 1][y] == -1:
            # total += 1
            # matrix[x + 1][y] = 1
            # curQueue.put(point(x + 1, y))
        # if x - 1 > -1 and x - 1 < row and matrix[x - 1][y] == -1:
            # total += 1
            # matrix[x - 1][y] = 1
            # curQueue.put(point(x - 1,y))
        # if y + 1 > -1 and y + 1 < line and matrix[x][y + 1] == -1:
            # total += 1
            # matrix[x][y + 1] = 1
            # curQueue.put(point(x, y + 1))
        # if y - 1 > -1 and y - 1 < line and matrix[x][y - 1] == -1:
            # total += 1
            # matrix[x][y - 1] = 1
            # curQueue.put(point(x, y - 1))
    print("Case "+str(index + 1)+": "+str(total))