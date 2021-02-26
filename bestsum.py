
def bestsum(targetsum, numbers, memo):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return 'null'

    shortest_combination = 'null'

    for num in numbers:
        remainder = targetsum - num
        remainder_result = bestsum(remainder, numbers, memo)
        if remainder_result != 'null':
            combination = [*remainder_result, num]
            if shortest_combination == 'null' or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[targetsum] = shortest_combination
    return memo[targetsum]



memo = {}
targetsum = 100
numbers = [2, 3, 10, 5]
print(bestsum(targetsum, numbers, memo))


