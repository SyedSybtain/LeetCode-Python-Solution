class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,element in enumerate(nums):
            if element == target:
                return i
        return -1
