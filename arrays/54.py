x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

top = 0
bottom = len(x) - 1
left = 0
right = len(x[0]) - 1
result = []

while top <= bottom and left <= right:
    for i in range(left, right+1):
        result.append(x[top][i])
    top += 1
    for i in range(top, bottom+1):
        result.append(x[i][right])
    right -= 1
    for i in range(right, left-1, -1):
        result.append(x[bottom][i])
    bottom -= 1
    for i in range(bottom, top-1, -1):
        result.append(x[i][left])
    left += 1
print(result)