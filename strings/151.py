x = input("Enter: ")
x = str(x).strip()
x = x.split()
print(' '.join(x[::-1]))