# Print a Spiral Pattern of Numbers
def print_spiral(n):
    
    matrix = [[0] * n for _ in range(n)]

   
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    num = 1

    while top <= bottom and left <= right:
       
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

  
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

  
    for row in matrix:
        print(" ".join(map(str, row)))


n = 5
print_spiral(n)
