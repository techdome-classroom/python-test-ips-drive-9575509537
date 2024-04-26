def smallest_missing_positive_integer(nums: List[int]) -> int:

   def smallest_missing_positive_integer(nums):
    # Rearrange the list so that nums[i] = i + 1 if possible
    def rearrange(nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    rearrange(nums)

    # Iterate through the rearranged list to find the smallest missing positive integer
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

    # If no missing positive integer is found, return the length of the list plus 1
    return len(nums) + 1

# Example usage:
nums1 = []
nums2 = []
nums3 = []
nums4 = []
nums5 = []
nums6 = []
nums7 = []
print(smallest_missing_positive_integer(nums1))  # Output: 2
print(smallest_missing_positive_integer(nums2))  # Output: 3
print(smallest_missing_positive_integer(nums3))  # Output: 1
print(smallest_missing_positive_integer(nums4))  # Output: 4
print(smallest_missing_positive_integer(nums5))  # Output: 5
print(smallest_missing_positive_integer(nums6))  # Output: 6
print(smallest_missing_positive_integer(nums7))  # Output: 7
