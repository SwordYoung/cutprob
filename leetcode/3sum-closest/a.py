#!/usr/bin/env python

class Solution:
    # @return an integer
    def inc(self, l, bound):
        l += 1
        while l < bound and self.n[l-1] == self.n[l]:
            l += 1
        return l
    def dec(self, r, bound):
        r -= 1
        while r > bound and self.n[r+1] == self.n[r]:
            r -= 1
        return r
    def sum2(self, pos1, val1, target):
        l = pos1+1
        r = len(self.n)-1
        while l < r:
            sum = self.n[l]+self.n[r]+val1
            m = sum - target if sum > target else target - sum
            if m == 0:
                self.result = target
                self.minus = m
                break
            elif self.minus is None or m < self.minus:
                self.minus = m
                self.result = sum
                
            if sum < target:
                l = self.inc(l, r)
            else:
                r = self.dec(r, l)
                
    def threeSumClosest(self, num, target):
        num.sort()
        self.n = num
        self.result = None
        self.minus = None
        
        i = 0
        while i < len(self.n)-2:
            self.sum2(i, self.n[i], target)
            if self.minus == 0 or self.n[i] > target/3:
                break
            i = self.inc(i, len(self.n)-2)
        return self.result

def runtest(num, target):
    print "solution for target %d and num %s is:\n%s" % (target, num, Solution().threeSumClosest(num, target))

if __name__ == "__main__":
    runtest([-3,-2,-5,3,-4], -1)
