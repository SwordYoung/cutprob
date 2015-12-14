#!/usr/bin/env python

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def get_submax(self, heights):
        class StackNode:
            def __init__(self, h, start_pos):
                self.h = h
                self.start_pos = start_pos
            def __str__(self):
                return "%d:%d" % (self.h, self.start_pos)
            def __repr__(self):
                return "%d:%d" % (self.h, self.start_pos)
                
        stack = []
        mmax = 0
        for i in xrange(len(heights)):
            lp = i
            while stack and heights[i] <= stack[-1].h:
                top_node = stack.pop()
                # calculate the max
                sub_area = top_node.h * (i - top_node.start_pos)
                lp = top_node.start_pos
                if sub_area > mmax:
                    mmax = sub_area
            stack.append(StackNode(heights[i], lp))
            # print "%d : %s" % (i, stack)

        while stack:
            top_node = stack.pop()
            # calculate the max
            sub_area = top_node.h * (len(heights) - top_node.start_pos)
            if sub_area > mmax:
                mmax = sub_area
        
        return mmax
    
    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) == 0:
            return 0
            
        matrix_h = []
        for i in xrange(len(matrix)):
            sub_h = []
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '0':
                    sub_h.append(0)
                else:
                    sub_h.append(1 if i == 0 else matrix_h[i-1][j] + 1)
            matrix_h.append(sub_h)

        # print "%s" % (matrix_h)
        
        mmax = 0
        for i in xrange(len(matrix)):
            sub_max = self.get_submax(matrix_h[i])
            # print "submax for %d is %d" % (i, sub_max)
            if sub_max > mmax:
                mmax = sub_max
        return mmax

def test(matrix):
    sol = Solution()
    print "solution for matrix: %s" % (matrix)
    print "%d" % (sol.maximalRectangle(matrix))

def test_manual():
    matrix = [["010100"], ["011001"], ["011001"], ["111100"]]
    test(matrix)

def test_manual2():
    matrix = ["0"]
    test(matrix)

if __name__ == "__main__":
    test_manual()
    test_manual2()
