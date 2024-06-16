from collections import deque


def max_kernel(num_list, k):
    result = []
    n = len(num_list)
    q = deque()
    for i in range(k):
        while q and num_list[i] >= num_list[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, n):
        result.append(num_list[q[0]])
        while q and q[0] <= i-k:
            q.popleft()
        while q and num_list[i] >= num_list[q[-1]]:
            q.pop()
        q.append(i)
    result.append(num_list[q[0]])
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
