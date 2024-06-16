def levenshtein_distance(token1, token2):
    n = len(token1)
    m = len(token2)
    dp = [[0 for _ in range(m+1)] for _ in range(2)]
    for j in range(m+1):
        dp[0][j] = j
    for i in range(n+1):
        for j in range(m+1):
            if j == 0:
                dp[1][j] = i
            else:
                x = dp[0][j]+1
                y = dp[1][j-1]+1
                z = dp[0][j-1]
                if token1[i-1] != token2[j-1]:
                    z += 1
                d = min(x, y)
                d = min(d, z)
                dp[1][j] = d
        for j in range(m+1):
            dp[0][j] = dp[1][j]
    distance = dp[1][m]
    return distance


assert (levenshtein_distance("hi", "hello")) == 4
print(levenshtein_distance("hola", "hello"))
