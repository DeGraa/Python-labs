def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3:
            if nums[i] == nums[i + 1]:
                return True

    return False


print(has_33([1, 3, 3, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
