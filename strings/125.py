x = input("Enter: ")
s = ""
def pal(x,s):
    for i in x:
        if i.isalnum():
            s += i.lower()
    r = s[::-1]
    if s == r:
        return True
    else:
        return False
print(pal(x,s))