#!/usr/bin/env python

def inpos_search(res, l, r, v):
    if l == r:
        return l
    m = (l+r)/2
    if res[m] == v:
        return m
    elif res[m] < v:
        return inpos_search(res, m+1, r, v)
    else:
        return inpos_search(res, l, m, v)

def test(nums):
    res = [0]
    for i in xrange(0, len(nums)):
        if nums[i] >= res[-1]:
            res.append(nums[i])
        else:
            in_pos = inpos_search(res, 0, len(res)-1, nums[i])
            assert in_pos < len(res), "%s %d %d" % (res, in_pos, nums[i])
            res[in_pos] = nums[i]
    print "%s %d" % (nums, len(res)-1)
    return len(res)-1

def manual_test():
    n = int(raw_input())
    nums = []
    for i in xrange(n):
        nums.append(int(raw_input()))
    print test(nums)

def test2(nums):
    res = [1] * len(nums)
    for i in xrange(1, len(nums)):
        for j in xrange(0, i):
            if nums[i] > nums[j]:
                res[i] = max(res[i], res[j]+1)
    mmax = 0
    for i in xrange(len(nums)):
        if res[i] > mmax:
            mmax = res[i]
    return mmax

def random_test():
    import random
    for i in xrange(100):
        nums = []
        for j in xrange(10):
            nums.append(random.randint(1, 200))
        a = test(nums)
        b = test2(nums)
        assert a == b, "%s %d %d" % (nums, a, b)

if __name__ == "__main__":
    random_test()
