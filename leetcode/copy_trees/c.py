#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # @return a list of tree node
    def generate(self,s,t):
        '''recursion with left and right branches'''
        if s>t:return [None];
        if s==t:return [TreeNode(s)];
        re=[];
        for i in range(s,t+1):
            left=self.generate(s,i-1);
            right=self.generate(i+1,t);
            for l in left:
                for r in right:
                    tmp=TreeNode(i);
                    tmp.left=l;
                    tmp.right=r;
                    re.append(tmp);
        return re;
    def generateTrees(self, n):
        return self.generate(1,n);

def runtest(n):
    print "result2 contains %d" % (len(Solution().generateTrees(n)))

if __name__ == "__main__":
    runtest(10)
