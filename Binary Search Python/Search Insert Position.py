class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if any(num == target for num in nums):
            for i in range(len_nums):
                while nums[i] == target:
                    return i
        else:
            if target > nums[len_nums-1]:
                return len_nums
            if target < nums[0]:
                return 0
            for  k in range(len_nums-1):
                left = k
                right = k+1
                while (target > nums[left]) and (target < nums[right]):
                    return right
