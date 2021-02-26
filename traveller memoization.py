def traveller(n, m, memo):
    key = n, m
    key1 = m, n
    if key in memo:
        return memo[key]
    if key1 in memo:
        return memo[key1]
    if n == 1 and m == 1:
        return 1
    elif n == 0 or m == 0:
        return 0
    else:
        memo[key] = traveller(n-1, m, memo) + traveller(n, m-1, memo)
        return memo[key]

memo = {}
print(traveller(800, 100, memo))
