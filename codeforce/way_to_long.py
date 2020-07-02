test_case = int(input())

for i in range(test_case):
    sentence = input()
    length = len(sentence)
    if length > 10:
        output = f"{sentence[0]}{len(sentence[1:-1])}{sentence[-1]}"
    else:
        output = sentence
    print(output)
