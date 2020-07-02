name_input = input().lower()
sum = list(set(name_input))

if len(sum) %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

