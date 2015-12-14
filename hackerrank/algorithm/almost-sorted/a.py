#!/usr/bin/env python

def test(n, nums):
    assert n == len(nums)
    mmax = []
    stk = []
    for i in xrange(n):
        # print "i = %d" % (i)
        mmax.append(i)
        while stk and nums[i] >= nums[stk[-1]]:
            stk.pop()
        if not stk:
            mmax[i] = 0
        else:
            mmax[i] = stk[-1]+1
        stk.append(i)
       
    mmin = [0] * n
    stk = []
    for i in xrange(n-1, -1, -1):
        mmin[i] = i
        while stk and nums[i] <= nums[stk[-1]]:
            stk.pop()
        if not stk:
            mmin[i] = n-1
        else:
            mmin[i] = stk[-1]-1
        stk.append(i)
 
    res = 0
    for j in xrange(n):
        for i in xrange(mmax[j], j+1):
            # if j <= mmin[i] and i >= mmax[j]:
            if j <= mmin[i]:
                res += 1
    print res
    return res

def test2(n, nums):
    stk = []
    stk2 = []
    sub_res = [1] * n
    mmin = nums[0]
    for i in xrange(n):
        while stk and nums[i] >= nums[stk[-1]]:
            sub_res[i] += sub_res[stk[-1]]
            stk.pop()
        if nums[i] < mmin:
            mmin = nums[i]
            stk = []
        stk.append(i)
    print "%s" % (sub_res)
    res = 0
    for i in sub_res:
        res += i
    print res
    return res

def read_line_int_lst():
    l = raw_input()
    l = l.split(' ')
    res = []
    for r in l:
        res.append(int(r))
    return res

def oj_test():
    n = int(raw_input())
    nums = read_line_int_lst()
    test2(n, nums)

def slow(n, nums):
    res = 0
    for i in xrange(n):
        for j in xrange(i, n):
            min_true = True
            min_false = True
            for k in xrange(i,j+1):
                if k != i and nums[k] < nums[i]:
                    min_true = False
                    break
                if k != j and nums[k] > nums[j]:
                    min_false = False
                    break
            if min_true and min_false:
                res += 1
    print res
    return res

def random_atest(size, rrange):
    import random
    # size = random.randint(1, 50000)
    nums = []
    for i in xrange(size):
        nums.append(random.randint(1, rrange))
    res1 = test2(size, nums)
    if size <= 500:
        res2 = slow(size, nums)
        assert res1 == res2, "%s, %d %d" % (nums, res1, res2)

def random_test():
    for i in xrange(1000):
        random_atest(5, 50)
    for i in xrange(10):
        random_atest(50, 500)
    random_atest(50000, 500000)

if __name__ == "__main__":
    random_test()

