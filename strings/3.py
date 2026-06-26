x = input("Enter: ")
l = []
m=0
for i in range(len(x)):
    if x[i] not in l:
        l.append(x[i])
    else:
        while x[i] in l:
            l.remove(l[0])
        l.append(x[i])
    m = max(m, len(l))
print(m)