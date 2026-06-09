x = list(map(int, input("Enter numbers: ").split()))
l = []
maximum = x[0]
current = x[0]
for i in range(1,len(x)):
    current = max(x[i], (current+x[i]))
    maximum = max(maximum, current)
print(maximum)