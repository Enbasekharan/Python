
def cansum(targetsum, numbers, memo):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in numbers:
        remainder = targetsum - num
        if cansum(remainder, numbers, memo) == True:
            memo[targetsum] = True
            return True
    memo[targetsum] = False
    return False

memo = {}
targetsum = 300
numbers = [7, 14]
print(cansum(targetsum, numbers, memo))


