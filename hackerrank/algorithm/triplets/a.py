#!/usr/bin/env python

import sys

def run_test(arr_size, arr):
    result = 0
    # Write code to compute the number of triplets as required, and store that value in 'result'
    res = []
    analyzed = set()
    for i in xrange(arr_size):
        if arr[i] in analyzed:
            continue

        la = set()
        ra = set()
        lam = set()
        ram = set()

        j = i - 1
        while j >= 0:
            assert arr[j] != arr[i]
            if arr[j] < arr[i]:
                la.add(arr[j])
            j -= 1
        j = i + 1
        while j < arr_size:
            if arr[j] == arr[i]:
                ram = ra
                ra = set()
            elif arr[j] < arr[i]:
                if not ram:
                    lam.add(arr[j])
            elif arr[j] > arr[i]:
                ra.add(arr[j])
            j += 1

        print "%d %s %s %s %s" % (arr[i], la, ram, lam, ra)
        result += 
        for l in la:
            for r in ra:
                res.append([l, arr[i], r])
        analyzed.add(arr[i])

    print res

    print result
    return result

def golden(size, arr):
    res = set()
    for i in xrange(size):
        for j in xrange(i+1, size):
            for k in xrange(j+1, size):
                if arr[i] < arr[j] and arr[j] < arr[k]:
                    res.add((arr[i], arr[j], arr[k]))
    print "golden: %s" % (res)
    return len(res)

def read_test():
    arr_size = int(sys.stdin.readline())
    arr = map(int, sys.stdin.readline().split())

def valid(p, has_set, twice_set):
    res = p not in twice_set
    if p in has_set:
        twice_set.add(p)
    has_set.add(p)
    return res

def random_test():
    import random
    size = random.randint(0, 10)
    arr = []
    has_set = set()
    twice_set = set()
    for i in xrange(size):
        p = random.randint(0, 5)
        while not valid(p, has_set, twice_set):
            p = random.randint(0, 5)
        arr.append(p)
    print has_set
    print twice_set
    print "input: %s" % (arr)
    res = run_test(size, arr)
    res2 = golden(size, arr)
    assert res == res2

def random_tests():
    for i in xrange(10):
        random_test()

if __name__ == "__main__":
    random_tests()

