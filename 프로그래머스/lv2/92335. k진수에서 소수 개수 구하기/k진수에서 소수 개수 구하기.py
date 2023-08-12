def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    a = ''
    
    while n:
        a += str(n%k)
        n //= k
    a = a[::-1]

    nums = a.split('0')
    for n in nums:
        if not n: continue
        if isPrime(int(n)): answer += 1

    return answer