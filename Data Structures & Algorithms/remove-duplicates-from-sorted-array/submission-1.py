class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        found = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in found:
                nums.pop(i)
                continue
            found.append(nums[i])
        print(nums)
        return len(nums)
        