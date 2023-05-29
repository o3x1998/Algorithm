def solution(k, tangerine):
    answer = 0
    dic = {n:0 for n in set(tangerine)} 
    for t in tangerine: dic[t] += 1
    dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])

    sum = 0
    for i in range(len(dic)):
        tmp = (sum + dic[i][1])
        if tmp >= k:
            sum += dic[i][1]
            answer += 1
            break
        else:
            sum += dic[i][1]
            answer += 1
        
    return answer