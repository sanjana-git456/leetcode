x = input("Enter: ")
def unique(x):
    l = list(x)
    for i in range(len(x)):
        l.remove(x[i])
        if x[i] not in l:
            return i
print(unique(x))