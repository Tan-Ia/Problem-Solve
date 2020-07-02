n = int(input())
l  = 0
data = []
for i in range(n):
    a, b = map(int, input().split()[:2])
    l =  (l + b) - a
    data.append(l)
print(max(data))



