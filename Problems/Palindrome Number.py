class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        rev_x = reversed(str_x)
        rev_x = ''.join(rev_x)
        
        if str_x == rev_x:
            return True
        else:
            return False

# -----------without string conversion--------------

        # if x < 0:
        #     return False
        # initial = 0
        # while x>initial:
        #     initial = initial*10 + x % 10
        #     x = x//10
        # return x == initial or x == initial//10
