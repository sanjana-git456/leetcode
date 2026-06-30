x = list(map(int, input("Enter: ").split()))
def rob(x):
    dp = [0]*len(x)
    dp[0] = x[0]
    dp[1] = max(x[0],x[1])
    for i in range(2,len(x)):
        dp[i] = max(dp[i-1], dp[i-2] + x[i])
    return dp[-1]
print(rob(x))