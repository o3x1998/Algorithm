def solution(participant, completion):
    dic = {}
    tmp = 0
    
    for p in participant:
        dic[hash(p)] = p
        tmp += hash(p)
        
    for c in completion:
        tmp -= hash(c)
        
    return dic[tmp]