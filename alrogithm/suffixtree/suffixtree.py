#!/usr/bin/env python

class Node:
    def __init__(self, p, v):
        self.v = v
        self.p = p
        if self.p is not None:
            self.p.branches.append(self)
        self.branches = []
        self.prevsuffix = None
        self.nextsuffix = None
        self.issuffix = self.p is not None

        assert self.p is not None or self.v == ""

    def isroot(self):
        return not self.v

    def update(self, v):
        self.v += v

    def pp(self, ind=0):
        def str_ind(ind):
            return "  "*ind

        print "%s-%s %s" % (str_ind(ind), self.v, self.issuffix)
        for subnode in self.branches:
            subnode.pp(ind+1)

class ListNode:
    def __init__(self, node):
        self.node = node
        self.prev = None
        self.nex = None



class SuffixTree:
    def __init__(self):
        self.root = Node(None, "")
        self.suffix_begin = None
        self.suffix_end = None
        self.leafs = []

    def addsuffix_prev(self, prev, sub):
        assert prev is not None
        sub.nextsuffix = prev.nextsuffix
        prev.nextsuffix = sub
        if prev == self.suffix_end:
            self.suffix_end = sub

    def addsuffix_end(self, sub):
        if self.suffix_root is None:
            self.suffix_root = sub
        else:
            self.suffix_end.nextsuffix = sub

        self.suffix_end = sub

    def addsuffix(self, node, c):
        if node.issuffix:
            if node.isroot():
                pass
            elif node.branches:
                new_node = Node(node, c)
                node.issuffix = False
                node.nextsuffix = None
            else:
                node.update(c)

    def add(self, c):
        s = self.suffix_root
        while s is not None:
            self.addsuffix(s, c)
            s = s.nextsuffix

        inside = False
        for l in self.root.branches:
            if l.v[0] == c:
                assert not inside
                if len(l.v) == 1:
                    l.issuffix = False
                else:
                    new_node = Node(l, l.v[1:])
                    l.v = c
                inside = True
         
        if not inside:
            sub = Node(self.root, c)
            self.leafs.append(sub)
            self.addsuffix_end(sub)

    def p(self):
        print "print tree:"
        assert self.root is not None
        self.root.pp()

def build_test(ss):
    tree = SuffixTree()
    for c in ss:
        tree.add(c)
        tree.p()

if __name__ == "__main__":
    build_test("bananas")


