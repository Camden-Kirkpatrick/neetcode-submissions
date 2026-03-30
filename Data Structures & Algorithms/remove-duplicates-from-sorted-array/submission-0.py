class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
        
        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)