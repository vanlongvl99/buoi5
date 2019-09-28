from queue import  Queue

def bfs(startKey, trueKey, listNums):
    visited = [False for i in range(100001)]
    dist = [-1]*100001
    queueKeys = Queue()
    visited[startKey] = True
    dist[startKey] = 0
    queueKeys.put(startKey)
    while not queueKeys.empty():
        u = queueKeys.get()
        for v in listNums:
            k = u*v%100000
            if k == trueKey:
                return dist[u] + 1
            if visited[k] == False:
                dist[k] = dist[u] + 1
                visited[k] = True
                queueKeys.put(k)
    return -1
if __name__ == "__main__":
    startKey, trueKey = map(int,input().split())
    amountNums = int(input())
    listNums = list(map(int, input().split()))
    print(bfs(startKey, trueKey, listNums))