''' 
Start iterating from the second element (index 1) to the end of the list.

For each element:

If the element is odd, replace it with the previous element plus 2.

If the element is even, calculate the average of all previous elements, floor the average to the nearest even number, and replace the current element with this value.

Return the modified list.
'''


def next_2(nums) -> list:
    for i in range(1, len(nums)):
        if nums[i] % 2 != 0:
            nums[i] = nums[i-1] + 2
        else:
            average = sum(nums[:i]) / len(nums[:i])
            nums[i] = int(2 * (average // 2))   # to make it even

    return nums
