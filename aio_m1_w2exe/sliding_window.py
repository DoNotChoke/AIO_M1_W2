from collections import deque


def sliding_window(arr, k):
    n = len(arr)
    q = deque()
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    ans = []
    for i in range(k, n):
        ans.append(arr[q[0]])
        while q and q[0] <= i-k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    ans.append(arr[q[0]])
    return ans


arr = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
ans = sliding_window(arr, k)
print(ans)
