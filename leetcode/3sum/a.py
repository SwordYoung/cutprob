#!/usr/bin/env python

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def find(self, l, r, v):
        if l == r:
            return l
        if self.n[r] <= v:
            return r
        if self.n[l] > v:
            return l-1
            
        assert self.n[l] <= v and self.n[r] > v
        
        if l == r - 1:
            return l
            
        m = (l+r)/2
        if self.n[m] == v:
            return m
        elif self.n[m] < v:
            return self.find(m+1, r)
        else:
            return self.find(l, m-1)
    def inc(self, l, r):
        l += 1
        while l < r and self.n[l-1] == self.n[l]:
            l += 1
        return l
    def dec(self, r, l):
        r -= 1
        while r > l and self.n[r+1] == self.n[r]:
            r -= 1
        return r
 
    def threeSum(self, num):
        num.sort()
        self.n = num
        
        results = []
        i = 0
        while i < len(num)-2:
            val1 = num[i]
            l = i+1
            r = len(num)-1
            while l < r:
                assert l < len(num)
                assert r > 1
                sum = num[l] + num[r] + val1
                if sum == 0:
                    print "find a result %d %d %d" % (i, l, r)
                    results.append([val1, num[l], num[r]])
                    l = self.inc(l, r)
                    r = self.dec(r, l)
                elif sum > 0:
                    r = self.dec(r, l)
                else:
                    l = self.inc(l, r)
            i = self.inc(i, len(num)-2)
        return results

def runtest(num):
    sol = Solution()
    print "%s result is %s" % (num, sol.threeSum(num))

if __name__ == "__main__":
    runtest([0,0,0]) 
    runtest([0,0,0,0,0])
    runtest([1,2,3,4])
    runtest([-3,-2,-1,0,1,2,3]) 
    runtest([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
    runtest([7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15])
