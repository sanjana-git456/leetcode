def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(x):
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])
    return merge(left, right)

x = list(map(int, input("Enter: ").split()))
print(mergeSort(x))