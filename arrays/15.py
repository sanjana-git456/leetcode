x = list(map(int, input("Enter: ").split()))
x = sorted(x)
result = []
for i in range(1,len(x)):
    fix = x[i]
    for j in range(i,len(x)):
        pointer1 = x[j]
        for k in range(j+1,len(x)):
            if (fix+pointer1+x[k] == 0):
                pointer2 = x[k]
                triplet = [fix,pointer1,pointer2]
                if triplet not in result:
                    result.append(triplet)
            else:
                continue
print(result)