from queue import Queue
def Bfs(m, n):
    visited = [False for i in range(n + 1)]
    path = [-1 for i in range(n+1)]
    graph = [[] for i in range(n+1)]
    for i in range(m):
        node1, node2 = map(int,input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    s = int(input())
    visited[s] = True
    queueQ = Queue()
    queueQ.put(s)
    while not queueQ.empty():
        u = queueQ.get()
        for i in graph[u]:
            if visited[i] == False:
                visited[i] = True
                queueQ.put(i)
                path[i] = u
    return s, path

if __name__ == "__main__":        
    q = int(input())
    output = []
    for i in range(q):
        n, m = map(int,input().split())
        out = [-1 for i in range(n+1)]
        s, path = Bfs(m, n)
        out[s] = 0
        for i in range(1,n+1):
            if path[i] != -1:
                k = i
                cnt = 1
                while path[k] != s:
                    cnt += 1
                    k = path[k]
                out[i] = cnt*6
        output.append(out)
    for i in range(q):
        for j in range(1,len(output[i])):
            if j == len(output[i]) -1 and output[i][j] != 0:
                print(output[i][j])
            elif output[i][j] != 0:
                print(output[i][j],end=" ") 


