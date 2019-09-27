from queue import Queue
n, m = map(int,input().split())
status = list(map(int,input().split()))
path = [-1]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(n-1):
    first, second = map(int,input().split())
    # path[max(first, second)] = min(first, second) 
    graph[first].append(second)
    graph[second].append(first)
visited = [False for i in range(n + 1)]
visited[1] = True
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
print(total)  


