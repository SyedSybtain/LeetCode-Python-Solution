class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        add = 0
        sub = 0
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        for i in range(len(s)):
            if s[i] == 'M':
                add = add + M
            elif s[i] == 'D':
                add = add + D
            elif s[i] == 'C':
                add = add + C
            elif s[i] == 'L':
                add = add + L
            elif s[i] == 'X':
                add = add + X
            elif s[i] == 'V':
                add = add + V
            else:
                add = add + I

        for j in range(len(s)-1):
            if (s[j] == 'C' and s[j+1]== 'M') or  (s[j] == 'C' and s[j+1]=='D'):
                sub = sub + 200
            elif (s[j] == 'X' and s[j+1]=='C') or (s[j] == 'X' and s[j+1]=='L'):
                sub = sub + 20
            elif (s[j] == 'I' and s[j+1]=='V') or (s[j]=='I' and s[j+1]=='X'):
                sub = sub + 2
        total = add - sub

        return total
            
