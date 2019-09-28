from queue import Queue
from copy import deepcopy
class point():
    def __init__(seft, x, y):
        seft.x = x
        seft.y = y

def bft(i, j, matrix, visited):
    matrix[i][j] = 0
    numOfSlicks = 0
    queueSlick = Queue()
    queueSlick.put(point(i, j))
    while not queueSlick.empty():
        numOfSlicks += 1
        pointer = queueSlick.get()
        x = pointer.x
        y = pointer.y
        visited[x][y] = True
        for i in range(len(dx)):
            r = x + dx[i]
            c = y + dy[i]
            if r in range(row) and c in range(colum):
                if matrix[r][c] == 1:
                    matrix[r][c] = 0
                    queueSlick.put(point(r, c))
    cnt[numOfSlicks] += 1
    
while True:
    row, colum = map(int,input().split())
    if row == 0 and colum == 0:
        break
    matrix = [[] for i in range(row)]
    for i in range(row):
        matrix[i] = list(map(int,input().split()))
    cnt = [0]*(250*250+1)
    rowvisited = [False for i in range(colum)]
    visited = []
    for i in range(row):
        visited.append(deepcopy(rowvisited))
    total = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(row):
        for j in range(colum):
            if visited[i][j] == False and matrix[i][j] == 1:
                visited[i][j] = True
                bft(i, j, matrix, visited)
                total += 1
    print(total) 
    for i in range(len(cnt)):
        if cnt[i] != 0:
            print(i,cnt[i])
    
    