def sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

print('Пузырьковая сортировкa:')
nums = [28, 43, 1, 53, 96, 84, 0, 14]
sort(nums)
print(nums)