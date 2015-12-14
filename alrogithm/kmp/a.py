#!/usr/bin/env python

def issubstr(s, f):
    k = [0] * len(f)
    k[0] = -1
    k[1] = 0
    i = 2
    cnd = 0
    while i < len(k):
        if f[i-1] == f[cnd]:
            cnd += 1
            k[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = k[cnd]
        else:
            k[i] = 0
            i += 1
    print k

    m = 0
    i = 0
    while m + i < len(s):
        if f[i] == s[m+i]:
            i += 1
            if i == len(f):
                return True
        else:
            if k[i] > -1:
                m = m+i-k[i]
                i = k[i]
            else:
                i = 0
                m += 1

def test(s, f):
    print "substr(%s, %s): %s" % (s, f, "True" if issubstr(s, f) else "False")

if __name__ == "__main__":
    test("abcdefgabcdabcdabcd", "abcdabc")
    test("abcdefgaaabaaabbcdabcdabcd", "aabaaab")
    test("abcdefgaaabaaabbcdabcdabcd", "abcdaabcab")

