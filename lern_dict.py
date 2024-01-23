numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

new_dict = {}

for num in numbers:
    if num not in new_dict:
        new_dict[num] = 1
    else:
        new_dict[num] += 1
print(new_dict)
