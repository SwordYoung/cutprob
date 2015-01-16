#!/usr/bin/env python

if __name__ == "__main__":
    p = range(0,10)
    res = p[:]
    while len(p) != 0:
        new_p = []
        for s in p:
            print "s = %d" % (s)
            l = len("%d" % s)
            if l == 1:
                l = 2
            print "l = %d, l * s = %d, 10** = %d" % (l, l * s, 10 ** (l))
            while l * s >= 10 ** (l-1):
                print "l = %d, l * s = %d, 10** = %d" % (l, l * s, 10 ** (l+1))
                if len("%d" % (l*s)) == l and (l*s) < 1000000000000000000:
                    new_p.append(l * s)
                l += 1
        new_p.sort()
        res.extend(new_p)
        p = new_p
        print "new_p: %s" % (new_p)
    res.sort()
    print res
