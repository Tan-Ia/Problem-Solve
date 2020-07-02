k, n, w =map(int,input().split())
sum_of_banans = [ k*banana for banana in range(1, w+1)]
banana_price = sum(sum_of_banans)
if banana_price == 0 or banana_price < 0:
    need = 0
else:
    need = banana_price - n
print(need)