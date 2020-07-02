
#
# numbers = list(i  for i in range(1, n+1))
# print( abs(6-int(S[i:i+3]))  for i in range(len(numbers)-2)))


def recur(n, out, i=1, index=0):

    # if sum becomes n, print the combination
    if n == 0:
        print(out[:index])

    # start from previous element in the combination till n
    for j in range(i, n + 1):

        # place current element at current index
        out[index] = j

        # recur with reduced sum
        recur(n - j, out, j, index + 1)


if __name__ == '__main__':
    n = int(input())
    out = [None] * n

    # print all combination of numbers from 1 to n having sum n
    recur(n, out)
