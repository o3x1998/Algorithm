import math

def solution(n, stations, w):
    answer = 0
    idx = 1
    
    for st in stations: 
        s, e = st-w, st+w
        if s < 1: s = 1
        if e > n: e = n
        answer += math.ceil((s-idx) / (1+(2*w)))
        idx = e+1

    if n >= idx:
        answer += math.ceil((n-idx+1) / (1+(2*w)))
        
    return answer