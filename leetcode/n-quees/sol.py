class Solution:
    # @return a list of lists of string
    def addresult(self, queues):
        assert len(queues) == self.n
        res_list = []
        for i in range(self.n):
            queue_line = ""
            for j in range(self.n):
                if j != queues[i]:
                    queue_line += "."
                else:
                    queue_line += "Q"
            res_list.append(queue_line)
        self.result.append(res_list)

    def getavail(self, queues):
        notaval = set(queues)
        for i in range(len(queues)):
            notaval.add(queues[i]-(len(queues)-i))
            notaval.add(queues[i]+(len(queues)-i))
        return self.vals - notaval

    def getResult(self, queues):
        assert queues is not None
        if len(queues) == self.n:
            self.addresult(queues)
            return
        avail = self.getavail(queues)
        for i in avail:
            self.getResult(queues+[i])

    def solveNQueens(self, n):
        self.n = n
        self.vals = set(range(n))
        self.result = []
        self.getResult([])
        return self.result

