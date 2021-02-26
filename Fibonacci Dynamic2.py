

def feb(n):
    if n <= 2:
        return 1
    global dp
    first = 0
    second = 0
    if (dp[n - 1] != -1):
        first = dp[n - 1]
    else:
        first = feb(n - 1)
    if (dp[n - 2] != -1):
        second = dp[n - 2]
    else:
        second = feb(n - 2)
    dp[n] = first + second
    return dp[n]

n = 600

dp = [-1 for i in range(n+1)]
print(feb(n))
