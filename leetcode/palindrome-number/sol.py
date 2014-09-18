#!/usr/bin/env python
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x == -1:
            return True
        def ll(x):
            return 0 if x == 0 or x == -1 else ll(x/10)+1
        
        p = x >= 0
        l = ll(x)
        print "x is %d l is %d" % (x, l)
        t = x
        for a in range(l/2):
            mark = 10**(a)+10**(l-1-a)
            b = (t / (10**(a))) % 10
            b = b if p else 10-b
            t = (t - b * mark) if p else (t+b*mark)
            # print "t=%d" % (t)
        if l % 2:
            b = (t/(10**(l/2))) % 10
            b = b if p else 10-b
            t = (t - b * (10**(l/2))) if p else (t+b*(10**(l/2)))
        return t == 0

if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(-2147483648)
    print sol.isPalindrome(1234321)
    print sol.isPalindrome(-1234321)
    print sol.isPalindrome(1)
    print sol.isPalindrome(-1)
    print sol.isPalindrome(-11)
