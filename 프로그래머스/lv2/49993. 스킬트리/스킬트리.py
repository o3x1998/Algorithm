def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        idx = 0 #skill의 인덱스
        flag = True
        for i in range(len(st)):
            if st[i] in skill:
                tmp = skill.index(st[i])
                if idx != tmp: 
                    flag = False
                    break
                else: idx += 1
        if flag: answer += 1
        
    return answer
