#!/usr/bin/env python

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def index(self, i):
        return self.A[i%len(self.A)]
        
    def findTarget(self, l, r, target):
        if l >= r:
            return l if self.index(l) == target else -1
        if self.index(r) < target:
            return -1
        if self.index(l) > target:
            return -1
            
        m = (l+r)/2
        if self.index(m) == target:
            return m
        elif self.index(m) < target:
            return self.findTarget(m+1, r, target)
        else:
            return self.findTarget(l, m-1, target)

    def truemin(self, p):
        return self.index(p) < self.index(p-1)    

    def findMin(self, l, r):
        if l == r:
            return l
            
        if self.A[l] < self.A[r]:
            return l
        elif self.A[l] > self.A[r]:
            m = (l+r) / 2
            if self.A[m] > self.A[r]:
                return self.findMin(m+1, r)
            else:
                return self.findMin(l+1, m)
        else:
            m = (l+r) / 2
            if self.A[m] > self.A[r]:
                return self.findMin(m+1, r)
            elif self.A[m] < self.A[r]:
                return self.findMin(l, m)
            min_pos_l = self.findMin(l, m)
            min_pos_r = self.findMin(m+1, r)
            return min_pos_l if self.truemin(min_pos_l) else min_pos_r
            
    def search(self, A, target):
        self.A = A
        min_pos = self.findMin(0, len(A)-1)
        print "min_pos is %d" % (min_pos)
        index = self.findTarget(min_pos, min_pos + len(A)-1, target)
        return index != -1
        
def runtest(num, t):
    print "result target %d and num %s is %s" % (t, num, Solution().search(num, t))

if __name__ == "__main__":
    runtest([3,1,1], 3)
    runtest([1,1,3,1], 3)
    runtest([1,2,1], 2)
