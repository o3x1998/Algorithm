def solution(k, tangerine):
    answer = 0
    dic = {n:0 for n in set(tangerine)} 
    for t in tangerine: dic[t] += 1
    dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])

    for idx, v in dic:
        k -= v
        answer += 1
        if k <= 0: break
    
    return answer