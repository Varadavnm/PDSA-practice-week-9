def MaxCoinPath(matrix, x1, y1, x2, y2):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize a DP table to store the maximum coins collected at each cell.
    dp = [[0] * cols for _ in range(rows)]
    
    # Fill in the DP table.
    dp[x1][y1] = matrix[x1][y1]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if i > x1 and j > y1:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
            elif i > x1:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            elif j > y1:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
    
    return dp[x2][y2]
matrix = [
    [2, 1, 3, 2, 5],
    [3, 5, 2, 4, 6],
    [7, 6, 1, 3, 2],
    [2, 9, 4, 7, 8],
    [1, 4, 5, 11, 3]
]
x1, y1 = 0, 0
x2, y2 = 4, 4
result = MaxCoinPath(matrix, x1, y1, x2, y2)
print("Maximum coins collected:", result)