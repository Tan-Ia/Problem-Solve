total_prvlm = int(input())
sum = 0
for i in range(total_prvlm):
    p, v, t = map(int,input().split()[:3])
    str_convert = f"{p}{v}{t}"
    if str_convert.count('1') >= 2:
        sum+=1

print(sum)
