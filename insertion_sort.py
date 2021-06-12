numbers = [11, 12, 5, 7, 30, 56]
for i in range(1, len(numbers)):
    j = i - 1
    curr = numbers[i]
    while j >= 0 and curr < numbers[j]:
        numbers[j+1] = numbers[j]
        j -= 1
        numbers[j+1] = curr
print(numbers)