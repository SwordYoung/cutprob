#!/usr/bin/env python

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def check(self, board, x, y):
        p = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        vertical = set()
        horical = set()
        sqr = set()
        for i in xrange(9):
            if board[i][y] != '.' and board[i][y] in vertical:
                return False
            vertical.add(board[i][y])
            if board[x][i] != '.' and board[x][i] in horical:
                return False
            horical.add(board[x][i])
            px = x/3*3 + i/3
            py = y/3*3 + i%3
            if board[px][py] != '.' and board[px][py] in sqr:
                return False
            sqr.add('.')
        return True
            
    def getcan(self, board, x, y):
        p = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        for i in xrange(9):
            if board[i][y] in p:
                p.remove(board[i][y])
            if board[x][i] in p:
                p.remove(board[x][i])
            px = x/3*3 + i/3
            py = y/3*3 + i%3
            if board[px][py] in p:
                p.remove(board[px][py])

        return p
            
    def solve(self, board, i):
        if i == 81:
            return True
        
        x = i / 9
        y = i % 9
        if board[x][y] == '.':
            for c in self.getcan(board, x, y):
                board[x][y] = c
                if self.solve(board, i+1):
                    return True
            board[x][y] = '.'
        else:
            return self.solve(board, i+1)
        return False
                
    def solveSudoku(self, board):
        i = 0
        self.solve(board, i)

def testcase(board):
    for i in xrange(len(board)):
        board[i] = list(board[i])
    Solution().solveSudoku(board)
    for b in board:
        print ''.join(b)

def test():
    # testcase([".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."])
    # testcase(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
    testcase(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])

if __name__ == "__main__":
    test()
