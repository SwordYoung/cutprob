#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def p(self):
        res = "%d" % (self.val)
        it = self.next
        while it is not None:
            res += " -> %d" % (it.val)
            it = it.next
        print res

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        fh = ListNode(-9999)
        fh.next = head

        cur = fh.next

        while cur.next is not None:
            p = cur.next
            it = fh
            while it.val < cur.val and it.next is not None:
                it = it.next
            if it == res and it.val >= cur.val:
                res = cur
                cur.next = it
            elif it.next is None:
                it.next = cur
                cur.next = None
            else:
                cur.next = it.next
                it.next = cur
            cur = p
        return res

def basic_test():
    head = None
    it = None
    for i in xrange(5000):
        new_node = ListNode(5000-i)
        if it is None:
            head = new_node
            it = new_node
        else:
            it.next = new_node
            it = it.next
    head.p()
    sol = Solution()
    res = sol.insertionSortList(head)
    res.p()

if __name__ == "__main__":
    basic_test()
