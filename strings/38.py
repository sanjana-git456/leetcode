x = int(input("Enter: "))
def read(s):
    result = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1
    result += str(count) + s[-1]
    return result
def countsay(n):
    s = "1"
    for i in range(n-1):
        s = read(s)
    return s
print(countsay(x))