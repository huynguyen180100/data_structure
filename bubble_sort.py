numbers = [10, 12, 15, 16, 20, 3]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if  numbers[j] < numbers[i]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
print(numbers)