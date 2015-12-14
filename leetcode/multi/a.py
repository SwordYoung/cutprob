#!/usr/bin/env python

import copy

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def mul(self, num, bit, shift):
        res = []
        if self.md.has_key(bit):
            res = copy.copy(self.md[bit])
            for i in range(shift):
                res.append(0)
        c = 0
        for i in range(len(num)):
            p = len(num)-1-i
            new_bit = num[p] * bit + c
            c = new_bit / 10
            res.append(str(new_bit % 10))
        if c != 0:
            res.append(c)
        res.reverse()
        self.md[bit] = copy.copy(res)
        for i in range(shift):
            res.append(0)
        return res
    
    def add(self, sum, add):
        l = len(sum) if len(sum) > len(add) else len(add)
        res = []
        c = 0
        for i in range(l):
            add_l = 0 if i >= len(sum) else int(sum[len(sum)-1-i])
            add_r = 0 if i >= len(add) else int(add[len(add)-1-i])
            new_bit = add_l + add_r + c
            res.append(new_bit % 10)
            c = new_bit / 10
        if c != 0:
            res.append(c)
        res.reverse()
        return res
        
    def multiply(self, num1, num2):
        self.md = {}
        self.md[0] = [0]
        
        n1 = []
        n2 = []
        for i in range(len(num1)):
            n1.append(int(num1[i]))
        for i in range(len(num2)):
            n2.append(int(num2[i]))
        
        adds = []
        for i in range(len(n2)):
            newadd = self.mul(n1, n2[len(n2)-1-i], i)
            adds.append(newadd)
        sum = [0]
        for i in range(len(adds)):
            sum = self.add(sum, adds[i])
        for i in range(len(sum)):
            sum[i] = str(sum[i])
        return "".join(sum)

def runtest(num1, num2):
    print "%s * %s is %s" % (num1, num2, Solution().multiply(num1,num2))

if __name__ == "__main__":
    runtest("234", "123")
    runtest("81", "9") 
    runtest("81", "0") 
    runtest("81", "00000") 
    runtest("541644934491774045283078961835381765161522999", "32445413586334925683746578480905159611191044438197493062101111648822131235899910651987299520806")
    runtest("88994039749630997005046990281879989302276369350", "7107597799709428413456141937460470149011183145188544168453129168495306617")
    runtest("256117489511377083148593685533950561400363410418754703282767252221661609163404299", "61200496111643709081218550902198211480012378840070191147459688611759881218205422431757614")
