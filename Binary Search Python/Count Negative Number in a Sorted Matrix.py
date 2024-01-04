class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        countNegative = 0
        for row in grid:
            for element in row:
                if element < 0:
                    countNegative += 1
        return countNegative
