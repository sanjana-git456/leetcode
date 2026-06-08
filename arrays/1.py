x = list(map(int, input("Enter numbers: ").split()))
t = int(input("Enter target: "))
def twosum(n):
    d = {}
    for i in range(len(n)):
        c = t-x[i]
        if c in d:
            print(d[c],i)
            break
        d[x[i]] = i
twosum(x)