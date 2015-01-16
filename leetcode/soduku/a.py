#!/usr/bin/env python

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(9):
            vertical = set()
            horical = set()
            sqr = set()
            a0 = []
            a1 = []
            a2 = []
            for j in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] in vertical:
                        print "v: [%d,%d] %s" % (i, j, vertical)
                        return False
                    vertical.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in horical:
                        print "h: [%d,%d] %s" % (j, i, horical)
                        return False
                    horical.add(board[j][i])
                pi = j/3 + (i/3)*3
                pj = j%3 + (i%3)*3
                if board[pi][pj] != '.':
                    if board[pi][pj] in sqr:
                        print "s: [%d,%d] %s" % (pi, pj, sqr)
                        return False
                    sqr.add(board[pi][pj])
                a0.append((i, j))
                a1.append((j, i))
                a2.append((pi, pj))
            print a0
            print a1
            print a2
                
        # assert 0, "%s" % (s)
        # print s
        return True


if __name__ == "__main__":
    board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
    Solution().isValidSudoku(board)
