class Solution:
    def countFreq(self, arr, target):
        # code here
        t=0
        for i in arr:
            if i==target:
                t+=1
        return t