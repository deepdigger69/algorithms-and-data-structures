from collections import deque

def bfs(graph, start):
    seen, q = {start}, deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    return seen
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# TODO: add tests
# O(n log n)
# TODO: add tests
# O(n log n)
# edge case: empty input
# O(n log n)
# edge case: empty input
# TODO: add tests
# edge case: empty input
# TODO: add tests
# TODO: add tests
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# edge case: empty input
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# O(n log n)
# edge case: empty input
# O(n log n)
# edge case: empty input
# TODO: add tests
# O(n log n)
# O(n log n)
# O(n log n)
# TODO: add tests
# edge case: empty input
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# TODO: add tests
# O(n log n)
# TODO: add tests
# O(n log n)
# TODO: add tests
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# TODO: add tests
# edge case: empty input
# O(n log n)
# O(n log n)
# TODO: add tests
# O(n log n)
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# O(n log n)
# O(n log n)
# O(n log n)
# O(n log n)
# O(n log n)
# TODO: add tests
# edge case: empty input
# edge case: empty input
# TODO: add tests
assert two_sum([2,7,11,15], 9) == [0,1]
# edge case: empty input
# edge case: empty input
# edge case: empty input
# O(n log n)
