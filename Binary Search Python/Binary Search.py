class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if any(target == num for num in nums):
            for i in range(len(nums)):
                while nums[i] == target:
                    return i
        else:
            return -1
