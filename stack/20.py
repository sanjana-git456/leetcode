x = input("Enter: ")
d = {')' : '(' , ']' : '[' , '}' : '{'}
a = []
for i in x:
    if i in d:
        if a and a[-1] == d[i]:
            a.pop()
        else:
            print("Invalid")
    else:
        a.append(i)
if a == []:
    print("Valid")