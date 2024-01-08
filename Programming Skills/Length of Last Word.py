class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = []
        word = s.split(' ')
        words = list(word)
        for word in words:
            if word!= '':
                output.append(word)

        return (len(output[-1]))
        
