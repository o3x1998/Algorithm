def find(arr, x):
    if arr[x] != x: return find(arr, arr[x])
    return x

def change(arr, x, p):
    for i in range(len(arr)):
        if arr[i] == x: arr[i] = p

def union(arr, a, b):
    a, b = find(arr, a), find(arr, b)
    if a < b: 
        arr[b] = a
        change(arr, b, a)
    else:
        arr[a] = b
        change(arr, a, b)

def solution(n, computers):
    answer = 0
    arr = [i for i in range(n)]
    
    for idx, computer in enumerate(computers):
        for i, c in enumerate(computer):
            if idx != i and c == 1:
                union(arr, idx, i)
            
    for i in range(n):
        if i in arr: answer += 1

    return answer
