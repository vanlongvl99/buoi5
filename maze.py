from copy import deepcopy
from queue import Queue

class point():
    def __init__(seft,x,y):
        seft.x = x
        seft.y = y

def bfs(entry, f, matrix):
    curQueue = Queue()
    rowVisited = [False for i in range(len(matrix[0]))]
    visited = []
    for i in range(len(matrix)):
        visited.append(deepcopy(rowVisited))
    matrix[entry.x][entry.y] = 1
    visited[entry.x][entry.y] = True
    curQueue.put(entry)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while not curQueue.empty():  # số lượng đỉnh tối đa
        pointer = curQueue.get()
        x = pointer.x
        y = pointer.y
        for i in range(len(dx)):
            if matrix[x + dx[i]][y + dy[i]] == -1 and not visited[x + dx[i]][y + dy[i]]:
                matrix[x + dx[i]][y + dy[i]] = 1
                curQueue.put(point(x + dx[i], y + dy[i]))
    return matrix[f.x][f.y]
    
if __name__ == "__main__":
    testCase = int(input())
    for index in range(testCase):
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
                        entryAndExit.append(point(x, y))
                    matrix[x][y] = -1
        if len(entryAndExit) != 2:
            print("invalid")
            continue
        print(bfs(entryAndExit[0], entryAndExit[1], matrix))
