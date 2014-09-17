#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ntol(r):
    res = []
    it = r
    while it is not None:
       res.append(it.val)
       it = it.next
    return res

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        def rev(start, n):
            if n == 0:
                return start, start
            assert start is not None, "%d" % (n)
            nh, nt = rev(start.next, n-1)
            if nh is None:
                assert nt is None
                assert n == 2
                return start, start
                
            assert nh is not None and nt is not None
            start.next = nt.next
            nt.next = start
            return nh, start
            
        start = head
        for i in range(m-1):
            start = start.next
        
        nh, nt = rev(start, n-m)
        if m == 1:
            return nh
        it = head
        for i in range(m-2):
            it = it.next
        assert it != nh
        it.next = nh
        return head

def gentest(l):
    if l is None or len(l) == 0:
        return None
    h = ListNode(l[0])
    it = h
    for i in range(1, len(l)):
        it.next = ListNode(l[i])
        it = it.next
    return  h

if __name__ == "__main__":
    sol = Solution()
    l = [3, 5]
    head = gentest(l)
    r = sol.reverseBetween(head, 1, 1)
    print "input: %s, m=%d, n=%d, result is %s" % (l, 1, 1, ntol(r))

    head = gentest(l)
    r = sol.reverseBetween(head, 1, 2)
    print "input: %s, m=%d, n=%d, result is %s" % (l, 1, 2, ntol(r))

    l = [3, 5, 6, 7, 8]
    head = gentest(l)
    r = sol.reverseBetween(head, 4, 4)
    print "input: %s, m=%d, n=%d, result is %s" % (l, 1, 1, ntol(r))

    head = gentest(l)
    r = sol.reverseBetween(head, 4, 5)
    print "input: %s, m=%d, n=%d, result is %s" % (l, 4, 5, ntol(r))

    head = gentest(l)
    r = sol.reverseBetween(head, 1, 5)
    print "input: %s, m=%d, n=%d, result is %s" % (l, 1, 1, ntol(r))
