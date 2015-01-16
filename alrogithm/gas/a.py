#!/usr/bin/env python

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        def prev(a, size):
            return a-1 if a > 0 else size-1
        def next(a, size):
            return a+1 if a < size-1 else 0
            
        gas_sum = 0
        for g in gas:
            gas_sum += g
        cost_sum = 0
        for c in cost:
            cost_sum += c
        
        if gas_sum < cost_sum:
            return -1
        
        start = 0
        while start < len(gas):
            print "start = %d" % (start)
            it = start
            prev_start = prev(start, len(gas))
            print "%d %d" % (it, prev_start)
            p = 0
            while p >= 0 and it != prev_start:
                p = p + gas[it] - cost[it]
                print "%d %d %d %d" % (p, it, gas[it], cost[it])
                it = next(it, len(gas))
            if p >= 0:
                return start
            start = it
        return -1

def test(gas, cost):
    sol = Solution()
    res = sol.canCompleteCircuit(gas, cost)

    print "input:"
    print "  %s" % (gas)
    print "  %s" % (cost)
    print "result: %d" % (res)

def manual_test():
    test([1, 7, 3, 8, 4], [4, 5, 7, 3, 1])

if __name__ == "__main__":
    manual_test()
