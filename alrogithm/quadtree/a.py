#!/usr/bin/env python


class Node:
    def __init__(self, i0, j0, i1, j1):
        self.i0 = i0
        self.j0 = j0
        self.i1 = i1
        self.j1 = j1
        self.gcd = None

        # self.gcd_0 = None # [0,0] to [i,j]
        # self.gcd_1 = None # [0,j+1] to [i+1,m]
        # self.gcd_2 = None # [i+1,0] to [n,j+1]
        # self.gcd_3 = None # [i+1,j+1] to [n,m]
        self.nodes = [None]*4

    def set_gcd(self, v):
        self.gcd = v
    def get_gcd(self):
        return self.gcd

    def p(self, ind = 0):
        def str_ind(ind):
            return "  " * ind
        print "%s[%d,%d] to [%d, %d], gcd: %s" % (str_ind(ind), self.i0, self.j0, self.i1, self.j1, self.gcd)
        for node in self.nodes:
            if node is None:
                print "%sNone" % (str_ind(ind+1))
            else:
                node.p(ind+1)

def cal_gcd(a, b):
    if a is None:
        return b
    if b is None:
        return a
    assert isinstance(a, int), "%s" % (a)
    assert isinstance(b, int), "%s" % (b)
    if a < b:
        return cal_gcd(b, a)
    if a % b == 0:
        return b
    return cal_gcd(b, a % b)


def cal_gcd_list(l):
    if not l:
        return None
    res = None if l[0] is None else l[0].gcd
    for i in xrange(1, len(l)):
        res = cal_gcd(res, None if l[i] is None else l[i].gcd)
    return res

class QuadTree:
    def __init__(self, matrix):
        self.matrix = matrix
        self.root = self.construct(0, 0, len(matrix)-1, len(matrix[0])-1)
        self.root.p()

    def construct(self, i0, j0, i1, j1):
        if i0 > i1 or j0 > j1:
            return None
        assert i0 < len(self.matrix)
        assert i1 < len(self.matrix)
        assert j0 < len(self.matrix[0])
        assert j1 < len(self.matrix[0])

        res = Node(i0, j0, i1, j1)

        if i0 == i1 and j0 == j1:
            res.set_gcd(int(self.matrix[i0][j0]))
            return res

        nodes = [None]*4
        ih = (i0+i1)/2
        jh = (j0+j1)/2
        nodes[0] = self.construct(i0, j0, ih, jh)
        nodes[1] = self.construct(i0, jh+1, ih, j1)
        nodes[2] = self.construct(ih+1, j0, i1, jh)
        nodes[3] = self.construct(ih+1, jh+1, i1, j1)
        res.nodes = nodes

        res.set_gcd(cal_gcd_list(nodes))
        return res 

def read_file():
    p = open("read.txt", 'r')
    matrix = []
    for l in p:
        line = l.strip().split(' ')
        matrix.append(line)
    print "%s" % (matrix)
    p.close()

    tree = QuadTree(matrix)
    

if __name__ == "__main__":
    read_file() 
