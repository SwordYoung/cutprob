#!/usr/bin/env python

import sys
sys.setrecursionlimit(100000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.d = {}
        self.d[(1, 0)] = [TreeNode(1)]
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0:
            return []
        if self.d.has_key((n,0)):
            return self.d[(n, 0)]
            
        def cp(tree, inc = 0):
            if tree is None:
                return None
            new_tree = TreeNode(tree.val+inc)
            new_tree.left = cp(tree.left, inc)
            new_tree.right = cp(tree.right, inc)
            return new_tree
        def tree_max(tree):
            if tree.right is not None:
                return tree_max(tree.right)
            return tree
        
        result = []
        l_n = self.generateTrees(n-1)
        for subn in l_n:
            # n as root
            new_n_1 = cp(subn)
            new_root = TreeNode(n)
            new_root.left = new_n_1
            result.append(new_root)
            # n as right_most
            new_n_2 = cp(subn)
            new_max = tree_max(new_n_2)
            new_max.right = TreeNode(n)
            result.append(new_n_2)
        
        for i in range(1, n-1):
            l1_trees = self.generateTrees(i)
            l2_trees = []
            if self.d.has_key((n-1-i,i)):
                l2_trees = self.d[(n-1-i,i)]
            else:
                l2_trees = self.generateTrees(n-1-i)
                for i2 in range(len(l2_trees)):
                    l2_trees[i2] = cp(l2_trees[i2], i)
                self.d[(n-1-i,i)] = l2_trees
            for l1 in l1_trees:
                for l2 in l2_trees:
                    l1 = cp(l1)
                    l2 = cp(l2)
                    new_node = TreeNode(n)
                    l1_max = tree_max(l1)
                    l1_max.right = new_node
                    new_node.left = l2
                    result.append(l1)
            
        self.d[(n,0)] = result
        print "rrr %d %d" % (n, len(result))
        return result

def runtest(n):
    print "result1 contains %d" % (len(Solution().generateTrees(n)))

if __name__ == "__main__":
    runtest(10)
