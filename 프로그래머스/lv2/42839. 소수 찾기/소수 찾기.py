import itertools

def solution(numbers):
    def primeNum(n):
        if n in (0, 1): return False
        if n == 2: return True
        for i in range(2, n):
            if n % i == 0:
                return False 
        return True
          
    answer = 0
    nums = set()
    for i in range(len(numbers)):
        nums |= set(map(int, map("".join, itertools.permutations(list(numbers), i + 1))))
    
    for n in nums:
        if primeNum(n): answer += 1

    return answer