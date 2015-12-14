#!/usr/bin/env python

class Solution:
    def __init__(self):
        self.poss = set()
        self.imposs = set()
    # @return a boolean
    def isScramble(self, s1, s2):
        print "input %s %s" % (s1, s2)
        if s1 == s2:
            return True
        if (s1, s2) in self.poss:
            return True
        if (s1, s2) in self.imposs:
            return False
        assert len(s1) == len(s2)
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]):
                self.poss.add((s1,s2))
                return True
        self.imposs.add((s1,s2))
        return False

def test(a, b):
    sol = Solution()
    print "input: '%s' '%s'" % (a, b)
    print "result %s" % (sol.isScramble(a, b))

if __name__ == "__main__":
    test("ab", "ba")
