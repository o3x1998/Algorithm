n = int(input())

def fibo(n):
    if n == 0 or n == 1: 
        memo[n] = n
        return memo[n]
    if memo[n] == -1:
        memo[n] = (fibo(n-1) + fibo(n-2))
        return memo[n]
    else:
        return memo[n]

memo = [-1] * (n+1)

print(fibo(n))