a, b = map(int,input().split()[:2])
sum = 0
if a % 2 == 0:
    print(f"{a} is even")
    sum += a
elif a % 2 != 0:
    print(f"{a} is odd")
    sum -= a

if b > 0:
    print(f"{b} is greater than zero")
    sum += b
elif b < 0:
    print(f"{b} is less than zero")
    sum -= b
elif b == 0:
    print(f"{b} is equal to zero")
    sum *=b
ab_sum = a + b
print(f"after adding,a+b is equal to {ab_sum}")
if ab_sum %  2 == 0:
    print(f"after adding {a} {b} sum is equal to {sum}")
    sum +=a
    sum +=b
elif ab_sum % 2 != 0:
    print(f"after removing {a} {b} sum is equal to {sum}")
    sum -= a
    sum -= b
elif ab_sum == 0:
    print(f"the result after multiplying sum = {sum}")
    sum  *= 10
sum *=5
print(f"THE ULTIMATE RESULT = {sum}")
print("I wanna be a national contestant and I can write long code")
