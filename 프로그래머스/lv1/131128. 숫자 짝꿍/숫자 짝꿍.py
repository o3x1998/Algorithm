from collections import Counter

def solution(X, Y):
    answer = ''
    X, Y = Counter(X), Counter(Y)

    for i in range(9, -1, -1):
        minN = min(X[str(i)], Y[str(i)])
        answer += (str(i)*minN)
    
    if answer == '': return "-1"
    elif answer[0] == '0': return "0"
    else: return answer