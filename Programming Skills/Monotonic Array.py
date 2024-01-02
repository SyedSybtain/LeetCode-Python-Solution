class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mono1=0
        mono2 = 0
        for i in range(len(nums)-1):
            if (nums[i+1]>=nums[i]):
                mono1 +=1
            if (nums[i+1]<=nums[i]):
                mono2 +=1
        if (mono1 == len(nums)-1) or (mono2 == len(nums)-1):
            return True
        else:
            return False
        
