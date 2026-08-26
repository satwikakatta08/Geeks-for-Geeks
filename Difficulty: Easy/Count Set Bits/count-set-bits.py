class Solution:
    def setBits(self, n):
        # code here
        c=0
        while n>0:
            c+=n&1
            n>>=1
        return c