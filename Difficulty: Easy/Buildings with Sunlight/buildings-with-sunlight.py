class Solution:
    def visibleBuildings(self, arr):
        # code here
        t=0
        mh=0
        for i in range(len(arr)):
            if arr[i]>=mh:
                t+=1
                mh=arr[i]
        return t            