x = list(map(int, input("Enter: ").split()))
l = []
z = []
for i in x:
    if i != 0:
        l.append(i)
    else:
        z.append(i)
print(l+z)