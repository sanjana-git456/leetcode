x = list(map(str, input("Enter words: ").split()))
fix = x[0]
l = []
for i in range(1,len(x)):
    for j in range(len(fix)):
        if j >= len(x[i]) or fix[j] != x[i][j]:
            fix = fix[:j]
            break
print(fix)