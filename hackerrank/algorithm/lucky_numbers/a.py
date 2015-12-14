#!/usr/bin/env python

res = []
for i in xrange(2, 1459):
    su = True
    for j in xrange(2, i):
        if i % j == 0:
            su = False
            break
    if su:
        res.append(i)
print res
print "%d" % (len(res))

sqr = {1:1, 4:2, 9:3, 16:4, 25:5, 36:6, 49:7, 64:8, 81:9}

def getsu(i, ddct, n, mmin):
    # print "i = %d, n = %d, mmin = %d" % (i, n, mmin)
    if i > 81 * n:
        return []
    if ddct.has_key((i, n, mmin)):
        return ddct[(i, n, mmin)]
    if n == 1:
        return [[sqr[i]]] if sqr.has_key(i) and sqr[i] >= mmin else []
    res = []
    for i1, i2 in sqr.items():
        subres = []
        if mmin > i2:
            continue
        if i == i1:
            subres = [[i2]]
        elif i > i1:
            sub_subres = getsu(i-i1, ddct, n-1, i2)
            subres = []
            for s in sub_subres:
                subres.append([i2] + s)
        else:
            subres = []
            break

        res.extend(subres)
    ddct[(i, n, mmin)] = res
    return res

ddct = {}
for i in res:
    getsu(i, ddct, 18, 1)

# print ddct

pres = set()

prim = set(res)
for s in ddct.values():
    for iis in s:
        sub_s = 0
        for tts in iis:
            sub_s += tts
        if sub_s in prim:
            pres.add(tuple(iis))

print len(pres)
