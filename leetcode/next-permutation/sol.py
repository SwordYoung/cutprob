#!/usr/bin/env python

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        i = len(num)-2
        while i >= 0:
            if num[i] < num[i+1]:
                break
            i -= 1
        if i == -1:
            num.sort()
        else:
            p = i+1
            for j in range(len(num)-1, i, -1):
                if num[j] > num[i]:
                    p = j
                    break
            tmp = num[i]
            num[i] = num[p]
            num[p] = tmp
            t = num[i+1:]
            t.sort()
            num = num[:i+1] + t
        return num

def test(l):
    sol = Solution()
    print "input: %s" % (l)
    print "output: %s" % (sol.nextPermutation(l))

if __name__ == "__main__":
    test([1,2])
    test([2,1])
    test([1,1])
    test([1,1,5])
    test([1,5,1])
    test([2,5,1])
