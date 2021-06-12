import sys
sys.setrecursionlimit(10000)

def divide(numbers, start, end):
    if start == end:
        return [numbers[start]]
    else:
        middle = (start + end)//2
        left_numbers = divide(numbers, start, end)
        right_numbers = divide(numbers, start, end)
        return conquer(numbers, left_numbers, right_numbers)

def conquer(numbers, left_numbers, right_numbers):
    nums = []
    i = 0
    j = 0
    while i < len(left_numbers) and j < len(right_numbers):
        if left_numbers[i] < right_numbers[j]:
            nums.append(left_numbers[i])
            i += 1
        else:
            nums.append(right_numbers[j])
            j += 1
    if i < len(left_numbers):
        nums += left_numbers[i:]
    if j < len(right_numbers):
        nums += right_numbers[j:]
    return nums
numbers = [20, 10, 16, 6, 89, 1, 5, 9, 100]
divide(numbers, 0, len(numbers)-1)