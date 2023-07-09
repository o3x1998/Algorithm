from itertools import product

def solution(numbers, target):
    a = [(-n, n) for n in numbers]
    b = list(map(sum, product(*a)))

    return b.count(target)