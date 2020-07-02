test_case = int(input())

for i in range(1,test_case+1):
    b, f, toss = map(int,input().split()[:3])
    if b == toss:
        print(f"Case {i} : Badal slapped Fojael")
    else:
        print(f"Case {i} : Fojael slapped Badal")
