x = list(map(int, input("Enter numbers: ").split()))
def dup(n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
        else:
            return True
    return False
print(dup(x))