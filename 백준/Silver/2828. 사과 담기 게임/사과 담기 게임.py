# n : 몇 칸
# m : 바구니 몇 칸
# j : 사과 몇 개

n, m = map(int, input().split())
j = int(input())
a = [int(input()) for _ in range(j)]

screen = list(range(0, n+1))
basket = [1, m]

cnt = 0

for x in a:
    if x >= basket[0] and x <= basket[1]:
        continue
    else:
        if x < basket[0]:
            tmp = basket[0] - x
            cnt += tmp
            basket[0] -= tmp
            basket[1] -= tmp
        elif x > basket[1]:
            tmp = x - basket[1]
            cnt += tmp
            basket[0] += tmp
            basket[1] += tmp
            
print(cnt)