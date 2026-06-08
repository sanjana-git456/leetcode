x = list(map(int, input("Enter numbers: ").split()))
maxdiff = 0
minnum = x[0]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[j]-x[i] > maxdiff:
#             maxdiff = (x[j]-x[i])
#         else:
#             continue
# print(maxdiff)

for i in range(1,len(x)):
    p = x[i] - minnum
    if p > maxdiff:
        maxdiff = p
    if minnum > x[i]:
        minnum = x[i]
print(maxdiff)