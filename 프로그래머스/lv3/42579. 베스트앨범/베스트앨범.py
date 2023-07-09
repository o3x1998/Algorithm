def solution(genres, plays):
    answer = []
    dic = dict()
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = 0
        dic[genres[i]] += plays[i]
        
    dic = sorted(dic.items(), key=lambda x: -x[1])

    for k, v in dic:
        tmp = []
        for i in range(len(genres)):
            if genres[i] == k:
                tmp.append([plays[i], i])
        tmp = sorted(tmp, key=lambda x: (-x[0], x[1]))
        for i in range(len(tmp)):
            if i == 2: break
            answer.append(tmp[i][1])

    return answer