#!/usr/bin/env python

# Enter your code here. Read input from STDIN. Print output to STDOUT

class TreeNode:
    def __init__(self, n):
        self.n = n
        self.prev = set()
    
    def addPrev(self, p):
        # p.next.append(self)
        self.prev.add(p.n)
        assert isinstance(self.prev, set)
        
    def removePrev(self, prevs):
        assert isinstance(self.prev, set)
        print "before: %s" % (list(self.prev))
        print "remove: %s" % (list(prevs))
        self.prev = self.prev - prevs
        print "after: %s" % (list(self.prev))
        assert isinstance(self.prev, set)
        
    def input_empty(self):
        return len(self.prev) == 0

class Solution:
    def __init__(self):
        self.node_dict = {}
    def add_connect(self, n1, n2):
        node1 = self.node_dict[n1]
        node2 = self.node_dict[n2]
        node2.addPrev(node1)
        
    def addsequence(self, seq):
        if len(seq) == 0:
            return None
        if not self.node_dict.has_key(seq[0]):
            self.node_dict[seq[0]] = TreeNode(seq[0])
        for i in xrange(1, len(seq)):
            if not self.node_dict.has_key(seq[i]):
                self.node_dict[seq[i]] = TreeNode(seq[i])
            self.add_connect(seq[i-1], seq[i])
            
    def getresult(self):
        nodes = self.node_dict.values()
        result = []
        while len(nodes) != 0:
            sub_result = []
            new_nodes = []
            for n in nodes:
                print "%d input is %d" % (n.n, len(n.prev))
                if n.input_empty():
                    sub_result.append(n.n)
                else:
                    new_nodes.append(n)
            sub_result.sort()
            nodes = new_nodes
            sub_set = set(sub_result)
            for n in nodes:
                n.removePrev(sub_set)
            result.extend(sub_result)
        return result

def read_num():
    line = raw_input()
    return int(line)

def read_nums():
    line = raw_input()
    strnums = line.split(' ')
    nums = []
    for s in strnums:
        nums.append(int(s))
    return nums

if __name__ == "__main__":
    n = read_num()
    sol = Solution()
    for i in xrange(n):
        p = read_num()
        nums = read_nums()
        sol.addsequence(nums)
    print 'INPUT DONE'
    result = sol.getresult()
    str_result = []
    for r in result:
        str_result.append("%d" % (r))
    print ' '.join(str_result)

