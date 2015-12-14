#!/usr/bin/env python

class Solution:
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

    def sum2(self, pos1, pos2, target):
        l = pos2+1
        r = len(self.n)-1
        while l < r:
            if self.n[l] > target/2 or self.n[r] < target/2:
                break
            if self.n[l] + self.n[r] == target:
                self.result.append([self.n[pos1], self.n[pos2], self.n[l], self.n[r]])
                l = self.inc(l, r)
                r = self.dec(r, l)
            elif self.n[l] + self.n[r] > target:
                r = self.dec(r, l)
            else:
                l = self.inc(l, r)

    def sum3(self, pos1, target):
        i = pos1+1
        while i < len(self.n)-2:
            self.sum2(pos1, i, target-self.n[i])
            i = self.inc(i, len(self.n)-2)
            if self.n[i] > target/3:
                break
        
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        self.n = num
        self.result = []

        i = 0
        while i < len(num)-3:
            self.sum3(i, target-self.n[i])
            i = self.inc(i, len(num)-3)
            if self.n[i] > target/4:
                break
        return self.result

def runtest(num, target):
    sol = Solution()
    print "solution for target %d and num %s is \n%s" % (target, num, sol.fourSum(num, target))

if __name__ == "__main__":
    runtest([-4,-3,-2,-1,0,1,2,3,4], 0)

