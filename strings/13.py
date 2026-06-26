x = input("Enter: ")
d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
result = 0
if len(x) == 1:
    print(d[x])
else:
    for i in range(len(x)-1):
        if d[x[i]] < d[x[i+1]]:
            result -= d[x[i]]
        else:
            result += d[x[i]]
    result += d[x[-1]]
    print(result)