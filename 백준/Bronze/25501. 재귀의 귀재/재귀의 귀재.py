t = int(input())
arr = [input() for _ in range(t)]

def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    a, b = recursion(s, 0, len(s)-1, 0)
    return a, b

for s in arr:
    a, b = isPalindrome(s)
    print('{} {}'.format(a, b))