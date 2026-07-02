x = int(input("Enter: "))
s = str(abs(x))
if x >= 0:
    print(''.join(s[::-1]))
else:
    print("-"+''.join(s[::-1]))