def isPrime(num):
    if num == 0 or num == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    if k != 10:
        a = []
        while True:
            a.append(n%k)
            n = n//k
            if n == 0: break

        a = a[::-1]
    else: a = list(map(int, str(n)))

    s, e, cnt = 0, 0, 0
    while True:
        if a[e] == 0:
            num = 0
            for j in reversed(a[s:e]):
                num += (j*(10**cnt))
                cnt += 1
            s, e = e+1, e+1
            if isPrime(num): answer += 1
        e += 1
        cnt = 0
        
        if e == len(a):
            num = 0
            for j in reversed(a[s:e]):
                num += (j*(10**cnt))
                cnt += 1
            if isPrime(num): answer += 1
            break

    return answer