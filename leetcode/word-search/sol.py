#!/usr/bin/env python

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def valid(board, mark, i, j, dir, c):
            i1 = i
            j1 = j
            if dir == 0:
                i1 += 1
            elif dir == 1:
                j1 += 1
            elif dir == 2:
                i1 -= 1
            elif dir == 3:
                j1 -= 1
            return i1 >= 0 and i1 < len(board) and j1 >= 0 and j1 < len(board[0]) and (not mark[i1][j1]) and board[i1][j1] == c, i1, j1
            
        def trav(word, mark, l, board, i, j):
            if l == len(word):
                return True
            for dir in range(4):
                v, i1, j1 = valid(board, mark, i, j, dir, word[l])
                if v:
                    mark[i1][j1] = True
                    if trav(word, mark, l+1, board, i1, j1):
                        return True
                    mark[i1][j1] = False
            return False

        mark = []
        start_cand = []
        for i in range(len(board)):
            sub_mark = []
            for j in range(len(board[0])):
                sub_mark.append(False)
                if board[i][j] == word[0]:
                    start_cand.append([i,j])
            mark.append(sub_mark)
        for start_i in start_cand:
            mark[start_i[0]][start_i[1]] = True
            if trav(word, mark, 1, board, start_i[0], start_i[1]):
                return True
            mark[start_i[0]][start_i[1]] = False
        return False

if __name__ == "__main__":
    sol = Solution()
    board =["abc", "abc"]
    word = "cbbc"
    print sol.exist(board, word)

