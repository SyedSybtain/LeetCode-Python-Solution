class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ''
        for i in s:
            if (ord(i) >=97) and (ord(i)<=122):
                new_s += i
            if (ord(i) >=47) and (ord(i)<=57):
                new_s += i
        s = new_s[::-1]
        print(new_s,s)
        if new_s == s:
            return True
        else:
            return False

