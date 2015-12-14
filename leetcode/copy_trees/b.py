#!/usr/bin/env python

class Solution:
    def __init__(self):
        self.dic = {}
        self.dic[0] = 1
        self.dic[1] = 1
        
    def nums(self, n):
        if self.dic.has_key(n):
            return self.dic[n]
        sum = 0
        for i in range(1, n+1):
            sum += self.nums(i-1) * self.nums(n-i)
        self.dic[n] = sum
        return sum
        
    # @return an integer
    def numTrees(self, n):
        return self.nums(n)
        
def runtest(n):
    print "result for %d is %d" % (n, Solution().numTrees(n))

if __name__ == "__main__":
    runtest(8)
