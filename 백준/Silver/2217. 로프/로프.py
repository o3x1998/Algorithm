k = int(input()) # 로프 개수
arr = [int(input()) for _ in range(k)] # 로프별 최대 중량
arr.sort(reverse=True) # 뒤집기
max_w = -1

for i in range(1, k+1):
  tmp = i * arr[i-1]
  max_w = max(max_w, tmp)

print(max_w)