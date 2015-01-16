#!/usr/bin/env python


def run_test(n, m, power, bullet):
    prev_dict = {}
    cur_dict = {}
    for i in xrange(n):
        ri = n-1-i
        for j in xrange(m):
            if i == 0:
                cur_dict[power[ri][j]] = power[ri][j]
            else:
                new_k = power[ri][j]
                for k, v in prev_dict.items():
                    all_bullet = new_k + k - min(v, bullet[ri][j])
                    if cur_dict.has_key(all_bullet):
                        cur_dict[all_bullet] = min(new_k, cur_dict[all_bullet])
                    else:
                        cur_dict[all_bullet] = new_k
        prev_dict = {}
        for c, t in cur_dict.items():
            small = True
            for c1, t1 in cur_dict.items():
                if c1 < c and t1 < t:
                    small = False
                    break
            if small:
                prev_dict[c] = t
        # print "%s" % (prev_dict)
        cur_dict = {}
    smallest = None
    for t in prev_dict.keys():
        if smallest is None or t < smallest:
            smallest = t
    print smallest
    return smallest

def mtest1():
    n = 3
    m = 3
    power = [[1, 2, 3], [3, 2, 1], [3, 2, 1]]
    bullet = [[1, 2, 3], [3, 2, 1], [1, 2, 3]]
    run_test(n, m, power, bullet)

def mtest2():
    n = 3
    m = 2
    power = [[1, 8], [6, 1], [4, 6]]
    bullet = [[2, 1], [4, 1], [3, 1]]
    run_test(n, m, power, bullet)

def mtest3():
    n = 3
    m = 3
    power = [[3, 2, 5], [8, 9, 1], [4, 7, 6]]
    bullet = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    run_test(n, m, power, bullet)

def mtest3():
    n = 3
    m = 2
    power = [[5, 10], [50, 60], [20, 25]]
    bullet = [[5, 50], [5, 20], [1, 1]]
    run_test(n, m, power, bullet)

def manual_test():
    mtest1()
    mtest2()
    mtest3()

if __name__ == "__main__":
    manual_test()
