#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class HeapNode:
    def __init__(self, n):
        self.v = n.val

    def __cmp__(self, b):
        return self.v.__cmp__(b.v)

class Heap:
    def __init__(self):
        self.datas = []

    def is_empty(self):
        return not self.datas

    def add(self, node):
        self.datas.append(node)
        self.up_modify(len(self.datas)-1)

    def top(self):
        assert not self.is_empty()
        return self.datas[0]

    def remove(self):
        self.swap(0, len(self.datas)-1)
        self.datas.pop()
        self.down_modify(0)

    def up_modify(self, p):
        if p == 0:
            return
        parent = (p - 1) / 2
        if self.datas[parent] > self.datas[p]:
            self.swap(parent, p)
            self.up_modify(parent)
        
    def down_modify(self, p):
        largest = p
        left = p * 2 + 1
        right = p * 2 + 2
        if left < len(self.datas) and self.datas[largest] > self.datas[left]:
            largest = left
        if right < len(self.datas) and self.datas[largest] > self.datas[right]:
            largest = right
        if largest != p:
            self.swap(p, largest)
            self.down_modify(largest)

    def swap(self, l, r):
        tmp = self.datas[l]
        self.datas[l] = self.datas[r]
        self.datas[r] = tmp

    def check(self, p = 0):
        left = p * 2 + 1
        right = p * 2 + 2
        if left < len(self.datas):
            assert self.datas[p] <= self.datas[left], "%s %d %d" % (self.datas, p, left)
        if right < len(self.datas):
            assert self.datas[p] <= self.datas[right], "%s %d %d" % (self.datas, p, right)

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = Heap()
        for l in lists:
            if l not None:
                node = HeapNode(l)
                heap.add(node)

        res = []
        while not heap.is_empty():
            top_node = heap.top()
            res.append(top_node.v)

            heap.remove()
            np = top_node.n.next
            if np is not None:
                new_node = HeapNode(np)
                heap.add(new_node)

        return res

def sort(lists):
    # init
    heap = Heap()
    for l in lists:
        if l:
            node = HeapNode(l, 0)
            heap.add(node)

    res = []
    while not heap.is_empty():
        top_node = heap.top()
        res.append(top_node.v)

        heap.remove()
        if top_node.i+1 < len(top_node.l):
            new_node = HeapNode(top_node.l, top_node.i+1)
            heap.add(new_node)

    return res

def test(lists):
    print "input: %s" % (lists)
    res = sort(lists)
    print "result: %s" % (res)
    import copy
    res_oracle = copy.copy(res)
    res_oracle.sort()
    assert res == res_oracle

def test_manual():
    test([[1,3,5], [2,4]])

def test_random():
    import random
    lists = []
    for i in xrange(10):
        sub_list = []
        sub_size = random.randint(0, 20)
        for j in xrange(sub_size):
            sub_list.append(random.randint(0, 100))
        sub_list.sort()
        lists.append(sub_list)
    test(lists)

if __name__ == "__main__":
    test_manual()
    test_random()

