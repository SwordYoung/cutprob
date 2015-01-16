#!/usr/bin/env python

res_dict = {}

def possible(steps, lens):
    if steps == -1:
        return 2 ** lens

    if steps == 0:
        return 1

    if steps-1 > lens:
        return 0

    if res_dict.has_key((steps, lens)):
        return res_dict[(steps, lens)]

    res = possible(steps-1, lens-1) + possible(steps, lens-1)
    res_dict[(steps, lens)] = res
    return res
    

def run_test(n, nums):
    assert n > 0
    if not(nums[0] == '0' or nums[0] == '?'):
        print 0
        return 0
    if n == 2 and not (nums[1] == '1' or nums[1] == '?'):
        print 0
        return 0
    start = 1
    res = 1
    star_lens = 0
    for i in xrange(2, n):
        if nums[i] == '?':
            star_lens += 1
        else:
            if star_lens != 0:
                res *= possible(int(nums[i]) - start, star_lens)
            start = int(nums[i])
            star_lens = 0

    if star_lens != 0:
        res *= possible(-1, star_lens)
    print res
    return res    

def mtest1():
    run_test(3, ['?', '?', '?'])

def mtest2():
    run_test(6, ['0', '?', '?', '?', '2', '?'])
    run_test(2, ['1', '?'])

def manual_test():
    mtest1()
    mtest2()

def read_test():
    n = int(raw_input().strip())
    nums = raw_input().strip().split(' ')
    run_test(n, nums)

if __name__ == "__main__":
    manual_test()
    read_test()
