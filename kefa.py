from queue import Queue
n, m = map(int,input().split())
status = list(map(int,input().split()))
path = [-1]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(n-1):
    first, second = map(int,input().split())
    path[max(first, second)] = min(first, second) 
    graph[first].append(second)
    graph[second].append(first)
total = 0
for i in range(2,n+1):
    if len(graph[i]) == 1:
        total += 1
        last = i
        cnt = 0
        while last != -1:
            if status[last - 1] == 1:
                cnt += 1
                if cnt > m:
                    total = total - 1
                    break
                last = path[last] 
                continue
            cnt = 0
            last = path[last]
print(total)  


