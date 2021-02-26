

def feb(n, memo):

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = feb(n-1, memo) + feb(n-2, memo)
    return memo[n]

n = 92

memo = {}
print(feb(n, memo))

