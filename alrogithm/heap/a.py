#!/usr/bin/env python

class Element():
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def inc(self):
        self.v += 1

    def __cmp__(self, b):
        return self.v.__cmp__(b.v)

    def __str__(self):
        return "%d:%d" % (self.k, self.v)

    def __repr__(self):
        return "%d:%d" % (self.k, self.v)

    def __hash__(self):
        return self.k.__hash__()

class Heap():
    def __init__(self):
        self.datas = []
        self.data_pos = {}

    def empty(self):
        return not self.datas

    def add(self, element):
        assert not self.data_pos.has_key(element)
        self.datas.append(element)
        p = len(self.datas)-1
        self.data_pos[element] = p

        self.up_modify(p)
        self.check()

    def top(self):
        if not self.datas:
            return None
        return self.datas[0]

    def check(self, c = 0):
        left = c*2+1
        right = c*2+2
        if left < len(self.datas):
            assert self.datas[left] <= self.datas[c], "%s" % (self.datas)
            self.check(left)
        if right < len(self.datas):
            assert self.datas[right] <= self.datas[c], "%s" % (self.datas)
            self.check(right)

    def remove(self):
        self.swap(0, len(self.datas)-1)
        del self.data_pos[self.datas[-1]]
        self.datas.pop()
        self.down_modify(0)
        self.check()

    def update(self, element):
        assert self.data_pos.has_key(element), "%s\n%s" % (element, self.data_pos)
        p = self.data_pos[element]
        self.up_modify(p)
        self.down_modify(p)
        self.check()

    def swap(self, p1, p2):
        self.data_pos[self.datas[p1]] = p2
        self.data_pos[self.datas[p2]] = p1

        tmp = self.datas[p1]
        self.datas[p1] = self.datas[p2]
        self.datas[p2] = tmp

    def up_modify(self, p):
        if p == 0:
            return
        np = (p-1)/2
        if self.datas[np] < self.datas[p]:
            self.swap(np, p)
            self.up_modify(np)

    def down_modify(self, p):
        left = p*2+1
        right = p*2+2
        largest = p
        if left < len(self.datas) and self.datas[left] > self.datas[largest]:
            largest = left
        if right < len(self.datas) and self.datas[right] > self.datas[largest]:
            largest = right
        if largest != p:
            self.swap(largest, p)
            self.down_modify(largest)

    def p(self):
        print "self.datas: %s" % (self.datas)
        print "self.data_pos: %s" % (self.data_pos)
        assert len(self.datas) == len(self.data_pos)
        for a, b in self.data_pos.items():
            assert self.datas[b] == a

class Counter():
    def __init__(self):
        self.datas = {}
        self.heap = Heap()

    def add(self, v):
        if v in self.datas:
            e = self.datas[v]
            assert self.heap.data_pos.has_key(e)
            e.inc()
            self.heap.update(e)
        else:
            self.datas[v] = Element(v, 1)
            self.heap.add(self.datas[v])

    def p(self):
        res = []
        while not self.heap.empty():
            t = self.heap.top()
            res.append(t)
            self.heap.remove()
            self.heap.p()
            if len(res) >= 2:
                assert res[-1].v <= res[-2].v, "%s" % (res)
        print "result is %s" % (res)

def read_file():
    with open("read.txt", 'r') as in_file:
        c = Counter()
        for a in in_file:
            c.add(int(a))
        c.p()

def random_input(times):
    import random
    c = Counter()
    for i in xrange(times):
        c.add(random.randint(0, 10))
    c.p()

if __name__ == "__main__":
    random_input(1000)
