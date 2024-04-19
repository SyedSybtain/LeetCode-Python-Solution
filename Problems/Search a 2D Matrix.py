class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for row in matrix:
            for element in row:
                if target == element:
                    return True
        return False
