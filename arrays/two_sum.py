def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
# TODO: add tests
# O(n log n)
# O(n log n)
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
