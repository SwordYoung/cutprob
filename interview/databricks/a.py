#!/usr/bin/env python

grid = "fxie amlo ewbx astu".split()
nrows, ncols = len(grid), len(grid[0])

# A dictionary word that could be a solution must use only the grid's
# letters and have length >= 3. (With a case-insensitive match.)
import re
alphabet = ''.join(set(''.join(grid)))

words = set(['fxie'])
prefixes = set(word[:i] for word in words
               for i in range(2, len(word)+1))

print prefixes

def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result

def extending(prefix, path):
    # print "prefix: %s path: %s" % (prefix, path)
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result

def neighbors((x, y)):
    if x > 0:
        yield(x-1, y)
    if x < ncols-1:
        yield(x+1, y)
    if y > 0:
        yield(x, y-1)
    if y < nrows-1:
        yield(x, y+1)

class It:
    def __init__(self):
        self.solver = solve()
        self.__getNext__()
        self.terminate = False

    def __getNext__(self):
        try:
            self.it = self.solver.next()
        except StopIteration:
            self.it = None
            self.terminate = True

    def hasNext(self):
        return not self.terminate

    def next(self):
        res = self.it
        self.__getNext__()
        return res

if __name__ == "__main__":
    #for t, p in solve():
        #print t, p
    it = It()
    while it.hasNext():
        print it.next()

