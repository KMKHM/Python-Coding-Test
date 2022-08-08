# DP 
N = int(input())
def sol(N):
    dp = [0, 1, 1]
    for a in range(3, N+1):
        dp.append(dp[a-1] + dp[a-2])
    return dp[N]

