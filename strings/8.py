x = int(input("Enter: "))
s = str(abs(x))
l = []
for i in s:
    l.append(i)
if x >= 0:
    print(''.join(l[::-1]))
else:
    print("-"+''.join(l[::-1]))