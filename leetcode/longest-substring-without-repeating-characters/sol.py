#!/usr/bin/env python

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if s is None or len(s) == 0:
            return 0
        max = 1
        cur = s[0]
        for i in range(1, len(s)):
            p = cur.find(s[i])
            if p == -1:
                cur += s[i]
            else:
                print "cur = %s" % (cur)
                if len(cur) > max:
                    max = len(cur)
                cur = cur[p+1:]+s[i]
                l = len(cur)
                print "after cur = %s" % (cur)
        if len(cur) > max:
            max = len(cur)
        return max

if __name__ == "__main__":
    sol = Solution()
    word="qopubjguxhxdipfzwswybgfylqvjzhar"
    print "word = %s" % (word)
    print sol.lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")

