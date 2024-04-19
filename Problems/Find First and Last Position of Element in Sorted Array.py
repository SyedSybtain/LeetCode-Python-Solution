class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index = []
        if any(target == num for num in nums):
            for i,num in enumerate(nums):
                if num == target:
                    index.append(i)
            return ([index[0],index[-1]])
        else:
            return ([-1,-1])
        
