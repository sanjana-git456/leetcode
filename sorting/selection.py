x = list(map(int, input("Enter: ").split()))
for i in range(len(x)):
    m = i
    for j in range(i+1,len(x)):
        if x[j] < x[m]:
            m = j
    x[i],x[m] = x[m],x[i]
print(x)