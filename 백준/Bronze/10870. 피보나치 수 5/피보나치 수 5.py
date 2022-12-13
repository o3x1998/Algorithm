a = int(input())
dict = {}

def fibo(n):
    if n in dict:
        return dict[n]
    if n == 0 or n == 1: 
        dict[n] = n
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(a))