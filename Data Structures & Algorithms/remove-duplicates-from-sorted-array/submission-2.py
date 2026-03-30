class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        found = []
        i = 0
        while i < len(nums):
            if nums[i] in found:
                nums.pop(i)
                continue
            found.append(nums[i])
            i += 1
        print(nums)
        return len(nums)
        