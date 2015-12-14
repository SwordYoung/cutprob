#!/usr/bin/env python

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        sp = '$#' + '#'.join(list(s)) + '#&'
        p = [1]*len(sp)
        
        mx = 1
        id = 1
        max_id = 0
        max_p = 0
        for i in xrange(2, len(sp)-2):
            if i < mx:
                j = id*2 - i
                if p[j] > mx-i:
                    p[i] = mx-i
                else:
                    p[i] = p[j]
            else:
                mx = 1
                id = 1
            while sp[i+p[i]] == sp[i-p[i]]:
                p[i] += 1
            if p[i] > mx - id:
                id = i
                mx = id + p[i]
            if p[i] > max_p:
                max_p = p[i]
                max_id = i
        res = sp[max_id-max_p+1:max_id+max_p]
        res = res.split('#')
        res = ''.join(res)
        return res

def test(s):
    sol = Solution()
    res = sol.longestPalindrome(s)
    print "lps for %s is %s" % (s, res)

if __name__ == "__main__":
    test("abcdefgfgabds")
