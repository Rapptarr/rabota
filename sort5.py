def sort(nums, start, end):
    if end - start > 1:
        p = part(nums, start, end)
        sort(nums, start, p)
        sort(nums, p + 1, end)

def part(nums, start, end):
    pivot = nums[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and nums[i] <= pivot):
            i = i + 1
        while (i <= j and nums[j] >= pivot):
            j = j - 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[start], nums[j] = nums[j], nums[start]
            return j

print('Быстрая сортировка:')
nums = [28, 43, 1, 53, 96, 84, 0, 14]
nums = [int(x) for x in nums]
sort(nums, 0, len(nums))
print(nums)