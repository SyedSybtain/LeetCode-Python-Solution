class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        elif x > 0:
            x = str(x)
            xr = x[::-1]
            out = int(xr)
            if out > 2**31:
                return 0
            return out

        elif x < 0:
            x = str(x)
            i0 = x[0]
            i1 = x[1::]
            xr = i1[::-1]
            out = int(i0+xr)
            if out < -2**31:
                return 0
            return out
