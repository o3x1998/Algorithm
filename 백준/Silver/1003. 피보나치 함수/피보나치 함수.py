import sys
input = sys.stdin.readline

T = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])