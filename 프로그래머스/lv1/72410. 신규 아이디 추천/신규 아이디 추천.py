import re

def solution(new_id):
    answer = new_id.lower() 
    answer = re.sub('[^a-z\d\-\_\.]', '', answer) 
    answer = re.sub('\.\.+', '.', answer) 
    answer = re.sub('^\.', '', answer) 
    if len(answer) > 0 and answer[len(answer)-1] == '.': answer = answer[:len(answer)-1]
    if answer == '': answer = 'a' 
    answer = answer[:15]
    if answer[len(answer)-1] == '.': answer = answer[:len(answer)-1]
    if len(answer) <= 2: answer += (answer[len(answer)-1] * (3-len(answer)))
    return answer