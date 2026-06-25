x = list(map(int, input("Enter: ").split()))
half = len(x)//2
l = []
d = {}
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] > half:
        print(i)