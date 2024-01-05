class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        out1 = []
        out2 = []
        output = []

        for num1 in nums1:
            if all(num1 != num2 for num2 in nums2):
                out1.append(num1)

        for num2 in nums2:
            if all(num2 != num1 for num1 in nums1):
                out2.append(num2)
        output = [list(set(out1)),list(set(out2))]
        return output
