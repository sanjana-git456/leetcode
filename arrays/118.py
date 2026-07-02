x = int(input("Enter: "))
def pascal(x):
    result = []
    for i in range(x):
        if i == 0:
            result.append([1])
        else:
            prev = result[-1]
            row = [1]
            for j in range(1,i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            result.append(row)
    return result
print(pascal(x))