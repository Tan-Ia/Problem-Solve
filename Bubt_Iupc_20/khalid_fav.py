test = int(input())

def summetion(num):
    # # while len(num) >1:
    #    nums = list(int(i) for i in num)
    #    num = str(sum(nums))
    #    summetion(num)
    output = 0
    length = len(num)
    if length > 1:
        nums = list(int(i) for i in num)
        num = str(sum(nums))
        summetion(num)
    if length == 1:
        output = num
    return output








for i in range(test):
    number = input()
    print(summetion(number))



