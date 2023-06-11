def solution(routes):
    answer = 0
    camera = -30001
    # 진출 지점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x:x[1])
    for r in routes:
        if r[0] <= camera and r[1] >= camera:
            continue
        else:
            camera = r[1]
            answer += 1        
    
    return answer