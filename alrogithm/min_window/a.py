#!/usr/bin/env python

class Checker:
    def __init__(self, T):
        self.char_dict = {}
        for x in T:
            if self.char_dict.has_key(x):
                self.char_dict[x] += 1
            else:
                self.char_dict[x] = 1
        
    def add(self, x):
        if self.char_dict.has_key(x):
            self.char_dict[x] -= 1
            return self.char_dict[x]
        return None
        
    def remove(self, x):
        if self.char_dict.has_key(x):
            self.char_dict[x] += 1
            return self.char_dict[x]
        return None
    
    def full(self):
        for k, v in self.char_dict.items():
            if v > 0:
                return False
        return True

    def __str__(self):
        return self.char_dict.__str__()

    def p(self):
        print self.char_dict

class Solution:
    # @return a string
    def minWindow(self, S, T):
        checker = Checker(T)
        # init
        i = 0
        while i < len(S) and not checker.full():
            checker.add(S[i])
            i += 1
        if not checker.full():
            return ""
            
        mmin = i
        res_mmin = S[:i]
        
        j = i
        i = 0
        while i < len(S) and j <= len(S):
            print "i=%d, j=%d, checker=%s" % (i, j, checker)
            x = checker.remove(S[i])
            if x is not None:
                while x > 0 and j < len(S):
                    xp = checker.add(S[j])
                    if S[j] == S[i]:
                        x = xp
                    j += 1
                if x > 0:
                    break
            i += 1
            new_len = j - i
            print "i=%d, j=%d, x=%s, checker=%s" % (i, j, x, checker)
            if (x is None or x <= 0) and new_len < mmin:
                mmin = new_len
                res_mmin = S[i:j]
                assert mmin >= len(T)
                
        return res_mmin

def test(s, t):
    sol = Solution()
    res = sol.minWindow(s, t)
    print "S = %s, T = %s, res = %s" % (s, t, res)

def manual_test():
    # test("ab", "a")
    test("bba", "ab")
    # test("b", "a")
    # test("", "a")
    # test("a", "a")
    # test("cabcaabac", "aab")
    # test("cabcabcac", "aab")

if __name__ == "__main__":
    manual_test()
