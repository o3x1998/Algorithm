def solution(name, yearning, photo):
    answer = []
    dic = {n : i for i, n in enumerate(name)} #이름의 인덱스로 yearning에서 점수 찾기

    for p in photo:
        cnt = 0
        for x in p:
            cnt += (yearning[dic[x]] if x in name else 0)
        answer.append(cnt)
        
    return answer