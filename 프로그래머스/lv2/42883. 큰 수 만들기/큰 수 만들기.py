def solution(number, k):
    stack = []
    
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    
    if k > 0: stack = stack[:-k]
    
    return ''.join(stack)