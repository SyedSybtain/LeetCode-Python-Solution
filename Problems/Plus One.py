class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strr = []
        digits_out = []
        for i in digits:
            strr.append(str(i))
        strr = ''.join(strr)
        strr =  int(strr)
        strr += 1
        for i in str(strr):
            digits_out.append(int(i))
        return digits_out
        
