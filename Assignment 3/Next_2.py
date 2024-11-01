def next_2(nums) -> list:
    for i in range(1, len(nums)):
        if nums[i] % 2 != 0:
            nums[i] = nums[i-1] + 2
        else:
            average = sum(nums[:i]) / len(nums[:i])
            nums[i] = int(2 * (average // 2))   # to make it even

    return nums
