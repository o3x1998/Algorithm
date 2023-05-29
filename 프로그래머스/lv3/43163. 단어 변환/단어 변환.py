from collections import deque

def solution(begin, target, words):
    dq = deque()
    dq.append([begin, 0])
    
    if target not in words: return 0
    
    while True:
        x, y = dq.popleft()
        if x == target: return y
        fail = True
        
        for word in words:
            cnt = 0
            
            for i in range(len(word)):
                if word[i] != x[i]: cnt += 1
            
            if cnt == 1:
                fail = False
                dq.append([word, y+1])
        
        if fail: return 0    