import sys

input = sys.stdin.readline

V, E = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(E)]
parent = [i for i in range(V+1)]
res = 0

tree.sort(key=lambda x: x[2])

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    
    if a >= b:
        parent[b] = a
    else:
        parent[a] = b


for a, b, w in tree:
    if find(a) != find(b):
        res += w
        union(a, b)

print(res)