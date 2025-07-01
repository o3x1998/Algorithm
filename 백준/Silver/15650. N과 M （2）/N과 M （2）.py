import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def DFS(s, arr):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(s, N):
        DFS(i+1, arr + [i+1])
         
DFS(0, [])    