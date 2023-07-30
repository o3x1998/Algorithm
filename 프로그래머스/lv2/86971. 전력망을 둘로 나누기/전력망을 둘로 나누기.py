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

def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        arr = [k for k in range(n+1)]
        for j in range(len(wires)):
            if i == j: continue
            union(arr, wires[j][0], wires[j][1])
        p = list(set(arr[1:]))
        answer.append(abs(arr.count(p[0]) - arr.count(p[1])))
    
    return min(answer)