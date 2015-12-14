#!/usr/bin/env python

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        p = {0:1, 1:1}
        for i in range(2,n+1):
            p[i]=p[i-1]*i
        
        sk = []
        for i in range(n):
            sk.append(True)
        
        kl = k-1
        res = ""
        for i in range(n,0,-1):
            l = (kl/p[i-1])
            kl = kl%p[i-1]
            j = 0
            ji = 0
            while j < l+1:
                if sk[ji]:
                    j += 1
                ji += 1
            ji -= 1
            assert sk[ji]
            sk[ji] = False
            res += "%d" % (ji+1)
        return res

def test(n, k):
    sol = Solution()
    print "input: %d %d" % (n, k)
    print "output: %s" % (sol.getPermutation(n, k))

if __name__ == "__main__":
    test(3, 4)
    test(4, 8)

