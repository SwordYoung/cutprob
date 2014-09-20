#!/usr/bin/env python

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if s is None or len(s) == 0:
            return None
        d = {-1:[[]], 0:[[s[0]]]}
        for i in range(1, len(s)):
            c = s[i]
            res = []
            final = set([""])
            for a in d[i-1]:
                res.append(a+[c])
                if len(a[-1])+1 <= i:
                    final.add(a[-1])
#             print "final=%s" % (final)
            for f in final:
                fp = i-len(f)-1
                if s[fp] == c:
                    #valid not
                    new_p = c + f + c
                    for j in d[fp-1]:
                        res.append(j+[new_p])
#             print "i=%d res=%s" % (i, res)
            d[i] = res
        return d[len(s)-1]

def test(s):
    sol = Solution()
    print "input: %s" % (s)
    print "output: %s" % (sol.partition(s))

if __name__ == "__main__":
    test("bb")
    test("bbbbb")
    test("abbbbba")

