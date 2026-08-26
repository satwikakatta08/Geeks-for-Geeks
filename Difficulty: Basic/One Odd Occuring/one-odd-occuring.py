class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        c=0
        for i in arr:
            c^=i
        return c