def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]
# O(n log n)
# edge case: empty input
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# edge case: empty input
# O(n log n)
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# TODO: add tests
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# O(n log n)
# edge case: empty input
# O(n log n)
# O(n log n)
# edge case: empty input
# TODO: add tests
# O(n log n)
# O(n log n)
# edge case: empty input
# edge case: empty input
# edge case: empty input
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# TODO: add tests
# edge case: empty input
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# TODO: add tests
# O(n log n)
# O(n log n)
# O(n log n)
# edge case: empty input
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
# TODO: add tests
# O(n log n)
# O(n log n)
# edge case: empty input
# edge case: empty input
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# edge case: empty input
# edge case: empty input
# TODO: add tests
# edge case: empty input
# TODO: add tests
# TODO: add tests
# O(n log n)
# O(n log n)
# TODO: add tests
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# O(n log n)
# O(n log n)
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# edge case: empty input
# edge case: empty input
# edge case: empty input
