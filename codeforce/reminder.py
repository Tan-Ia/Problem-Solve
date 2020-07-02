test = int(input())
for i in range(test):
    x, y, n = map(int, input().split()[:3])
    last = n / x
    print( int(last % x))

