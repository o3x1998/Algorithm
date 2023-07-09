from itertools import product

def solution(numbers, target):
    answer = 0
    tmp = list(product([-1, 1], repeat=len(numbers)))
    for i in range(len(tmp)):
        mul = [x*y for x,y in zip(numbers, tmp[i])]
        if sum(mul) == target: answer += 1
    
    return answer