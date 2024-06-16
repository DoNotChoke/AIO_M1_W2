def levenshtein(source, target):
    source = "#"+ source
    target = "#"+ target
    n= len(source)
    m= len(target)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range (n):
        dp[i][0]= i
    for j in range (m):
        dp[0][j]= j
    for i in range (1,n):
        for j in range (1,m):
            x= dp[i-1][j]+1  #insert
            y= dp[i][j-1]+1 #erase
            z= dp[i-1][j-1]     #match/ mismatch
            if(source[i] != target[j]):
                z+= 1
            d= min(x,y)
            d= min(d,z)
            dp[i][j]= d
    return dp[n-1][m-1]


source= "kitten"
target= "sitting"
print(levenshtein(source, target))
        