#!/usr/bin/env python

class Solution:
    # @return a list of lists of integers
    def cc(self, n, k):
        if self.d.has_key((n,k)):
            return self.d[(n,k)]
        if k == 0 or n < k:
            res = None
        elif k == 1:
            self.cc(n-1, k)
            res = [[n]]
            if self.d[(n-1,k)] != None:
                res.extend(self.d[(n-1,k)])
        else:
            self.cc(n-1,k-1)
            self.cc(n-1,k)
            res = []
            if self.d[(n-1,k)] != None:
                res.extend(self.d[(n-1,k)])
            if self.d[(n-1,k-1)] != None:
                for r in self.d[(n-1,k-1)]:
                    res.append(r+[n])
        self.d[(n,k)] = res
        
    def combine(self, n, k):
        self.d = {}
        self.cc(n, k)
        return self.d[(n,k)]

def test(n, k):
    sol = Solution()
    print "input: n=%d k=%d" % (n, k)
    print "output: %s" % (sol.combine(n, k))

if __name__ == "__main__":
    test(4, 2)
    test(6, 3)
