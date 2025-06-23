num = int(input())
arr = [0] * num
visited = [False] * num

def DFS(cnt):
    if cnt == num:
        print(*arr)
        return
    for i in range(num):
        if not visited[i]:
            arr[cnt] = (i+1)
            visited[i] = True
            DFS(cnt+1)
            visited[i] = False
        
DFS(0)