class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word12 = word1+word2
        word = []
        for i in range(len(word12)):
            if (i<len(word1)) and (len(word1)>=0):
                word.append(word1[i])
            if (len(word2)>=0) and (i<len(word2)):
                word.append(word2[i])
        return ''.join(word)
