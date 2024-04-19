class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        itr = len(nums)
       
        for i in range(itr):
            for j in range(itr):
                if nums[i]+nums[j]== target and i != j:
                    print(i,j)
                    return [i,j]
