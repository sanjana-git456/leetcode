s = input("Enter s: ")
t = input("Enter t: ")
def anagram(a,b):
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    else:
        return False
# print(anagram(s,t))

def anag(s,t):
    d1 = {}
    for i in s:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] = d1[i]+1
    d2 = {}
    for i in t:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] = d2[i]+1
    if d1 == d2:
        return True
    else:
        return False
print(anag(s,t))