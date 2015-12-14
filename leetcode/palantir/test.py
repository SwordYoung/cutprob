#!/usr/bin/env python

class Solution:
    def __init__(self):
        self.solution_dict = {}
        self.n_set = set()
        self.gcd = []
        
    def pre_quit(self, in_n, in_b, up_bound):
        if in_n < 0 or in_b < 0:
            return True, -1 # impossible
        if in_n == 0:
            return True, 0
        if in_n in self.n_set:
            return True, 1
        if in_n % self.gcd[in_b] != 0:
            return True, -1

        max_possible = in_n / self.in_b_numbers[in_b]
        if in_n % self.in_b_numbers[in_b] == 0:
            return True, max_possible
        if up_bound != -1 and max_possible >= up_bound:
            return True, -1
        
        return False, 0

    def find_solution(self, in_n, in_b, up_bound):
        is_pre_quit, ret_value = self.pre_quit(in_n, in_b, up_bound)
        if is_pre_quit:
            return ret_value

        max_possible = in_n / self.in_b_numbers[in_b]

        min_sum = -1
        min_iter = up_bound
        for i in xrange(max_possible, -1, -1):
            if min_iter == 0:
                break
            res = self.find_solution(in_n - self.in_b_numbers[in_b] * i, in_b-1, -1 if up_bound == -1 else up_bound-i)
            
            if res != -1:
                if min_iter == -1 or min_iter > res:
                    min_iter = res
                res = res + i
                if min_sum == -1 or min_sum > res:
                    min_sum = res
                    if up_bound == -1:
                        up_bound = min_sum
                
            if min_iter != -1:
                min_iter -= 1
                
        return min_sum
    
    def calculate_gcd(self):
        def cal_gcd(a, b):
            if a < b:
                return cal_gcd(b, a)
            if b == 0:
                return a
            return cal_gcd(a % b, b)
        
        self.gcd.append(self.in_b_numbers[0])
        for i in xrange(1, len(self.in_b_numbers)):
            self.gcd.append(cal_gcd(self.gcd[i-1], self.in_b_numbers[i]))
            

    def solve(self, in_n, in_b, in_b_numbers):
        self.in_n = in_n
        self.in_b_numbers = in_b_numbers
        self.in_b_numbers.sort()
        self.n_set = set(self.in_b_numbers)
        self.calculate_gcd()

        result = self.find_solution(in_n, in_b-1, -1)
        return result

def solve(in_n, in_b, in_b_numbers):
    print "input: n is %d, b is %d" % (in_n, in_b)
    print "in_b_numbers is %s" % (in_b_numbers)
    result = Solution().solve(in_n, in_b, in_b_numbers)
    if result == -1:
        print "IMPOSSIBLE"
    else:
        print result

# utility function for input
def read_line():
    line = raw_input()
    line = line.strip()
    return line

def read_strs():
    line = read_line()
    strs = line.split(' ')
    return strs

def read_numbers():
    nums = read_strs()
    for i in xrange(len(nums)):
        nums[i] = int(nums[i])
    return nums

def runtest():
    in_line1 = read_numbers()
    in_n = in_line1[0]
    in_b = in_line1[1]
    in_b_numbers = read_numbers()
    assert len(in_b_numbers) == in_b
    solve(in_n, in_b, in_b_numbers)

def runtests():
    num_tests = read_numbers()[0]
    for i in xrange(num_tests):
        runtest()

# if __name__ == "__main__":
if __name__ == "__test__":
    runtests()

# if __name__ == "__test__":
if __name__ == "__main__":
    infile = open("in.txt", 'r')
    import sys
    sys.stdin = infile
    runtests()
    infile.close()

