#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def lton(l):
    if len(l) == 0:
        return None
    h = ListNode(l[0])
    it = h
    for i in range(1, len(l)):
        it.next = ListNode(l[i])
        it = it.next
    return h

def ntol(n):
    l = []
    it = n
    while it != None:
        l.append(it.val)
        it = it.next
    return l

class Solution:
    # @param head, a ListNode
    # @return nothing
    def trav(self, it, l, r):
        if l == r:
            nit = it.next
            it.next = None
            return it, it, nit
        elif l == r-1:
            nt = it.next
            nnt = nt.next
            it.next.next = None
            assert nt.next is None
            # print "ret: %d %d %d" % (it.val, nt.val, nnt.val)
            return it, nt, nnt
        
        nh, nt, nnt = self.trav(it.next, l+1, r-1)
        # print "l=%d r=%d %d %d %d" % (l, r, nh.val, nt.val, nnt.val)
        rt1 = nnt.next

        it.next = nnt
        nnt.next = nh

        # print "result: %s" % (ntol(it))
        # print "ret: %d %d" % (-1 if nnt is None else nnt.val, -1 if rt1 is None else rt1.val)
        return it, nnt, rt1
        
    def reorderList(self, head):
        if head is None:
            return
        ll = 0
        it = head
        while it != None:
            it = it.next
            ll += 1
        if ll == 0:
            return
        self.trav(head, 0, ll-1)

def test(nl):
    n = lton(nl)
    print "input: %s" % (nl)
    sol = Solution()
    sol.reorderList(n)
    il = ntol(n)
    print "output: %s" % (il)

if __name__ == "__main__":
    test([])
    test([1])
    test([1, 2])
    test([1, 2, 3, 4, 5, 6, 7, 8])
    test([1, 2, 3, 4, 5, 6, 7, 8, 9])
