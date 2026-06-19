x = input("Enter: ")
d = {')' : '(' , ']' : '[' , '}' : '{'}
a = []
valid = True
for i in x:
    if i in d:
        if a and a[-1] == d[i]:
            a.pop()
        else:
            valid = False
            break
    else:
        a.append(i)
if valid and a == []:
    print("Valid")
else:
    print("Invalid")