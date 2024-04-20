class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = sorted(nums1+nums2)
        len_nums = len(nums)
        odd = (len_nums+1)/2
        odd = odd - 1
        even_index = len_nums/2
        even = float(nums[even_index]+nums[even_index-1])/2
        if len_nums%2 == 1:
            return nums[odd]
        else:
            return even
