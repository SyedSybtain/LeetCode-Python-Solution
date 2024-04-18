class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        M = int(num / 1000)
        m = num % 1000
        CM = int(m / 900)
        cm = m % 900
        D = int(cm / 500)
        d = cm % 500
        CD = int(d / 400)
        cd = d % 400
        C = int(cd / 100)
        c = cd % 100
        XC = int(c / 90)
        xc = c % 90
        L = int(xc / 50)
        l = xc % 50
        XL = int(l / 40)
        xl = l % 40
        X = int(xl / 10)
        x = xl % 10
        IX = int(x / 9)
        ix = x % 9
        V = int(ix / 5)
        v = ix % 5
        IV = int(v / 4)
        iv = v % 4
        I = int(iv / 1)
        i = iv % 1
    
        if M >= 1:
            roman += M*"M"
        if CM >= 1:
            roman += CM*"CM"
        if D >= 1:
            roman += D*"D"
        if CD >= 1:
            roman += CD*"CD"
        if C >= 1:
            roman += C*"C"
        if XC >= 1:
            roman += XC*"XC"
        if L >= 1:
            roman += L*"L"
        if XL >= 1:
            roman += XL*"XL"
        if X >= 1:
            roman += X*"X"
        if IX >= 1:
            roman += IX*"IX"
        if V >= 1:
            roman += V*"V"
        if IV >= 1:
            roman += IV*"IV"
        if I >= 1:
            roman += I*"I"

        return roman
        
