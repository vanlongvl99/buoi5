from queue import Queue
class point():
    def __init__(seft,id,preCat):
        seft.id = id
        seft.preCat = preCat


def solve1(n, m, visited, graph):
    path = [-1]*(n+1)
    queueQ = Queue()
    queueQ.put(1)
    while not queueQ.empty():
        u = queueQ.get()
        for i in graph[u]:
            if visited[i] == False:
                visited[i] = True
                queueQ.put(i)
                path[i] = u
    total = 0
    for i in range(2, n+1):
        if len(graph[i]) == 1: # các leaf vertices thì chỉ liên kết với đúng 1 đỉnh khác
            total += 1
            last = i
            cnt = 0
            while last != -1:  # xét ngược từ vị trí i về root 
                if status[last - 1] == 1:   # check trên những đỉnh về root có gặp cat hay k?
                    cnt += 1
                    if cnt > m:         # số mèo quá qui định
                        total = total - 1
                        break
                    last = path[last] 
                    continue
                cnt = 0
                last = path[last]
    return total

def solve2(n, m, visited, graph):
    queuePoints = Queue()
    total = 0
    queuePoints.put(point(1,status[0]))
    while not queuePoints.empty():
        pointer = queuePoints.get()
        for i in graph[pointer.id]:
            if len(graph[i]) == 1 and visited[i] == False:
                if status[i - 1] + pointer.preCat <= m:
                    total += 1
            else:
                if visited[i] == False:
                    if status[i - 1] == 0:
                        queuePoints.put(point(i, 0))
                    elif pointer.preCat < m:
                        queuePoints.put(point(i, pointer.preCat + 1))
                    visited[i] = True
    return total    

if __name__ == "__main__":    
    n, m = map(int,input().split())
    status = list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for i in range(n-1):
        first, second = map(int,input().split())
        graph[first].append(second)
        graph[second].append(first)
    visited = [False for i in range(n + 1)]
    visited[1] = True
    total = solve2(n, m, visited, graph)
    print(total)  


