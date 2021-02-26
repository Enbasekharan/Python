
def howsum(targetsum, numbers, memo):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return 'null'
    for num in numbers:
        remainder = targetsum - num
        remainder_result = howsum(remainder, numbers, memo)
        if remainder_result != 'null':
            memo[targetsum] = [*remainder_result, num]
            return memo[targetsum]
    memo[targetsum] = 'null'
    return memo[targetsum]



memo = {}
targetsum = 100
numbers = [10, 5, 1]
print(howsum(targetsum, numbers, memo))


